from bs4 import BeautifulSoup
import requests

def horizontal_line():
    print("-"*50)

url = "https://www.newegg.com/p/2SN-0001-01A25?cm_sp=SH-_-1005515-_-8-_-2-_-9SIAB6HD4U9475-_-macbook+pro-_-macbook-_-1&Item=9SIAB6HD4U9475"

# getting the html document
result = requests.get(url)
html_document = BeautifulSoup(result.text, "html.parser")
# print(html_document)
# horizontal_line()

# make it look nicer.
# print(html_document.prettify())
# horizontal_line()

# want to get the prices

# we can search for the currency text
prices = html_document.find_all(text="$")
print(prices)

# as a result we found the dollar sign ir repeated five time so we need to know which one represents our price
for price in prices:
    print(price.parent)
horizontal_line()

# we found that the second price in the list is our target
target_price = prices[1].parent
print(target_price)
horizontal_line()

# but we do want to get the price number and from the html element parent we can see the number is located between
# strong tag:
target_price_tag = target_price.find("strong")
print(target_price_tag)
horizontal_line()

# Finally, our price:
price_of_product = target_price_tag.text
print(price_of_product)
horizontal_line()
