import requests 
from bs4 import BeautifulSoup
import pickle

def scrape():
    url = "https://www.dineout.co.in/"
    r = requests.get(url)

    soup = BeautifulSoup(r.content,'html.parser')

    cities = [f"{str(i.text).lower()}-restaurants" for i in soup.findAll(class_= '_3LAV0')[0].findAll('li')]
    print(cities)
    data = {i:{} for i in cities}
    print(data)
    for city_pages in cities:
       print(city_pages,end=" ")
       pg =1 
       page_url = f"{url}{city_pages}?p={pg}"
       r = requests.get(page_url)
       while("Food not found" not in r.text):
           page_url = f"{url}{city_pages}?p={pg}"
           r = requests.get(page_url)
           s =  BeautifulSoup(r.content, "html.parser")
           restaurants = s.findAll(class_='restnt-info cursor')
           items = {i.findAll("a")[0].get('href'):i.findAll('a')[0].text for i in restaurants}
           data[city_pages].update(items)
           pg+=1
       print(f"DONE {pg}")
    data_file = open('data.pkl', 'wb')
    pickle.dump(data, data_file)
    data_file.close()

def validate_file():
    file = open('data.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    for i in data:
        print(i,"\t",len(data[i]))


if __name__ == "__main__":
    scrape()
