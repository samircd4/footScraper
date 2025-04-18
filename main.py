import requests
from rich import print
import pandas as pd


def get_products(page_number=0):
    url = "https://www.footlocker.com/zgw/search-core/products/v3/search"

    # Query parameters for filtering and pagination
    querystring = {
        "query": "::collection_id:discount-eligible",
        "q": "greatdeals",
        "currentPage": page_number,
        "sort": "relevance",
        "pageSize": "200",
        "pageType": "browse",
        "timestamp": "4"
    }

    payload = ""

    # Headers to simulate a real browser session (some security and tracking info)
    headers = {
        "cookie": "...",  # (truncated for readability)
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        "x-api-lang": "en-US",
        "x-fl-request-id": "1c5cb050-1b9c-11f0-b86f-5552691e3306"
        # ... other headers omitted for brevity
    }

    # Initial request to get pagination info
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = response.json()
    pagination = data.get('pagination')
    total_page = pagination.get('totalPages')
    current_page = pagination.get('currentPage')

    all_products = []

    while True:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        data = response.json()
        products = data.get('products')

        for product in products:
            base_product = product.get('baseProduct')
            title = product.get('name')
            price = product.get('price').get('value')
            link = f'https://www.footlocker.com/product/~/{base_product}.html'
            is_discounted = product.get('badges').get('isDiscountsExcluded')

            data = {
                'title': title,
                'price': price,
                'base_product': base_product,
                'is_discounted': is_discounted,
                'link': link
            }

            print(data)
            all_products.append(data)

        # Go to next page
        current_page += 1
        querystring['currentPage'] = current_page

        print(current_page, total_page)
        if current_page == total_page:
            break

    return all_products


if __name__ == "__main__":
    all_products = get_products()
    
    df = pd.DataFrame(all_products)
    df.to_csv('products.csv', index=False)
