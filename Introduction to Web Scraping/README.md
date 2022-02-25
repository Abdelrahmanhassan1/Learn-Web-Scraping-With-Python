# An Introduction to web scraping using beautiful soup module.
<hr>

## The First part to scrap from local files.
<hr>
<p style="font-size: 1rem">First, install the package:</p>

> pip install beautifulsoup4

<p style="font-size: 1rem">Then import the package in your python file:</p>

> from bs4 import beautifulsoup

<p style="font-size: 1rem">The methods covered in this section:</p>

1. html_document.title. <br>
to find the title tag 
2. html_document.title.string. <br>
to find the title tag text 
3. html_document.find(). <br>
to find a specific html element and return the first element found
4. html_document.find_all() <br>
to find a specific html element and return all elements found in an array

<hr>

## Second part is to scrap from online pages.

<hr>

<p style="font-size: 1rem">First, install requests package:</p>

> pip install requests

<p style="font-size: 1rem">The methods covered in this section:</p>

1. requests.get(url) <br>
pass the url you want to get its content
2. html_document.prettify() <br>
To make the content looks more nicer and clean
3. text.parent
returns the html element that contains a specific text