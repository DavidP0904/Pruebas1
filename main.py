import requests

respuesta = requests.get("https://api.github.com")
print("Codigo de respuesta:", respuesta.status_code)