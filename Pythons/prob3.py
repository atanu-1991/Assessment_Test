# Question 3: -
# Write a program, which would download the data from the provided link, and then read the data and convert
# that into properly structured data and return it in Excel format.

# Note - Write comments wherever necessary explaining the code written.

# Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json

# Data Attributes - 
# ● id: Identification Number - int 
# ● num: Number of the Pokémon in the official Pokédex - int 
# ● name: Pokémon name - string 
# ● img: URL to an image of this Pokémon - string 
# ● type: Pokémon type -string 
# ● height: Pokémon height - float
# ● weight: Pokémon weight - float 
# ● candy: type of candy used to evolve Pokémon or given when transferred - string 
# ● candy_count: the amount of candies required to evolve- int
# ● egg: Number of kilometers to travel to hatch the egg - float 
# ● spawn_chance: Percentage of spawn chance (NEW) - float 
# ● avg_spawns: Number of this pokemon on 10.000 spawns (NEW) - int
# ● spawn_time: Spawns most active at the time on this field. Spawn times are the same for all time zones and are expressed in local time. (NEW) - “minutes: seconds” 
# ● multipliers: Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int
# ● weakness: Types of Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of
# successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous
# evolutions of Pokémon - - list of dict



import pandas as pd
import requests


def download_data(url):
    '''
    This function download the json data from the url
    '''
    response = requests.get(url)
    data = response.json()
    return data


def convert_into_excel(data):
    '''
    This function converts the data from json to excel format and will save it
    '''
    # Extract the 'pokemon' field from the data
    pokemon_data = data['pokemon']

    # creating list for every filed
    id = []
    num = []
    name = []
    img = []
    type = []
    height = []
    weight = []
    candy = []
    candy_count = []
    egg = []
    spawn_chance = []
    avg_spawns = []
    spawn_time = []
    multipliers = []
    weaknesses = []
    next_evolution = []
    prev_evolution = []

    # Iterate over each pokemon in the data and extract the attributes
    for pokemon in pokemon_data:
        id.append(pokemon['id'])
        num.append(pokemon['num'])
        name.append(pokemon['name'])
        img.append(pokemon['img'])
        type.append(pokemon['type'])
        height.append(pokemon['height'])
        weight.append(pokemon['weight'])
        candy.append(pokemon['candy'])
        candy_count.append(pokemon.get('candy_count', None))
        egg.append(pokemon.get('egg', None))
        spawn_chance.append(pokemon.get('spawn_chance', None))
        avg_spawns.append(pokemon.get('avg_spawns', None))
        spawn_time.append(pokemon.get('spawn_time', None))
        multipliers.append(pokemon.get('multipliers', None))
        weaknesses.append(pokemon.get('weaknesses', None))
        next_evolution.append(pokemon.get('next_evolution', None))
        prev_evolution.append(pokemon.get('prev_evolution', None))
       

    # Store data in dictionary format
    pokemon_dict = {
        'id' : id,
        'num' : num,
        'name' : name,
        'img' : img,
        'type' : type,
        'height' : height,
        'weight' : weight,
        'candy' : candy,
        'candy_count' : candy_count,
        'egg' : egg,
        'spawn_chance' : spawn_chance,
        'avg_spawns' : avg_spawns,
        'spawn_time' : spawn_time,
        'multipliers' : multipliers,
        'weaknesses' : weaknesses,
        'next_evolution' : next_evolution,
        'prev_evolution' : prev_evolution
    }


    # Converting data from dictionary to pandas dataframe
    df = pd.DataFrame(pokemon_dict)

    # Store the pandas data frame into excel format
    df.to_excel("pokemon_data.xlsx",index=False)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    data = download_data(url=url)
    convert_into_excel(data=data)
