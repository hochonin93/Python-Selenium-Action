import requests

# URL to make the request to
url = 'https://ipinfo.io/json'

# Making a GET request to the URL
response = requests.get(url)

# Parsing the JSON data
data = response.json()
print(str(data))
# Extracting the IP address from the response
ip_address = data['ip']

# Define the path where you want to save the file
file_path = 'ip_addresses.txt'  # Change this to your desired file path

# Appending the IP address to a text file with a newline
with open(file_path, 'a') as file:
    file.write(str(data) + '\n')
