import pandas as pandas
import pymongo as pymongo
 
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')
posts = client.testdb

post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))