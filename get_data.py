import requests
from bs4 import BeautifulSoup
import regex as re

def deg_to_dms(deg, pretty_print=None, ndp=4):
    m, s = divmod(abs(deg)*3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)

    if pretty_print:
        if pretty_print=='latitude':
            hemi = 'N' if d>=0 else 'S'
        elif pretty_print=='longitude':
            hemi = 'E' if d>=0 else 'W'
        else:
            hemi = '?'
        return "{d:d}° {m:d}' {s:.{ndp:d}f}'' {hemi:1s}".format(
                    d=abs(d), m=m, s=s, hemi=hemi, ndp=ndp)
    return d, m, s

# url = "agra/urban-deck-sanjay-place-central-agra-65790"
# url = "agra/wonder-terrace-bar-kitchen-tajganj-east-agra-65115"
# url = "agra/hi-fi-cafe-shahganj-west-agra-86534"
# url = "agra/new-pizza-king-dayal-bagh-north-agra-106277"
# url = "agra/the-taste-of-india-tajganj-east-agra-65604"
# url  = "agra/sea-view-restaurant-civil-lines-north-agra-67133"
# # url = "agra/pavilion-caf-tajganj-east-agra-65068"
# url = "/agra/ashoka-bar-lohamandi-west-agra-65063"
# url = '/agra/mommys-paradise-sikandra-north-agra-66763'
# url = "/delhi/cold-love-ice-cream-connaught-place-central-delhi-103023"

def get_data(url):
    r = requests.get(f"https://www.dineout.co.in/{url}")
    s = BeautifulSoup(r.content,"html.parser")
    title = s.findAll(class_ = "restnt-details_info")[0].findAll("h1")[0].text
    price_for_two= s.findAll(class_ = "restnt-cost")[0].text.split("|")[0].replace(" for 2","")[2:]
    cuisine = [i.text for i in s.findAll(class_ = "restnt-cost")[0].findAll("a")]
    address  = s.findAll(class_ = 'address')[0].text.replace("Address:","")
    try:
        pincode = re.findall("[1-9][0-9]{5}",address)[0]
    except:
        pincode = address[-6:]
    maps = s.findAll(class_= "open-map pull-right")[0].findAll('a')[0].get('href')
    m = maps.split('=')[1].split(',')
    latitude = deg_to_dms(float(m[0]),pretty_print='latitude')
    longitude = deg_to_dms(float(m[1]),pretty_print='longitude') 
    count_reviews,count_votes,rating = [0,0,0]
    if("reviews-count font-bold" in str(r.content)):
        count_reviews = s.findAll(class_= "reviews-count font-bold")[0].text #use regex to extract number
    if("rating-count font-bold" in str(r.content)):
        count_votes  = s.findAll(class_ = "rating-count font-bold")[0].text #use regex to extract number
    rating_class = ["cursor rest-rating rating-5_5","cursor rest-rating rating-4_5", "cursor rest-rating rating-4", "cursor rest-rating rating-1_5","cursor rest-rating rating-3_5","cursor rest-rating rating-2_5",]
    for check in rating_class:
        if(check in str(r.content)):
            rating = s.findAll(class_= check)[0].text
            break
    try:
        facilities = [i.text for i in s.findAll("ul",{'class' : "d-flex facilities"})[0].findAll("li")]
    except:
        facilities = 'Not Found' 
    temp_phone = [i.findAll("p")[0].text for i in s.findAll(class_="rdp-section rdp-need-help")[0].findAll("li")]
    call_us, restaurant_phone = 0, 0
    if(len(temp_phone)>1):
        call_us, restaurant_phone = temp_phone
    else:
        call_us = temp_phone[0]
    menu = [j.get('href') for i in s.findAll(id= "menu")[0].findAll("li") for j in i.findAll('a')]
    label_menu  = [j.get('alt') for i in s.findAll(id= "menu")[0].findAll("li") for j in i.findAll('img')]
    bestselling_item = 0
    if("BESTSELLING ITEMS" in str(r.content)):
        bestselling_item = [i.findAll("p")[0].text for i in s.findAll(class_= "about-info d-flex") if "BESTSELLING" in i.text ][0]
    restaurant_type = "Not Mentioned"
    try:
        restaurant_type = [i.findAll("p")[0].text for i in s.findAll(class_= "about-info d-flex") if "TYPE" in i.text ][0]
    except:
        pass

    data = {"Name" : [title],
            "Price_for_two" : [price_for_two],
            "Cuisines" : [cuisine],
            "Address" : [address],
            "Maps_Link" : [maps],
            "Pincode" : [pincode],
            "latitude": [latitude],
            "longitude" : [longitude],
            "Reviews" : [count_reviews],
            "Votes": [count_votes],
            "Rating": [rating],
            "Facilities": [facilities],
            "Company_Phone": [call_us],
            "Restaurant_Phone": [restaurant_phone],
            "Menu_Links" : [menu],
            "Menu_Labels" : [label_menu],
            "Bestselling_Items": [bestselling_item],
            "Restaurant_Type": [restaurant_type]}
    return(data)

