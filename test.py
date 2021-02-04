from urllib.parse import urlencode
import requests
API_KEY = ""


def getData(address, dataType='json'):
    base = f"https://maps.googleapis.com/maps/api/geocode/{dataType}"  # url
    params = {
        "address": address, "key": API_KEY}
    url_params = urlencode(params)
    url = f"{base}?{url_params}"
    data = requests.get(url)
    if data.status_code not in range(200, 299):
        return {}
    return data.json()


address1 = getData("1600 Amphitheatre Parkway, Mountain View, CA")
print(address1)  # ["results"][0]['address_components'])
print("\n")

# Abstract factory pattern
