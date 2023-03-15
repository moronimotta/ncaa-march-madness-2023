
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def get_teams_names():

    url_teams_names = 'https://www.ncaa.com/march-madness-live/bracket'
    response = requests.get(url_teams_names)
    html = response.content

    
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the team names in the bracket
    team_names = []
    for team in soup.find_all('p', class_='body body_2 color_lvl_-5'):
        team_names.append(team.text)

    # remove all the empty strings from the list
    team_names = list(filter(None, team_names))
    return team_names


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


# Loop through each table and extract the data
    for table in tables:
        # Initialize an empty list to store the data from this table
        table_data = []
        
        # Get the headers of the table (the first row)
        headers = []
        for th in table.find("tr").find_all("th"):
            headers.append(th.text.strip())
        
        # Loop through each row of the table (excluding the first row)
        for tr in table.find_all("tr")[1:]:
            # Initialize an empty dictionary to store the data from this row
            row_data = {}
            
            # Loop through each cell of the row and add the data to the dictionary
            for i, td in enumerate(tr.find_all("td")):
                row_data[headers[i]] = td.text.strip()
            
            # Add the dictionary to the list of data from this table
            table_data.append(row_data)
        
        # Add the list of data from this table to the overall list of data
        data.append(table_data)

    # from the first table, get the data for the first item and join with the first item in the second table and do that for all items in the first table
    for i, item in enumerate(data[0]):
        item.update(data[1][i])

    # Remove the second table from the data
    data.pop(1)

    # Write the data to a JSON file
    with open("basketball_stats.json", "w") as outfile:
        json.dump(data, outfile)

generate_statistics()