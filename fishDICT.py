import requests

url = "https://fish-species.p.rapidapi.com/fish_api/fishes"

headers = {
	"x-rapidapi-key": "2e6dc38449msh075cddb5b0cebb9p1da0c7jsne372cef69d56",
	"x-rapidapi-host": "fish-species.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

fishDICT = {
    
}