import requests
from bs4 import BeautifulSoup
from db import get_all_products, save_price
from alert import send_alert
import re

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

def scrape_price(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")

        price_tag = (
            soup.select_one("p.price_color") or
            soup.select_one("span.a-price-whole") or
            soup.select_one(".a-price .a-offscreen") or
            soup.select_one("#priceblock_ourprice") or
            soup.select_one(".a-color-price")
        )

        if price_tag:
            price_text = price_tag.get_text()
            price_text = price_text.replace(",", "").replace("₹", "").replace("£", "").replace("$", "").strip()
            numbers = re.findall(r'\d+\.?\d*', price_text)
            if numbers:
                return float(numbers[0])

        print("Price tag not found.")
        return None

    except Exception as e:
        print(f"Error scraping: {e}")
        return None

def run_tracker():
    print("\n--- Running Price Tracker ---")
    products = get_all_products()

    if not products:
        print("No products found in database.")
        return

    for product in products:
        print(f"\nChecking: {product['product_name']}")
        price = scrape_price(product["url"])

        if price:
            print(f"Current Price: {price} | Target: {product['target_price']}")
            save_price(product["id"], price)

            if price <= float(product["target_price"]):
                print("Price dropped! Sending alert...")
                send_alert(
                    product["product_name"],
                    price,
                    product["target_price"],
                    product["url"]
                )
            else:
                print("Price is above target. No alert needed.")
        else:
            print(f"Could not fetch price for {product['product_name']}")

if __name__ == "__main__":
    run_tracker()