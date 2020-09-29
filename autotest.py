import requests

def send_login():
    r =requests.get(url="http://localhost:5002/protected")
    print(r.text)