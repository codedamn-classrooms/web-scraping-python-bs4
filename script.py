import requests from bs4 import BeautifulSoup
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as empty list

# Set all_h1_tags to all h1 tags of the soup

# Create seventh_p_text and set it to 7th p element text of the page
