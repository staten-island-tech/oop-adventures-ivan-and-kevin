import requests

url = "https://fish-species.p.rapidapi.com/fish_api/group"

querystring = {"meta_property":"scientific_classification","property_value":"actinopterygii","meta_property_attribute":"class"}

headers = {
	"x-rapidapi-key": "2e6dc38449msh075cddb5b0cebb9p1da0c7jsne372cef69d56",
	"x-rapidapi-host": "fish-species.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
