# rebalancer
This is a simple script I made while experimenting with vim to help me rebalance my investment portfolio

# what to do
1. You must load your portfolios from a csv file. If you type "load" and hit enter it will load from "ports.csv" in its same directory. If you type "load -C /pathhere/filehere.csv" it SHOULD load your custom location file. I didn't test it. I don't know why you'd want to do that anyway. I don't know why I coded it.
2. After loading the file you can type "rebal" and hit enter to begin rebalancing
3. You must then enter how much money is going into the account, and how much is currently in each holding.
4. It should output some amount of money for you to put into each holding
5. Use "exit" to close. Or put in a string at any other point IG there's no real error catching so you can just break it no big deal. 

# the rebalancing methods
1. The first balancing method is "Basic" from the command "rebal -B" - This just takes the ideal percentage of each asset and applies it directly to how much money is going in.
2. The second method is "Full" from the comand "rebal -F" - This assumes that you're going to do a proper rebalance and withdraw assets from your overheld assets to add to your lower valued ones. When you get your numbers, withdraw the negative ammounts and deposit the positive ones.
3. The third method is "Manual" from "rebal -M 0.X" - Basically you can normalize your full rebelancing by weighting it to the basic rebalancing. For example, if you want your number to be 90% from basic and 10% from full, you can use "rebal -M 0.9" The numerical argument is the normalization weight.
4. The last method is the default and the raison d'être of this script. If you use the command "rebal" by itself or with any other arguments you'll get this. Basically I try to "rolling rebalance" weighting methods 1 and 2 until none of the numbers are negative. This reduces/delays the need for full withdrawing rebalances since you do a bit of "course correcting" over time. 

# the csv file
1. The CSV included is a sample, but you must change it manually to fit the portfolio you have if you end up using this script
2. Each line on the csv file is a different portfolio. You can keep a single line, or manage multiple. I have two, a IRA and a Taxable.
3. It's a CSV, so all the values are seperated by commas (big surprise)
4. The first value in each line is the portfolio name. Whop whop.
5. After that the values come in pairs of twos: [STOCK TICKER], [IDEAL PERCENTAGE] If you have an odd number of values... IDK the world might explode or something? It's a super simple script don't @ me
6. The ticker part is for human convenience. It will display whenever the script requires information from you, so it's important to know what holding its askinga bout.
7. The percentage is displayed in decimal form. Id est: "15%" must be "0.15"
8. When you run the load command, there will be a warning if any of your portfolios don't add up to 100%. It won't stop you from running the program, but the math will be wrong.
