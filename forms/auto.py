import requests

# 1. The test URL
url = "https://httpbin.org/post"

# 2. Fake form data
data = {
    "first_name": "John",
    "last_name": "Doe",
    "favorite_color": "Blue"
}

# 3. Send the request
response = requests.post(url, data=data)

# 4. See the result
if response.status_code == 200:
    print("Success! The server received this data:")
    # httpbin returns JSON data showing what you sent
    print(response.json()['form'])
else:
    print("Failed with status code:", response.status_code)
