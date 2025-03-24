import requests

apikey= 'get api key from openweathermap by signing in'
baseURL= 'https://api.openweathermap.org/data/2.5/weather?q='
# here the url would be like- https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}
# all info. about how exactly we have to write url is given in the website 
city= input("Enter city name: ")
completeURL= baseURL+city+'&appid='+apikey

response= requests.get(completeURL)
data= response.json()
print(data) # this will print all info. all info are under main dictionary
print(data['main']['temp']['temp_max']['temp_min']) # from main, we get these info. 