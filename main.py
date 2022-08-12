from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl.workbook import Workbook
import pandas as pd

url = 'https://www.scrapethissite.com/pages/simple/'
path = "YOUR PATH TO CHROMEDRIVER"
driver = webdriver.Chrome(path)
driver.get(url)

#GET COUNTRIES
countries = driver.find_elements(By.CSS_SELECTOR,'#countries > div > div > div:nth-child(1) > h3')
countries_list = []
for country in countries:
    c = country.text
    countries_list.append(c)

#GET CAPITOLS
capital_pull = driver.find_elements(By.CSS_SELECTOR, '#countries > div > div > div:nth-child(1) > div > span.country-capital')
capitals = []
for capital in capital_pull:
    cap = capital.text
    capitals.append(cap)

#GET POPULATION
population_pull = driver.find_elements(By.CSS_SELECTOR, '#countries > div > div > div:nth-child(1) > div > span.country-population')
populations = []
for population in population_pull:
    pop = population.text
    populations.append(pop)

#GET AREA
area_pull = driver.find_elements(By.CSS_SELECTOR,'#countries > div > div > div:nth-child(1) > div > span.country-area')
areas = []
for area in area_pull:
    a = area.text
    areas.append(a)


df = pd.DataFrame(index=None)
df['Country'] = countries_list
df['Capital'] = capitals
df['Population'] = populations
df['Area'] = areas

df.set_index('Country', inplace=True)

driver.close()

with pd.ExcelWriter("countries.xlsx") as writer:
    df.to_excel(writer)
