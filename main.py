import functions_framework, requests


LATITUDE = 'INSERT_YOUR_LATITUDE_HERE'
LONGITUDE = 'INSERT_YOUR_LONGITUDE_HERE'
OPEN_WEATHER_MAP_API_KEY = 'INSERT_YOUR_OPENWEATHERMAP_API_KEY_HERE'
WIRE_PUSHER_DEVICE_ID = 'INSERT_YOUR_WIREPUSHER_DEVICE_ID_HERE'


def check_humidity(request):
    r = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s' % (
            LATITUDE, LONGITUDE, OPEN_WEATHER_MAP_API_KEY))
    humidity = r.json().get('main').get('humidity')

    low_humidity_alert_message = 'Humidity is low ({}%) in your neighborhood right now,' \
                                 ' you should consider using an air humidifier.'.format(humidity)
    print(low_humidity_alert_message)

    if humidity <= 50:
        requests.get(
            'https://wirepusher.com/send?id={}&title=Alert&message={}'.format(WIRE_PUSHER_DEVICE_ID, low_humidity_alert_message))
    return 'OK'