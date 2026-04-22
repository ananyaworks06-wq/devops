import requests
import time

print("Checking API...")

start = time.time()

response = requests.get("https://jsonplaceholder.typicode.com/posts")

end = time.time()

response_time = (end - start) * 1000

print("Response time:", response_time, "ms")

if response_time > 500:
    raise Exception("Too slow ❌")

print("API is fast ✅")