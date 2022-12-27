import os
import requests

websiteUrl = input("Please enter a full URL address:\n(Follow this format: http://latimere.io as an example)\nEnter website here: ")

queryParameters = {"q":"MLIS"}

userResponse = requests.get(websiteUrl, queryParameters)
if userResponse.status_code == 200:
    print(userResponse.text)
else:
    print("Website Not Reachable: {response.status_code}")






