# Question 5 -
# Write a program to download the data from the given API link and then extract the following data with
# proper formatting

# Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes

# Note - Write proper code comments wherever needed for the code understanding

# Excepted Output Data Attributes -
# ● id - int 
# ● url - string
# ● name - string 
# ● season- int 
# ● number - int
# ● type - string 
# ● airdate -date format 
# ● airtime -12-hour time format
# ● runtime - float
# ● average rating - float
# ● summary - string
# ● without html tags
# ● medium image link - string
# ● Original image link - string

import json
from bs4 import BeautifulSoup
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
    # Extracting shows information
    shows_data = data.get('_embedded',{}).get('episodes',[])

    # Creating list for every features
    episode_id = []
    episode_url = []
    episode_name = []
    episode_season = []
    episode_number = []
    episode_type = []
    episode_airdate = []
    episode_airtime = []
    episode_airstamp = []
    episode_runtime = []
    episode_rating = []
    episode_summary = []
    episode_medium_image = []
    episode_original_image = []

    for episode in shows_data:
        episode_id.append(episode.get('id', None))
        episode_url.append(episode.get('url', None))
        episode_name.append(episode.get('name', None))
        episode_season.append(episode.get('season', None))
        episode_number.append(episode.get('number', None))
        episode_type.append(episode.get('type', None))
        episode_airdate.append(episode.get('airdate', None))
        episode_airtime.append(episode.get('airtime', None))
        episode_airstamp.append(episode.get('airstamp', None))
        episode_runtime.append(episode.get('runtime', None))
        episode_rating.append(episode.get('rating',{}).get('average', None))

        summary_html = episode.get('summary', None)
        if summary_html:
            bs = BeautifulSoup(summary_html, 'html.parser')
            summary = bs.get_text()
        else:
            summary = None
        episode_summary.append(summary)

        episode_medium_image.append(episode.get('image',{}).get('medium', None))
        episode_original_image.append(episode.get('image',{}).get('original', None))


    episode_dict = {
        'id' : episode_id,
        'url' : episode_url,
        'name' : episode_name,
        'season' : episode_season,
        'number' : episode_number,
        'type' : episode_type,
        'airdate' : episode_airdate,
        'airtime' : episode_airtime,
        'airstamp' : episode_airstamp,
        'runtime' : episode_runtime,
        'rating' : episode_rating,
        'summary' : episode_summary,
        'medium_image' : episode_medium_image,
        'original_image' : episode_original_image
    }

    df = pd.DataFrame(episode_dict)

    df.to_csv('episode.csv', index=False)
    print("Data Exported Successfully!!")


if __name__ == "__main__":
    url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
    data = download_data(url)
    convert_into_csv(data=data)

