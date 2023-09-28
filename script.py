import requests
def get_times(country, city):
    url = f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"
    try :
        response = requests.get(url)
        info = response.json()
    except:
        raise(ValueError)
    else:
        return ({i:j for i, j in info["data"]["timings"].items()})