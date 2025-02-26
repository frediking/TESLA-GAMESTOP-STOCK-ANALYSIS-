# Load all packages

import yfinance as yf
import pandas as pd
import requests
import warnings
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "iframe"



# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# Define Graphing Function

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))


# Using yfinance to extract Tesla stock Data

Tesla = yf.Ticker("TSLA")

tesla_data = Tesla.history(period="max")


# Reset the index of the dataframe

tesla_data.reset_index(inplace=True)
tesla_data.head(5)


# Webscraping to Extract Tesla Revenue Data from the webpage below.
# WEBPAGE = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm 

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
print(html_data)


# Parsing the html data.

beautiful_soup = BeautifulSoup(html_data, 'html.parser')


# Extracting the table with `Tesla Revenue` and storing it into a dataframe named `tesla_revenue` with columns `Date` and `Revenue`.
# PROCESSES
# 1. Create an Empty DataFrame
# 2. Find the Relevant Table
# 3. Check for the Tesla Quarterly Revenue Table
# 4. Iterate Through Rows in the Table Body
# 5. Extract Data from Columns
# 6. Append Data to the DataFrame


tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in beautiful_soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text.strip()
    revenue = col[1].text.strip()
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)


# Removing the commas and dollar sign from the `Revenue` column

tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(str).str.replace(r'[$,]', '', regex=True)
print(tesla_revenue)

# Remove all null or empty strings in the Revenue column.

tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


tesla_revenue.head()
tesla_revenue.tail()


# Using yfinance to Extract GameStop Stock Data

Gamestop = yf.Ticker('GME')


# Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`.

gme_data = Gamestop.history(period="max")
gme_data.head(5)

# **Reset the index of the dataframe

gme_data.reset_index(inplace=True)
gme_data.head(5)


# Using Webscraping to Extract GME Revenue Data from webpage below.

# WEBPAGE - https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. 

url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(url_2).text
print(html_data_2)


# Parse the html data 

beautiful_soup = BeautifulSoup(html_data_2, 'html.parser')


# Extracting the table with `GameStop Revenue` and storING it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. 
# USE SAME PROCESS AS USED IN THE EXTRACTION OF TESLA REVENUE DATA ABOVE.

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in beautiful_soup.find_all("tbody")[0].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text.strip()
    revenue = col[1].text.strip()
    gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

gme_revenue.tail()


# Plot Tesla Stock Graph

# Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.
# Checking columns of dataframe first
print(tesla_data.columns)

make_graph(tesla_data, tesla_revenue, Tesla)


# Plot GameStop Stock Graph
print(gme_data.columns)
make_graph(gme_data, gme_revenue, 'GameStop')