import doctest
from bs4 import BeautifulSoup as bs


def horizontal_line():
    print("-" * 50)


with open("index.html", "r") as file:
    html_document = bs(file, "html.parser")

# get the full document
# print(html_document)

# get the title element of the page
title_element = html_document.title

# get the title text
title_text = title_element.string
print(title_text)
horizontal_line()

# change the title text
title_element.string = "Abdelrahman's Story"
print(html_document)
horizontal_line()

# find specific tag element
# return the first tag element
print(html_document.find("a"))
horizontal_line()

# return all tag elements in an array
print(len(html_document.find_all("a")))
print(html_document.find_all("a"))
horizontal_line()



