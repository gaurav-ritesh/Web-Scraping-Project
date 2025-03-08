# Web Scraping Project

## Overview
This project is a **Python-based web scraper** designed to extract product details from e-commerce websites using `BeautifulSoup` and `Requests`. The scraped data is saved in a CSV file for further analysis and insights.

## Features
1. **Efficient Data Extraction** – Scrapes product **title, price, and link** from an e-commerce site.
2. **CSV Storage** – Saves extracted data in a structured CSV format.
3. **User-Agent Handling** – Avoids basic bot detection by sending appropriate headers.
4. **Scalability** – Supports future enhancements like pagination and multiple site scraping.
5. **Automation Potential** – Can be scheduled for periodic data collection for price tracking.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with the required dependencies.
```sh
pip install requests beautifulsoup4
```

## Usage
1. Clone this repository:
```sh
git clone https://github.com/your-username/web-scraping-project.git
cd web-scraping-project
```
2. Edit the `url` variable inside `scraper.py` with the target website.
3. Run the script:
```sh
python scraper.py
```
4. The extracted data will be saved as `products.csv`.

## Contributing
Feel free to fork the repo and submit pull requests for improvements!

## License
This project is licensed under the **MIT License**.
