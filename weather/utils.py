import requests
from django.conf import settings

def fetch_aqi_data(city: str) -> dict | None:
    url = f"https://api.waqi.info/feed/{city}/?token={settings.AQICN_TOKEN}"
    resp = requests.get(url)
    #print("WAQI HTTP:", resp.status_code, resp.text)    # ← debug
    data = resp.json()
    if data.get("status") == "ok":
        #print("WAQI DATA:", data["data"])               # ← debug
        return data["data"]
    #print("WAQI ERROR:", data)                          # ← debug
    return None