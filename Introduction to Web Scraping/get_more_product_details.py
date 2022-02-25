import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup


def horizontal_line():
    print("-" * 50)


URL = ('https://www.amazon.eg/-/en/Apple-Macbook-13-Inch-8-core-7-core/dp/B08N5VXMK6/ref=sr_1_1?crid=3LJB737JSL61Y'
       '&keywords=macbook&qid=1645812093&sprefix=macboo%2Caps%2C316&sr=8-1')

# user agent = browser information (get via google search "my user agent")
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.102 Safari/537.36'}

page = requests.get(URL, headers=headers)

html_document = BeautifulSoup(page.content, 'html.parser')

# get the product name
title_element = html_document.find(id="productTitle")
title_text = title_element.text
# print(title_text)

# get the product price
price_element = html_document.find(class_="a-price-whole")
price_as_a_whole = price_element.text
# print(price_as_a_whole)

# get the image of the product
div_containing_img = html_document.find_all(id="imgTagWrapperId")[0]
img_element = div_containing_img.find("img")
img_src = img_element['src']
# print(img_src)

# then downloading the image using the source link
response = requests.get(img_src)
img = open("./product_images/" + title_text+".png", "wb")
img.write(response.content)
img.close()

# saving the data in csv
data_dictionary = {"product_name": title_text, "product_price": price_as_a_whole}
data_items = data_dictionary.items()
data_list = list(data_items)
data_frame = pd.DataFrame(data_list)
data_frame.to_csv('./products_data/product_data.csv', encoding='utf-8', index=False, header=None)