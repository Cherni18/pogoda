import requests
ola=input("введите город ")
url = f"https://wttr.in/{ola}"
response = requests.get(url)
response.raise_for_status()
print(response.text)
print(response)