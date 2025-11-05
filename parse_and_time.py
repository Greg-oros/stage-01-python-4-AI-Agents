# parser gets data from wikipedia page: Climate change, saves to json file and shows response time
# requests – a library that allows you to send HTTP requests (e.g., download data from the internet)
# BeautifulSoup – a tool for "cleaning" HTML code and converting it to readable text:

import requests
from bs4 import BeautifulSoup



# This is the Wikipedia API address (Action API).
# I don't fetch the page like a regular website – I just ask the API for data:

url = "https://en.wikipedia.org/w/api.php"

#These are the query parameters (i.e., "what I want from the API"):
#action: parse tell Wikipedia: prepare the page for reading
#page: Climate change name of the article we want to retrieve
#prop: text retrieve the article content (without infoboxes, history, etc.)
#format: json the response should be in JSON format (i.e., in Python → dictionary):

params = {
    "action": "parse",
    "page": "Climate change",
    "prop": "text",
    "format": "json"
}



# I add User-Agent, because I am not bot:

headers = {
    "User-Agent": "My_first_application (g.olczyk@yahoo.com)"
}

# Sending an HTTP GET request to the API
# params automatically create a query like this:
# https://en.wikipedia.org/w/api.php?action=parse&page=Climate+change&prop=text&format=json
# Headers prevent blocking from wiki:

response = requests.get(url, params=params, headers=headers)

# showing connection status in case of problems
#200 means: everything is OK
#404 – not found
# 429 – too many queries → Wikipedia is blocking me:

print("Status:", response.status_code)

# I convert the response to a dictionary.
# Now I can refer to the data as a dict:

data = response.json()

# After sending the requests.get(url, params=params, headers=headers) request, the response object contains various data about the server's response, including:
# status_code: status code (200 = OK, 404 = page not found, etc.)
# headers: response headers
# content: retrieved data
# elapsed: server response time
# response.elapsed is the duration of the request, using a timedelta object.
# To convert this time to a number in seconds, I use: response.elapsed.total_seconds():

print("Response time:", response.elapsed.total_seconds(), "seconds")



# Wikipedia returned the article as HTML, not plain text.
# Here I enter the dictionary structure:
# data["parse"] → part of the response with article details
# ["text"] → article content
# ["*"] → article HTML itself
# After this line, the HTML is a long text with HTML tags:

html = data["parse"]["text"]["*"]

# BeautifulSoup cleans up HTML and converts it to plain text.
# get_text() removes all <tags> and leaves only the content:

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

# I am only displaying the first 500 characters to check if everything is working.
# I am not showing the whole thing because it's very long:

print(text[:500])

# We open a text file for writing.
# encoding="utf-8" allows me to correctly save Polish letters.
# write(text) saves the entire article to a file:

with open("Climate_change.txt", "w", encoding="utf-8") as f:
    f.write(text)

#Information for me that the operation was successful

print("\n Article saved to file: Climate_change.txt")

# import json library:

import json

# making dictionary:

article_json = {
    "title": "Climate change",
    "text": text
}

# Saving text to JSON file and
# json.dump(article_json, f, ensure_ascii=False, indent=4)
# json.dump() — Writes data to a file in JSON format.
# article_json — The data we're writing (our dictionary).
# f — The file we're writing to.
# ensure_ascii=False — Allows writing normal characters (doesn't convert Polish letters to \u0142).
# indent=4 — Formats the file nicely (indents the JSON by 4 spaces to make it readable):

with open("Climate_change.json", "w", encoding="utf-8") as f:
    json.dump(article_json, f, ensure_ascii=False, indent=4)

print("\n Article saved to JSON file: Climate_change.json")
