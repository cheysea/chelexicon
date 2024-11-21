import browser_cookie3
import requests

# Get cookies from Chrome
cookies = browser_cookie3.chrome()

# Make a request with the cookies
response = requests.get("https://www.humblebundle.com/home/library", cookies=cookies)

# Print the response
print(response.text)