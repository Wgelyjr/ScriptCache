#A simple little script that requests pokemon & type information from the pokeapi

import requests
import sys
import json

finished = False
while finished == False:
	query = input("Enter a Pokemon, Pokemon type, or quit to exit: ")
	query = query.lower()
	if query == "quit":
		quit()
	elif query == "debug":
		finished = True
	else:
		pass
	url = "https://pokeapi.co/api/v2/"
	typelist = ["type/","pokemon/"]
	ext_dict = {}
	query_type = ""
	print("")
	#Deciding which query to use, and passing it along
	for type in typelist:
		try:
			ext_dict[type] = requests.get(url + type + query)
			ext_dict[type] = ext_dict[type].text
			ext_dict[type] = json.loads(ext_dict[type])
		except (requests.exceptions.RequestException):
			print("Connection failed; please try again.")
			quit()
	for response in ext_dict:
		if len(ext_dict[response]) > 1:
			query_type = response.strip("/")
			data = ext_dict[response]
			break
		else:
			pass
	#Making the JSON response pretty to be output
	if query_type == "type":
		for key in data["damage_relations"]:
			damage_dict = data["damage_relations"][key][::1]
			form = str(key)
			form = form.replace("_"," ")
			print(form + ":")
			for i in range(0,len(damage_dict)):
				print("\t" + str(damage_dict[i]["name"]))
			print("")
	elif query_type == "pokemon":
		print("Name: " + str(data["name"]))
		if len(data["types"]) > 1:
			print("Types: ", end="")
			print(str(data["types"][0]["type"]["name"]) + ", ",end="")
			print(str(data["types"][1]["type"]["name"]))
		else:
			print("Type: " + str(data["types"][0]["type"]["name"]))
		print("ID no.: " + str(data["id"]))
		height = str(data["height"])
		dec1 = height[0:-1]
		dec2 = height[-1:]
		height = dec1 + "." + dec2
		weight = str(data["weight"])
		dec1 = weight[0:-1]
		dec2 = weight[-1:]
		weight = dec1 + "." + dec2
		print("Average height: " + height + "m")
		print("Average weight: " + weight + "kg")
		print("")
	else:
		print("Make sure to enter a Pokemon or Pokemon type, or check your spelling. \n")