#!/usr/bin/python
# ------------------------------------------------------------------------------
# Reuters Launcher
# ------------------------------------------------------------------------------

# Import required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ------------------------------------------------------------------------------
Ticker = raw_input("Ticker: ")
# ------------------------------------------------------------------------------

# Link to the overview page
#Reuters = ("https://www.reuters.com/finance/stocks/overview/")

driver = webdriver.Chrome()

# Link to the profile page
Reuters = ("https://www.reuters.com/finance/stocks/company-profile/")

# Restate the link, appending the ticker symbol
Reuters = Reuters + Ticker

# Locate Reuters company profile page
driver.get(Reuters)