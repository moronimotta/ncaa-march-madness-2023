
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def generate_statistics():

    url = "https://www.espn.com/mens-college-basketball/stats/team/_/season/2023"

    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")


    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    
    # navigate to the web page
    driver.get(url)

    data = []

    while True:
        try:
            
            time.sleep(10)
            # Wait for the ad to close
            WebDriverWait(driver, 15).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "overlayClose"))
            )
            
            # Click on the "show more" button
            show_more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "loadMore__link"))
            )
            show_more_button.click()     
            
        except:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            tables = soup.find_all("table")
            break
            
    driver.quit()


    for table in tables:

        table_data = []
        
        # Get the headers of the table (the first row)
        headers = []
        for th in table.find("tr").find_all("th"):
            headers.append(th.text.strip())
        
        # Loop through each row of the table (excluding the first row)
        for tr in table.find_all("tr")[1:]:
            row_data = {}
            
            for i, td in enumerate(tr.find_all("td")):
                row_data[headers[i]] = td.text.strip()
            
            table_data.append(row_data)
        
        data.append(table_data)

    for i, item in enumerate(data[0]):
        item.update(data[1][i])

    data.pop(1)

    with open("basketball_stats.json", "w") as outfile:
        json.dump(data, outfile)

generate_statistics()
