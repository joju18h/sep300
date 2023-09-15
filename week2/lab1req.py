import asyncio
import requests
import os

async def fetch_data(url):
    response = requests.get(url)
    if(response.status_code == 200): #200 means
        return f"{url} has returned an OK response"
    else:
        return f"Request failed for {url}"

async def main():
    tasks = [
        fetch_data("https://api.apis.guru/v2/list.json"),
        fetch_data("https://api.publicapis.org/entries"),
        fetch_data("https://api.artic.edu/api/v1/artworks/search?q=cats")
    ]

    results =  await asyncio.gather(*tasks)
    print("All tasks have been executed")

    for result in results:
        print(result)

asyncio.run(main())


choice = input("Press any key to clear the terminal ")
os.system('clear')
