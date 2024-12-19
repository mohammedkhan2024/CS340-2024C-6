#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Passw0rd123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32802
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            # Use MongoDB's insert_one() method to insert the data into the collection
            self.database.animals.insert_one(data)  # data should be dictionary
            return True # Return True to indicate successful insertion       
        else:
            # Raise an exception if the provided data is None or empty
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create method to implement the R in CRUD.

    def read(self, query):
        if query is not None:
            # Use MongoDB's find() method to fetch data matching the query
            data = self.collection.find(query)
            return list(data) # Convert the MongoDB data to a list and return it
        else:
            # If no query is provided, fetch all data from the collection
            data = self.collection.find({})
        return list(data) # Convert and return all data as a list
    
#Create method to implement the U in CRUD.

    def update(self, query, new_values):
        if query and new_values:
            # Perform the update operation.
            result = self.collection.update_many(query, new_values)
            # Return the count of modified documents.
            return result.modified_count
        else:
            # Raise an error if parameters are invalid.
            raise ValueError("Query and new_values parameters must be non-empty.")
        
# Create method to implement the D in CRUD.

    def delete(self, query):
        if query is not None:
            # Perform the delete operation.
            result = self.collection.delete_many(query)
            # Return the count of deleted documents.
            return result.deleted_count
        else:
            # Raise an error if the query is missing.
            raise ValueError("Query parameter must be non-empty.")

