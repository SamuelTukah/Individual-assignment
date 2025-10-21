#q6_github_weather_async
"""Q6: Basic API interaction and async calls to GitHub & Open-Meteo."""

import asyncio
import aiohttp
import requests

GITHUB_USER = "https://api.github.com/users/octocat"
GITHUB_USERS = ["octocat", "torvalds", "mojombo", "defunkt", "pjhyett"]
WEATHER_API = "https://api.open-meteo.com/v1/forecast?latitude=0.3&longitude=32.6&current_weather=true"

# Part A: synchronous example using requests
def fetch_sync_github():
    r = requests.get(GITHUB_USER, timeout=10)
    r.raise_for_status()
    data = r.json()
    print("Synchronous GitHub fetch:")
    print("Name:", data.get("name"))
    print("Public repos:", data.get("public_repos"))
    print("Profile URL:", data.get("html_url"))

# Part B & C: asynchronous using aiohttp
async def fetch_github_user(session, username, retries=3):
    url = f"https://api.github.com/users/{username}"
    for attempt in range(1, retries+1):
        try:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    print(f"[{username}] status {resp.status}")
        except Exception as e:
            print(f"[{username}] attempt {attempt} failed: {e}")
        await asyncio.sleep(1)
    return None

async def fetch_weather(session):
    async with session.get(WEATHER_API, timeout=10) as resp:
        return await resp.json()

async def main_async():
    async with aiohttp.ClientSession() as session:
        #to launch GitHub user fetches 
        tasks = [fetch_github_user(session, u) for u in GITHUB_USERS]
        tasks.append(fetch_weather(session))  
        results = await asyncio.gather(*tasks)
        
        weather = results[-1]
        users = results[:-1]

        # sort users by public_repos
        users = [u for u in users if u]
        users_sorted = sorted(users, key=lambda x: x.get("public_repos", 0), reverse=True)
        print("\nTop GitHub users by public_repos:")
        for u in users_sorted:
            print(u.get("login"), "repos:", u.get("public_repos"))

        # print weather summary
        if weather and "current_weather" in weather:
            cw = weather["current_weather"]
            print("\nWeather (lat=0.3,long=32.6):")
            print("temperature:", cw.get("temperature"), "windspeed:", cw.get("windspeed"))

if __name__ == "__main__":
   
    fetch_sync_github()
   
    asyncio.run(main_async())
