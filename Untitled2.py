#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()


# In[2]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()


# In[11]:


data_df=spark.read.format("json").load("file:/home/labuser/Downloads/688b97cc-73ed-4262-b3be-6ef274e26311_83d04ac6-cb74-4a96-a06a-e0d5442aa126_cars.json")
data_df.show()


# In[10]:




