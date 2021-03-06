# Python Challenge

## Table of contents
  * [Introduction](#introduction)
    * [PyBank](#pybank)
    * [PyPoll](#pypoll)
  * [Output](#output)
  * [Technologies](#technologies)

## <a name="introduction"></a> Introduction
This project is to create two Python scripts, one for analyzing the financial records of a company, and the other for helping a small, rural town modernize its vote-counting process.
### <a name="pybank"></a> PyBank
* Inside a PyBank folder, you will find the following:
  * A python script file called main.py which is the main script to run for analyzing the financial records of a company
  * A "Resources" folder that contains the CSV file used, financial data called [budget_data.csv](./PyBank/Resources/budget_data.csv). The dataset is composed of two columns: Date and Profit/Losses.
  * An "Analysis" folder that contains a text file called financial_analysis.txt that has the results from the analysis

* The Python script will analyze the records to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

* The script will both print the analysis to the terminal and export a text file with the results.

### <a name="pypoll"></a> PyPoll
* Inside a PyPoll folder, you will find the following:
  * A python script file called main.py which is the main script to run for analyzing the votes
  * A "Resources" folder that contains the CSV file used, poll data called [election_data.csv](./PyPoll/Resources/election_data.csv). The dataset is composed of three columns: Voter ID, Country, and Candidate.
  * An "Analysis" folder that contains a text file called election_results.txt that has the results from the analysis.

* The Python script will analyze the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote

* The script will both print the analysis to the terminal and export a text file with the results.


## <a name="output"></a> Output
* PyBank
[financial_analysis.txt](./PyBank/Analysis/financial_analysis.txt)
```text
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```


* PyPoll
[election_results.txt](./PyPoll/Analysis/election_results.txt)
```text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-------------------------
Winner: Khan
-------------------------
```



## <a name="technologies"></a> Technologies
Project is created with:
* Python 3.8
