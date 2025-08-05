import requests
from bs4 import BeautifulSoup
import gspread
from google.oauth2.service_account import Credentials

url = 'https://www.hellojob.az/vakansiya/korporativ-satis-uzre-mutexessis-4010704'
headers = {'User-Agent': 'Mozilla/5.0'}

# Google Sheets-ə giriş
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file(
    r'C:\Users\UniSoft PC\Downloads\hybrid-task-467419-b1-b3450705adea.json',
    scopes=scopes
)

gc = gspread.authorize(creds)
sheet = gc.open('job hunting').sheet1
sheet.update(values=[['Vəzifə', 'Şirkət', 'Link', 'Bitmə Tarixi']], range_name='A1:D1')


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

title_tag = soup.find('h1', class_='section-title')
title = title_tag.get_text(strip=True) if title_tag else 'Tapılmadı'

company_tag = soup.find('a', class_='vacancies__category text-black')
company = company_tag.get_text(strip=True) if company_tag else 'Tapılmadı'

deadline = 'Tapılmadı'
ul_tag = soup.find('ul', class_='company__item__details')
if ul_tag:
    li_tags = ul_tag.find_all('li')
    for li in li_tags:
        span = li.find('span')
        if span and 'Bitmə tarixi' in span.text:
            p = li.find('p')
            if p:
                deadline = p.get_text(strip=True)
                break

sheet.append_row([title, company, url, deadline])





