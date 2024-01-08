import requests
from tkinter import *
from PIL import ImageTk, Image
import io


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
image_response = requests.get(pokemon)

window = Tk()
window.title("Pokemon")
window.minsize(width=200, height=100)

image = Image.open(io.BytesIO(image_response.content))
photo = ImageTk.PhotoImage(image)

label = Label(window, image=photo)
label.pack()

label2 = Label(text=user_input)
label2.pack()

window.mainloop()



