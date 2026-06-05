import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def save_price(product_id, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO price_history (product_id, price) VALUES (%s, %s)",
        (product_id, price)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Price Rs.{price} saved to database.")

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products