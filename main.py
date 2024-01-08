import requests
from tkinter import *


def get_pokemon_data():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    if response.status_code == 200:
        return response.json().get("results")

user_input = input("Enter Pokemon: ").lower()
def get_pokemon_url(user_input):
    pokemon_response = get_pokemon_data()
    for pokemon in pokemon_response:
        if pokemon["name"] == user_input:
            return pokemon["url"]

pokemon_url = get_pokemon_url(user_input)
pokemon_details = requests.get(pokemon_url)
pokemon = pokemon_details.json().get("sprites").get("front_default")
print(pokemon)

window = Tk()
window.title(user_input.upper())

window.mainloop()



