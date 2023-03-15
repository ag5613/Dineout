# Dineout.co.in web scraping

This project is a web scraping project that extracts restaurant data from dineout.co.in, a popular online restaurant booking platform. The project is implemented using Python and the BeautifulSoup library for web scraping.


## Project Structure

The project is organized as follows:

- 'get_data.py': Python script that contains the web scraping code for the specific restaurant.
- 'get_links.py' : Python script that contains the web scraping code to scrape all the links of all the resturants.
- 'requirements.txt' : File that lists the dependencies required to run the project.

## Installation
To install the project dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

First you need to get scrape links of all the restaurants of all the cities, to do so  execute the following command:

```
python get_links.py
```

After getting the links you can scrape the details by executing the following command :

```
python get_data.py
```

The scraper will extract the following information from dineout.co.in:

    Name
    Price_for_two
    Cuisines
    Address
    Maps_Link
    Pincode
    latitude
    longitude
    Reviews
    Votes
    Rating
    Facilities
    Company_Phone
    Restaurant_Phone
    Menu_Links
    Menu_Labels
    Bestselling_Items
    Restaurant_Type