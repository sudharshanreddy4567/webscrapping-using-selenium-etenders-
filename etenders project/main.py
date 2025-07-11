import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select

chromeoptions=Options()
driver=webdriver.Chrome(options=chromeoptions)

url="https://etender.cpwd.gov.in/"
driver.get(url)
driver.maximize_window()
time.sleep(4)
try:
    at=driver.switch_to.alert
    at.accept()
    time.sleep(4)
except NoAlertPresentException:
    print("THere isno alert persent")

tenders=driver.find_element(By.LINK_TEXT,"New Tenders")
tenders.click()
time.sleep(4)
alltabs=driver.find_element(By.LINK_TEXT,"All")
alltabs.click()
time.sleep(4)
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)
dp=Select(driver.find_element(By.NAME,'example_length'))
dp.select_by_visible_text("20")
time.sleep(4)
rows=driver.find_elements(By.XPATH,'//table[contains(@class, "table")]/tbody/tr')
data1=[]
for i in rows[:20]:
    col=i.find_elements(By.TAG_NAME,'td')
    if len(col) >=6:
        data={
            "NIT/RFP NO":col[0].text.strip(),
            "Name of Work / Subwork / Packages":col[1].text.strip(),
            "Estimated Cost":col[2].text.strip(),
            "Bid Submission Closing Date & Time":col[3].text.strip(),
            "EMD Amount": col[4].text.strip(),
            "Bid Opening Date & Time":col[5].text.strip(),
        }
        data1.append(data)

driver.quit()

csv_cols = {
    "NIT/RFP NO": "ref_no",
    "Name of Work / Subwork / Packages": "title",
    "Estimated Cost": "tender_value",
    "Bid Submission Closing Date & Time": "bid_submission_end_date",
    "EMD Amount": "emd",
    "Bid Opening Date & Time": "bid_open_date"
}
with open("20tenderslist.csv",mode="w",newline="",encoding="utf-8") as csvfile:
    wi=csv.DictWriter(csvfile,fieldnames=csv_cols.values())
    wi.writeheader()
    for row in data1:
        wi.writerow({csv_cols[k]:v for k,v in row.items()})
# print(data1)
