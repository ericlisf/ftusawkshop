import pandas as pd

def load_location(df, connection):
    locations = df[["continent", "country"]].drop_duplicates.reset_index()

def reshape_data():
    pass

def load_facts():

def gapminder_all_etl(connection_string, filepath):
    load_locations()
    reshape_data()
    load_facts()    
