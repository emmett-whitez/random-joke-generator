import requests

url = "https://official-joke-api.appspot.com/random_joke"

run = True

while run:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        print(f"{data["setup"]}\n{data["punchline"]}\n")
        res = str(input("Wanna hear another joke? (y/n):"))

        if res == "n":
            run = False
        else: continue

    else:
        print("Failed to retreive data from {url}")