import requests
import json


hassioHost = ""
token = ""
#hassioHost = "http://192.168.50.5:8123"
#token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2M2NlNDdmMDg1ZWQ0MThmOTg5ZDE5MDczNjUwMmNiNCIsImlhdCI6MTcxMzcxNzI3OSwiZXhwIjoyMDI5MDc3Mjc5fQ.V0m3REmXt6d7hFJrtMPfazMPhsOM0LfnFmJvrplSZ1o"



def getTemperatur():
    endpoint = "/api/states/sensor.garten_wetterstation_temperature"
    url = hassioHost + endpoint
    headers = {
        "Authorization": token,
        "content-type": "application/json",
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    temperatur = data["state"]
    return temperatur


if __name__ == "__main__":
    print(getTemperatur())
