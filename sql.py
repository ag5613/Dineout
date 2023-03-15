import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='dineout')
table = "CREATE TABLE data ('Name' VARCHAR(20), 'Price for two' VARCHAR(20), 'Cuisines' ENUM, 'Address' TEXT, 'Link to map' TEXT, 'Reviews' TEXT, 'Votes' TEXT, 'Rating' TEXT, 'Facilities'ENUM, 'Company Phone' TEXT, 'Restaurant Phone' TEXT, 'Menu Links' ENUM, 'Menu Labels' ENUM, 'Bestselling Items' TEXT, 'Restaurant Type' TEXT"
cursor = cnx.cursor()
cursor.execute(table)     