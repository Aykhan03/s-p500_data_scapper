# s-p500-excel

# S&P 500 Company Data Scraper

## Introduction
This Python script collects data on S&P 500 companies, extracts specific information, and stores it in an Excel file. It navigates through various financial websites to gather real-time data on these companies.

## Technologies
- Python 
- Selenium
- BeautifulSoup
- Pandas
- ChromeDriver

## Setup
To run this project, install it locally using pip:

pip install selenium bs4 pandas openpyxl chromedriver_autoinstaller requests webdriver_manager


## How to Use
Run the script using Python. The script will automatically open the necessary websites, scrape data, and store it in an Excel file named `stock.xlsx`.

## Features
- Real-time data collection on S&P 500 companies
- Data extraction includes company name, ticker symbol, sector, current value, and more
- Output in a well-formatted Excel file
