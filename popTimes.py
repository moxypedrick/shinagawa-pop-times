import googlemaps
import populartimes
from datetime import datetime
import numpy as np
import pandas as pd

key='AIzaSyBZS83bpkP4MhkFYzRXkcfcPI5llceuISM'



l2 = [35.615647, 139.731446]
#l2 = [35.623572, 139.746225]
u2 = [35.655782, 139.766209]
#u2 = [35.634872, 139.753246]

type = ["hospital", "library", "grocery_or_supermarket", "bar", "bus_station", "cafe", "restaurant"]
#["transit_station", "store", "park", "school",  
#"lodging", "night_club", "local_government_office", 

dayMap = {"Monday": "6/1/2020", "Tuesday":"6/2/2020", "Wednesday":"6/3/2020", "Thursday":"6/4/2020", "Friday":"6/5/2020", "Saturday":"6/6/2020", "Sunday":"6/7/2020"}

dataList = []

dataList.append(['name', 'rating', 'id', 'cat1', 'cat2', 'day', 'hour', 'date', 'pop', 'time-spent', 'lat', 'lng'])

for item in type:
    dataList = []
    dataList.append(['name', 'rating', 'id', 'cat1', 'cat2', 'day', 'hour', 'date', 'pop', 'time-spent', 'lat', 'lng'])
    fileName = 'google-data-'+str(item)+'.csv'
    print(item)
    popTimes = populartimes.get(key, item,l2,u2)
    p=0
    
    popTimesLength = len(popTimes)
    print(popTimesLength)
    while p < popTimesLength:
        bizName = popTimes[p]['name']
        bizName.replace(',','')
        bizId = popTimes[p]['id']
        bizType0 = popTimes[p]['types'][0]
        bizType1 = popTimes[p]['types'][1]
        lat = popTimes[p]['coordinates']['lat']
        lng = popTimes[p]['coordinates']['lng']

        try:
            rating = popTimes[p]['rating']
            timeSpent = popTimes[p]['time_spent'][1]
        except:
            rating = 0
            timeSpent = 0
        
        for item in popTimes[p]['populartimes']:
            popList = item['data']
            day2 = dayMap[item['name']]
            itemName = item["name"]

            hour = 0
            popListLength = len(popList)
            while hour < popListLength:
                #print(popList[hour])
                dateString = day2 +" "+ str(hour) + ":00"
                listItem = [
                    bizName, str(rating), bizId,
                    bizType0, bizType1, itemName,
                    str(hour), dateString, popList[hour],
                    str(timeSpent), str(lat), str(lng)
                ]
                dataList.append(listItem)
                hour = hour + 1        
        p = p + 1
        print(p)
    b = np.array(dataList) 
    
    np.savetxt(fileName, b, delimiter=',', comments='', fmt='%s', encoding='utf-8') 
    b=None 

   


   
'''"accounting",
    "airport",
    "amusement_park",
    "aquarium",
    "art_gallery",
    "atm",
    "bakery",
    "bank",
    "bar",
    "beauty_salon",
    "bicycle_store",
    "book_store",
    "bowling_alley",
    "bus_station",
    "cafe",
    "campground",
    "car_dealer",
    "car_rental",
    "car_repair",
    "car_wash",
    "casino",
    "cemetery",
    "church",
    "city_hall",
    "clothing_store",
    "convenience_store",
    "courthouse",
    "dentist",
    "department_store",
    "doctor",
    "drugstore",
    "electrician",
    "electronics_store",
    "embassy",
    "fire_station",
    "florist",
    "funeral_home",
    "furniture_store",
    "gas_station",
    "grocery_or_supermarket",
    "gym",
    "hair_care",
    "hardware_store",
    "hindu_temple",
    "home_goods_store",
    "hospital",
    "insurance_agency",
    "jewelry_store",
    "laundry"]
'''

'''
    lawyer
    library
    light_rail_station
    liquor_store
    local_government_office
    locksmith
    lodging
    meal_delivery
    meal_takeaway
    mosque
    movie_rental
    movie_theater
    moving_company
    museum
    night_club
    painter
    park
    parking
    pet_store
    pharmacy
    physiotherapist
    plumber
    police
    post_office
    primary_school
    real_estate_agency
    restaurant
    roofing_contractor
    rv_park
    school
    secondary_school
    shoe_store
    shopping_mall
    spa
    stadium
    storage
    store
    subway_station
    supermarket
    synagogue
    taxi_stand
    tourist_attraction
    train_station
    transit_station
    travel_agency
    university
    veterinary_care
    zoo'''

#placeId = "ChIJX-8n5USKGGARhNuxeFFyY_Y"

#popTime = populartimes.get_id(key,placeId)