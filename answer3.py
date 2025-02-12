import requests
import time

urls = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",
    "http://httpstat.us/500",
    "https://www.google.com/"
]

def check_urls():
    for url in urls:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        print(url, "-> Status:", status_code)
        if 400 <= status_code < 600:
            print("Error", url, "returned error status:", status_code)
        if status_code == 200:
            print("Success", url, "returned status:", status_code)

while True:
    check_urls()
    print("NEXT CHECK")
    time.sleep(10)
