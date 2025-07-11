# webscrapping-using-selenium-etenders-
# Web Scraping of CPWD e-Tenders using Selenium

This project is a simple Python script that uses **Selenium** to scrape tender data from the official **CPWD eTender Portal** ([https://etender.cpwd.gov.in/](https://etender.cpwd.gov.in/)).

## 🚀 Features

- Opens the CPWD eTender website using Selenium.
- Handles pop-up alerts automatically.
- Navigates to the "New Tenders" section and selects "All" tenders.
- Scrolls down and changes the table view to show 20 tenders.
- Extracts key tender details:
  - NIT/RFP Number
  - Name of Work / Subwork / Packages
  - Estimated Cost
  - Bid Submission Closing Date & Time
  - EMD Amount
  - Bid Opening Date & Time
- Saves the extracted data in a CSV file named `20tenderslist.csv`.

## 🛠 Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- Selenium

## 📦 Install Dependencies

```bash
pip install selenium
