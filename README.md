# rebalancer
When you rebalance your holdings in a taxable portfolio it often requires withdrawing from some assets, which created a taxable event. I try to minimize/delay this with a "rolling rebalance" where, when my monthly autodeposit goes into the cash reserve of my portfolio, I curtail how much goes into each asset based on its curret% and target%. This is more formally known as "buy only value averaging."

This is a simple script I made while experimenting with vim to help me do this. 

# what to do
1. You must load your portfolios from a csv file. If you type "load" and hit enter it will load from "ports.csv" in the relative directory you're working from / cd-d into. If you type "load -C /pathhere/filehere.csv" it SHOULD load your custom location file. If the default load path is broken / you don't cd around in your terminal... just use "load -C " and then click and drag your file into the terminal window.
2. After loading the file you can type "rebal" and hit enter to begin rebalancing
3. You must then enter how much money is going into the account, and how much is currently in each holding.
4. It should output some amount of money for you to put into each holding
5. Use "exit" to close. Or put in a string at any other point IG there's no real error catching so you can just break it no big deal. 

# the rebalancing methods
1. The first balancing method is "Basic" from the command "rebal -B" - This just takes the ideal percentage of each asset and applies it directly to how much money is going in. If you want to automate your asset purchases as well as the deposit, you can use these numbers. 
2. The second method is "Full" from the comand "rebal -F" - This assumes that you're going to do a proper rebalance and withdraw assets from your overheld assets to add to your lower valued ones. When you get your numbers, withdraw the negative ammounts and deposit the positive ones.
3. The third method is "Manual" from "rebal -M 0.X" - Basically you can normalize your full rebelancing by weighting it to the basic rebalancing. For example, if you want your number to be 90% from basic and 10% from full, you can use "rebal -M 0.9" The numerical argument is the normalization weight (a percentage in decimal form).
4. The default method and the raison d'être of this script. If you use the command "rebal" by itself or with any other arguments you'll get this. Basically it tries different normalization weights until none of the values are negative. If you deposit this amount into each asset, and repeat each month, it will "course correcting" a bit over time without requiring a withdrawl. The script displays what % it settled on so that you can choose to do a full rebalance when the % gets higher than your liking.
5. During the last method / default rebalancing, it increments the normalization weight by 0.02 (2%). If you would like to round to larger or smaller intervals, you can use a different increment with "rebal -I 0.X" where the decimal is the percentage you want to increment by in decimal form. For example if you'd like to increment by 1%, use 0.01... if you would like to increment by 0.5%, use 0.005... etc
6. Finally, theres a truncating rebalancing method in "rebal -T" which removes all holdings you'd have to withdrawl from on a full rebalance from the asset list, and recalculates target % based on whats left, and then balances your deposit based only on putting money into the remaining deposits. This is useful for if your deposit is a small percent of your overall portfolio.

# the csv file
1. The CSV included is a sample, but you must change it manually to fit the portfolio you have if you end up using this script
2. Each line on the csv file is a different portfolio. You can keep a single line, or manage multiple. I have two, a IRA and a Taxable.
3. It's a CSV, so all the values are seperated by commas (big surprise)
4. The first value in each line is the portfolio name. Whop whop.
5. After that the values come in pairs of twos: [STOCK TICKER], [IDEAL PERCENTAGE]. You can keep adding pairs after that to accomidate more funds. If you mismatch the pairs... IDK the world might explode or something? It's a super simple script don't @ me
6. The ticker part is for human convenience. It will display whenever the script requires information from you, so it's important to know what holding its askinga bout.
7. The percentage is displayed in decimal form. Id est: "15%" must be "0.15"
8. When you run the load command, there will be a warning if any of your portfolios don't add up to 100%. It won't stop you from running the program, but the math will be wrong.
