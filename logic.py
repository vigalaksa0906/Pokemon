import aiohttp
import random

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.img = None
        self.name = None

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"The name of your Pokémon is: {self.name}"

    async def show_img(self):
        # An asynchronous method to get the name of a Pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request to retrieve Pokémon data
                if response.status == 200:
                    data = await response.json()  # Receiving JSON response
                    img_url = data['sprites']['front_default']  # Retrieving the URL of a Pokémon
                    return img_url  # Returning the image's URL
                else:
                    return None  # Returning None if the request fails