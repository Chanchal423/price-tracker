# E-Commerce Price Tracker

A Python tool that automatically tracks product prices and sends email alerts when prices drop below the target price.

## Features
- Scrapes product prices using BeautifulSoup and Requests
- Stores price history in MySQL database
- Sends email alerts when price drops below target
- Runs automatically every 6 hours using scheduler

## Tech Stack
- Python
- BeautifulSoup, Requests
- MySQL, mysql-connector-python
- smtplib for email alerts
- schedule library for automation

## How to Run
1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Set up .env file with your credentials
4. Run: python tracker.py
