import requests
from bs4 import BeautifulSoup
import csv

def scrape_ecommerce(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    
    for item in soup.find_all('div', class_='product-item'):
        title = item.find('h2', class_='product-title').text.strip()
        price = item.find('span', class_='price').text.strip()
        link = item.find('a', class_='product-link')['href']
        
        products.append([title, price, link])
    
    save_to_csv(products)

def save_to_csv(data, filename='products.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Link'])
        writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = "https://example.com/products"  # Replace with  site URL
    scrape_ecommerce(url)

"""
### Project Description

1. **Efficient Web Scraping**: Extracts product data (title, price, and link) from e-commerce websites using BeautifulSoup and Requests.
2. **CSV Data Storage**: Saves the scraped product information into a structured CSV file for easy access and analysis.
3. **User-Agent Handling**: Bypasses basic bot detection by sending an appropriate User-Agent header in requests.
4. **Scalability**: Can be expanded to support pagination and multiple e-commerce websites with minor modifications.
5. **Automation Potential**: Easily integrates with automation tools to schedule regular data collection for market research and price tracking.
"""
