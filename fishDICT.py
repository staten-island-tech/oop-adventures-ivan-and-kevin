import requests


response = requests.get("https://fishbase.ropensci.org/fishbase")
if response.status_code != 200:
    print("Error fetching data!")
data = response.json()
print(data)

