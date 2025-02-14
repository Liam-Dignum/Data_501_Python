import requests
import requests_cache

base_url = 'https://pokeapi.co/api/v2/'

requests_cache.install_cache('poke_cache')
#r = requests.get(base_url + 'pokedex/2')
#r_json = r.json()
#print(r_json['pokemon_entries'])
r = requests.get(base_url + 'pokemon/1')
r_json = r.json()
print(r_json['stats'])