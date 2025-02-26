**TSLA & GME Stock Price and Revenue Analysis**  

## **Project Overview**  
This project fetches historical stock prices and revenue data for **Tesla (TSLA)** and **GameStop (GME)** using `yfinance` and web scraping. It processes this data and visualizes the historical trends using interactive plots created with **Plotly**.  

## **Features**  
- Fetches **TSLA** and **GME** stock price data from Yahoo Finance using `yfinance`.  
- Scrapes revenue data from online sources using `BeautifulSoup`.  
- Processes and cleans the retrieved data.  
- Generates interactive visualizations of **historical stock prices** and **company revenue** using `plotly`.  

---

## **Installation**  
### **Prerequisites**  
Ensure you have Python installed (>=3.7). Install the required dependencies using:  

```sh
pip install yfinance pandas requests beautifulsoup4 plotly
```

---

## **How It Works**  

### **1. Load Required Packages**  
The script imports essential Python libraries:  

- `yfinance`: Fetches stock data from Yahoo Finance.  
- `pandas`: Handles data manipulation and cleaning.  
- `requests`: Retrieves web content for scraping.  
- `bs4 (BeautifulSoup)`: Extracts revenue data from web pages.  
- `plotly.graph_objects`: Creates interactive visualizations.  

### **2. Define Graphing Function**  
A function `make_graph(stock_data, revenue_data, stock)` is created to:  
- Filter stock and revenue data up to specific dates.  
- Plot stock price trends in one subplot and revenue trends in another.  
- Add interactive elements like a date range slider.  

### **3. Fetch Tesla Stock Data**  
The script retrieves **Teslaâs** historical stock prices from Yahoo Finance using:  

```python
Tesla = yf.Ticker("TSLA")
tesla_data = Tesla.history(period="max")
tesla_data.reset_index(inplace=True)
```

### **4. Fetch GameStop Stock Data**  
Similarly, the script retrieves **GameStopâs** stock data:  

```python
GME = yf.Ticker("GME")
gme_data = GME.history(period="max")
gme_data.reset_index(inplace=True)
```

### **5. Scrape Revenue Data**  
Revenue data is extracted from an online source using **web scraping**:  

```python
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
# Extract revenue data from HTML tables
```

The same method is used for **GameStop revenue data**.  

### **6. Generate and Display Interactive Graphs**  
After fetching and processing the data, the script calls `make_graph()` to display the stock price and revenue trends for both **TSLA** and **GME**:  

```python
make_graph(tesla_data, tesla_revenue, "Tesla Stock & Revenue")
make_graph(gme_data, gme_revenue, "GameStop Stock & Revenue")
```

---

## **Usage**  
1. Run the script using:  

```sh
python TSLA_GME-SHARE PRICE_REVENUE.py
```

2. Interactive graphs will be displayed in your browser.  

---

## **Potential Improvements**  
- Automate revenue data extraction using an API instead of web scraping.  
- Add **real-time** stock price updates.  
- Implement **data storage** using a database for historical analysis.  

---

## **Contributors**  
- **[Fredinard Ohene-Addo]**  

---

## **License**  
This project is open-source under the **MIT License**. 
