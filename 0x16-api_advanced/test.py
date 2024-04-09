import requests

# response = requests.get('https://www.reddit.com/dev/api/')
response = requests.get('https://www.reddit.com/r/programming/about.json')

# Get the headers from the response
headers = response.headers

# Print the headers
# print(headers)

content_type = response.headers['User-Agent']
print(content_type)