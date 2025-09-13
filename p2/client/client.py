import requests

r = requests.get("http://s2:8000/ping")  # use container name as host
print("Got response from container 2:", r.json())
