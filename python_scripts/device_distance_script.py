# device_distance_script.py

device_1 = "device_tracker." + data.get('device_id_1')
device_2 = "device_tracker." + data.get('device_id_2')
unit = data.get('unit')
sensor_name = "distance_"+ data.get('device_id_1') +"_" + data.get('device_id_2')
friendly_name = "Distance between " + data.get('device_id_1') +" and " + data.get('device_id_2')

# Get current & new state
device_1 = hass.states.get(device_1)
device_2 = hass.states.get(device_2)

if unit == 'metric':
    f = 0.6
    unitof = 'mi'
else:
    f = 1
    unitof = 'km'
    
    
try:
    device_1_lat = device_1.attributes.get('latitude')
    device_1_long = device_1.attributes.get('longitude')
    device_2_lat = device_2.attributes.get('latitude')
    device_2_long = device_2.attributes.get('longitude')



    # approximate radius of earth in km
    R = 6373.0
    
    lat1 = math.radians(device_1_lat)
    lon1 = math.radians(device_1_long)
    lat2 = math.radians(device_2_lat)
    lon2 = math.radians(device_2_long)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = round(R * c * f,2) 
    
    hass.states.set(('sensor.' + sensor_name), distance, 
        {
            "icon" : "mdi:map-marker-distance",
            "friendly_name" : friendly_name,
            "unit_of_measurement": unitof, 
            "devices":data.get('device_id_1') +" & " + data.get('device_id_2')
        
    }) 
    
    
    logger.info("Distance Tracker {}".format(distance))

except:
    logger.info("Distance Tracker - Check config! No coordinates found!")
