import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

# Function to get request from Ebay
def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print("Server responded with:", response.status_code)
    else:
      # Note: first argument is the html code which is response.text
      # second argument is a parser that will parse html code
      soup = BeautifulSoup(response.text, 'lxml')
    return soup;


# Function to scrape needed data
def get_detailed_data(soup):

    #item
    #price
    #items sold
    try:
        t = soup.find("h1", {"id": 'itemTitle'})
        title =t.text[16::]

    except:
        title = ""

    try:
        p = soup.find("span", {"id": 'prcIsum_bidPrice'})
        if p is None:
            p = soup.find("span", {"id": 'prcIsum'})
        currency, price =  p.text.split(" ")
    except:
        price = ""
        currency = ""

    data = {
        "title": title,
        "price" :price,
        "currency": currency
    }
    return data

def get_index_data(soup):
    try:
        links = soup.find_all("a", {"class" :'s-item__link'})
    except:
        links = []

    urls = [item.get('href') for item in links]

    # print(links[0].get('href'))
    return urls[1:len(urls)]


# Main function will manage collection to collect script data
def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=shiny+charizard+gx&_pgn=2'
    products = get_index_data(get_page(url))

    for links in products:
        get_detailed_data(get_page(links))









# If file is running directly from console the file name attribute will be '__main__'
# If being imported into another script. Name attribute will contain the file. In this case ebay_scarpe.py
if __name__ == '__main__':
    main()
