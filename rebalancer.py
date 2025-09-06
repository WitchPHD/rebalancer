import csv

folio_list = []
interval = 0.02

class FOLIO:
    # A Portfolio Class
    def __init__ (self, raw):
        self.name = raw.pop(0)
        self.holding_list = []
        self.percent = 0
        self.bal = 0
        self.deposit = 0
        self.tot_in = 0

        #populate portfolios from CSV
        while raw:
            name = raw.pop(0)
            amount = raw.pop(0)
            self.holding_list.append(HOLDING(name, amount))
        for holding in self.holding_list:
            self.percent += holding.ideal
        if round(self.percent, 2) != 1:
            print('\t ## WARNING ## Your ideal percentages in {:} do not add up to 100% ({:})'.format(self.name, self.percent))
        print('\t\tPortfolio {:} has {:} holdings'.format(self.name, len(self.holding_list)))

    def value(self):
        #get the value of portfolio
        for holding in self.holding_list:
            self.bal += holding.bal 
        self.tot_in = self.deposit + self.bal

    def basic_balancing(self):
        #print a basic output for each holding
        for holding in self.holding_list:
            holding.deposit = holding.ideal * self.deposit

    def manual_balancing(self, percent):
        #manual rebalancing with user indicated % normalization
        self.full_balancing()
        for holding in self.holding_list:
            holding.deposit = (percent * (self.deposit * holding.ideal)) + ((1-percent)*holding.deposit)

    def full_balancing(self):
        #full rebalancing including withdrawl
        for holding in self.holding_list:
            holding.deposit = (self.tot_in * holding.ideal) - holding.bal

    def default_balancing(self):
        #default zero-izing rebalancing
        percent = 0.0
        self.manual_balancing(percent)
        while self.is_neg():
            percent += interval
            self.manual_balancing(percent)
        print('\t Rebalancing with a Normalization of: {:.2f}%'.format(percent*100))

    def is_neg(self):
        for holding in self.holding_list:
            if holding.deposit < 0:
                return True

    def display_deposits(self):
        print('\t## {:} ## '.format(self.name))
        for holding in self.holding_list:
            print('\t\t{:} ~ ${:.0f}'.format(holding.ticker, holding.deposit))
    

class HOLDING:
    # a class for holdings in the portfolio
    def __init__ (self, ticker, amount):
        self.ticker = ticker
        self.ideal = float(amount)
        self.bal = 0
        self.deposit = 0
        
def load(cmd):
    #clear old data
    global folio_list
    folio_list = []
    # Load portfolios from file
    directory = 'ports.csv'
    if '-C' in cmd:
        directory = cmd.replace('load','')
        directory = directory.replace('-C','')
    print ('\tLoading from: {:}'.format(directory))
    with open(directory) as portfolio_file:
        portfolios = csv.reader(portfolio_file)
        line_count = 0
        for row in portfolios:
            folio_list.append(FOLIO(row))    

def rebalance(cmd):
    # First ask for money going in, and all current holdings amounts
    for folio in folio_list:
        folio.deposit = float(input('\tAmount going in {:}: '.format(folio.name)))
        for holding in folio.holding_list:
            holding.bal = float(input('\t\tCurrent amount in {:}: '.format(holding.ticker)))
        folio.value()
    # After, do the correct balancing method based on the modifier
    for folio in folio_list:
        if '-B' in cmd:
            folio.basic_balancing()
        elif '-M' in cmd: 
            num = cmd.replace('rebal','')
            num = num.replace('-M','')
            folio.manual_balancing(float(num))
        elif '-F' in cmd:
            folio.full_balancing() 
        elif '-I' in cmd: 
            num = cmd.replace('rebal','')
            num = num.replace('-I','')
            global interval
            interval = float(num)
            folio.default_balancing()
            interval = 0.02
        else:
            folio.default_balancing()
        # Finally, print the results
        folio.display_deposits()

if __name__ == '__main__':
    while True:
        # Main class accepts commands, then runs command based on input
        cmd = input('Enter CMD: ')
        if 'load' in cmd: 
            load(cmd)
        elif 'rebal' in cmd:
            rebalance(cmd)
        elif 'exit' in cmd:
            exit()
