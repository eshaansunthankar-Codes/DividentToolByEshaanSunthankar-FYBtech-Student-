# DividentToolByEshaanSunthankar-FYBtech-Student-
Divident tool used for comparison of 2 stocks and for watching the divident history of any stock using yfianance , Hope its helpful (done by a first year student )

This was easy to make there were  nested loops for selecting the data from the yfianance library and from the user who selects option 1 ad option 2 
option 1 :

 Option 1: View Dividend History of a Single Company
 Description:
The user selects this option to see the dividend payment history of a company (for example, TCS, Reliance, or HDFC Bank) from the year 2020 till the present.

 Logic (Easyyyy) :
The program shows a list of sample company stock symbols (like TCS.NS, INFY.NS).

The user inputs the stock symbol they want to check.

The script uses yfinance to get dividend data from Yahoo Finance.

It filters dividend payments from January 2020 onward.

The data is then plotted on a graph using matplotlib.

It also prints the average dividend paid during this time.

 Output:
A line chart showing dividend amounts vs. time.

Printed average dividend value in ₹.

Option 2 : 
  Compare Dividends of Two Companies
  
 Description:
The user selects this option to compare the dividend payouts of two companies side-by-side from 2020 onwards.

  (Logic):
Again, sample stock symbols are shown to guide the user.

The user inputs two valid stock symbols (e.g., ITC.NS and INFY.NS).

The program fetches dividend data for both.

It checks if both companies have valid dividend data since 2020.

If yes, it plots both companies’ dividend trends on one graph, with proper labels and legends.

The script also prints the average dividend for both companies.

Output:
A dual-line chart showing comparative dividend trends.

Printed average dividend values for each company.
