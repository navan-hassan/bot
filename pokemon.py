import requests

def get_pokemon_info(pokemon_name):
	url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
	response = requests.get(url, timeout=10)
	print(response)
	if (response.status_code == 200):
		response = response.json()
		new_message = "Name: " + response['name'].title() + "\nType:"
		for i in response['types']:
			new_message += " " + i['type']['name'].title() 
		new_message+= "\nAbilities:"
		for i in response['abilities']:
			new_message += " " + i['ability']['name'].title() 
		new_message+= "\nStats:\n"
		bst = 0
		for i in response['stats']:
			new_message += "    " + i['stat']['name'].upper() + ": " + str(i['base_stat']) + "\n"
			bst += i['base_stat']
		new_message+= "Base Stat Total: " + str(bst)
		return new_message
