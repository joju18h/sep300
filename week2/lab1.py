#George Paul Robert, ID: 117928226
import asyncio
import aiohttp

async def fetch_data(url):

#Note to self: 'async with' indicates an asychronus context manager which automatically manages the handling of the connection
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            apiStatus = response.status

    if(apiStatus ==  200):
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
