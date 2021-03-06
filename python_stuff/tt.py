import pandas as pandas
import pymongo as pymongo
 
from pymongo import MongoClient

cars = [ {'name': 'Audi', 'price': 52642},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600} ]

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.testdb
    
    db.cars.insert_many(cars)
    with client:
    
      db = client.testdb
      print(db.list_collection_names())
      sql = ("Select * from cars")
      cursora = db.cursora(buffered = True)
      cursora.execute(sql)