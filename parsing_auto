import requests, re
from bs4 import BeautifulSoup
import pandas as pd

def getting_page_numbers(url):
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    pages = len([i.text for i in soup.findAll('a', {'class' : 'ListingPagination-module__page'})])
    return pages

def getting_data(url, pages):
    all_prices = []
    all_years = []
    all_mileages = []
    for page in range(pages + 1):
        resp = requests.get(f'{url}?page={page}') #, {'http' : 'http://' + ip_port, 'User-Agent' : useragent})

        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        prices = [int(''.join(re.findall('\d+', price.text))) for price in soup.findAll('div', {'class' : 'ListingItem-module__columnCellPrice'})]

        years = [int(year.text) for year in soup.findAll('div', {'class' : 'ListingItem-module__year'})]

        temp_mileages = [''.join(re.findall('\d+', mileage.text)) for mileage in soup.findAll('div', {'class' : 'ListingItem-module__kmAge'})]
        mileages = [0 if miles == '' else int(miles) for miles in temp_mileages]

        all_prices.extend(prices)
        all_years.extend(years)
        all_mileages.extend(mileages)

        
    bikes = pd.DataFrame({
    'price' : all_prices,
    'year' : all_years,
    'mileage' : all_mileages
    })

    bikes = bikes.query(' mileage < 5')
    bike_prices = bikes.groupby('year', as_index = False).agg({'price' : 'mean'}).sort_values('year', ascending = False).astype(int)

    
    return bike_prices

def main():
    auto_url = 'https://auto.ru/krasnogorsk/motorcycle/bmw/g_310_gs/all/'
    page_numbers = getting_page_numbers(auto_url)
    data_df = getting_data(auto_url, page_numbers)
    
    return data_df
    
moto_prices = main()    
    
if __name__=='__main__':
    print(moto_prices)
