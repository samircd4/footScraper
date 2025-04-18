# FootScraper

**FootScraper** is a Python script that scrapes discounted product data from [Footlocker](https://www.footlocker.com), including product names, prices, discount status, and links. Results are saved to a CSV file for easy access and analysis.

## Features

- Scrapes up to 200 products per page
- Filters for discount-eligible items
- Automatically navigates through all pages
- Logs progress and errors to both console and `product_scraper.log`
- Outputs data to `products.csv`

## Requirements

- Python 3.7+
- `requests`
- `pandas`

You can install the required packages with:

```bash
pip install requests pandas
