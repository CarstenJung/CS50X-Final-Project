import requests
from flask_cors import CORS   

def colors_API():

    url = "https://random-palette-generator.p.rapidapi.com/palette/10/3"

    headers = {
	"X-RapidAPI-Key": "0312a8b547msh803ce3e5bf40b25p1f493ejsne51ba464e29f",
	"X-RapidAPI-Host": "random-palette-generator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()
    colors = data
    
    return colors
