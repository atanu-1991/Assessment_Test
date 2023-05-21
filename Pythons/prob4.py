# Question 4 -
# Write a program to download the data from the link given below and then read the data and convert the into
# the proper structure and return it as a CSV file.

# Link - https://data.nasa.gov/resource/y77d-th95.json

# Note - Write code comments wherever needed for code understanding.

# Excepted Output Data Attributes
# ● Name of Earth Meteorite - string 
# ● id - ID of Earth Meteorite - int 
# ● nametype - string 
# ● recclass - string
# ● mass - Mass of Earth Meteorite - float 
# ● year - Year at which Earth Meteorite was hit - datetime format 
# ● reclat - float 
# ● recclong - float
# ● point coordinates - list of in

import pandas as pd
import requests

def download_data(url):
    '''
    This function download the json data from the url
    '''
    response = requests.get(url)
    data = response.json()
    return data


def convert_into_csv(data):
    '''
    This function converts the data from json to csv format and will save it
    '''

    # creating list of every field
    names = []
    ids = []
    nametypes = []
    recclass = []
    masses = []
    years = []
    reclats = []
    reclongs = []
    coordinates = []

    for meteorite in data:
        names.append(meteorite.get('name', None))
        ids.append(meteorite.get('id', None))
        nametypes.append(meteorite.get('nametype', None))
        recclass.append(meteorite.get('recclass', None))
        masses.append(meteorite.get('mass', None))
        years.append(meteorite.get('year', None))
        reclats.append(meteorite.get('reclat', None))
        reclongs.append(meteorite.get('reclong', None))
        if meteorite.get('geolocation', None) is not None:
            coordinates.append(meteorite['geolocation'].get('coordinates', None))
        else:
            coordinates.append(None)


    data_dict = {
        'name' : names,
        'id' : ids,
        'nametype' : nametypes,
        'recclass' : recclass,
        'mass' : masses,
        'year' : years,
        'reclat' : reclats,
        'reclong' : reclongs,
        'coordinates' : coordinates
    }

    # print(data_dict)
    df = pd.DataFrame(data_dict)

    df.to_csv("meteorite_data.csv",index=False)

    print("Data Exported Successfully")


if __name__ == "__main__":
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    data = download_data(url)
    convert_into_csv(data=data)