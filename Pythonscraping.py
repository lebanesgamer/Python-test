import requests
from bs4 import BeautifulSoup

# URL of a coupon website
url = 'https://www.coupons.com/coupon-codes/amazon/'

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the coupon codes on the page
coupon_codes = soup.find_all(class_='code')

# Print the coupon codes
for coupon in coupon_codes:
    print(coupon.text)
