import requests #pip install requests

city=input("Please Enter the city for know the clime: ")

url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=YOURKEY&units=metric".format(city)#url for call the api and key

response=requests.get(url)#get url with the protocol http get
data=response.json()#parse the response with json (javascript object notation)

temperature=data["main"]["temp"]#save the temperature and other attributes with the index example of this
"""
Example
{
    main:{
        temp:282,
    }
}
"""
wind_speed=data["wind"]["speed"]
longitude=data["coord"]["lon"]
latitude=data["coord"]["lat"]
description=data["weather"][0]["description"]
"""
{
Example
    weather:[
        description:'Broke cloud'
    ]
}
"""

print('The temperature is: {} \nThe wind speed is: {} \nThe longitude is: {} \nThe latitude is: {} \nThe description is: {}'.format(temperature,wind_speed,longitude,latitude,description))
#Print the values with format