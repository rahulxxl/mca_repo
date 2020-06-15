import json
import requests

MAPS_API_KEY = "ua9AKL2fpGPEnZ2Ba7Mwt1TNLA8hbuT3"

City_Keys = {
    "amritsar": "205593",
}

GeoLocation = {
    'Latitude': 31.64,
    'Longitude': 74.865,
}



r_text = '''
[
    {
        "LocalObservationDateTime": "2020-06-11T16:25:00+05:30",
        "EpochTime": 1591872900,
        "WeatherText": "Sunny",
        "WeatherIcon": 1,
        "HasPrecipitation": false,
        "PrecipitationType": null,
        "IsDayTime": true,
        "Temperature": {
            "Metric": {
                "Value": 37.2,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 99,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "RealFeelTemperature": {
            "Metric": {
                "Value": 37.8,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 100,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "RealFeelTemperatureShade": {
            "Metric": {
                "Value": 36,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 97,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "RelativeHumidity": 30,
        "IndoorRelativeHumidity": 30,
        "DewPoint": {
            "Metric": {
                "Value": 17.2,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 63,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "Wind": {
            "Direction": {
                "Degrees": 338,
                "Localized": "NNW",
                "English": "NNW"
            },
            "Speed": {
                "Metric": {
                    "Value": 14.8,
                    "Unit": "km/h",
                    "UnitType": 7
                },
                "Imperial": {
                    "Value": 9.2,
                    "Unit": "mi/h",
                    "UnitType": 9
                }
            }
        },
        "WindGust": {
            "Speed": {
                "Metric": {
                    "Value": 14.8,
                    "Unit": "km/h",
                    "UnitType": 7
                },
                "Imperial": {
                    "Value": 9.2,
                    "Unit": "mi/h",
                    "UnitType": 9
                }
            }
        },
        "UVIndex": 3,
        "UVIndexText": "Moderate",
        "Visibility": {
            "Metric": {
                "Value": 4.8,
                "Unit": "km",
                "UnitType": 6
            },
            "Imperial": {
                "Value": 3,
                "Unit": "mi",
                "UnitType": 2
            }
        },
        "ObstructionsToVisibility": "H",
        "CloudCover": 6,
        "Ceiling": {
            "Metric": {
                "Value": 6949,
                "Unit": "m",
                "UnitType": 5
            },
            "Imperial": {
                "Value": 22800,
                "Unit": "ft",
                "UnitType": 0
            }
        },
        "Pressure": {
            "Metric": {
                "Value": 1000,
                "Unit": "mb",
                "UnitType": 14
            },
            "Imperial": {
                "Value": 29.53,
                "Unit": "inHg",
                "UnitType": 12
            }
        },
        "PressureTendency": {
            "LocalizedText": "Falling",
            "Code": "F"
        },
        "Past24HourTemperatureDeparture": {
            "Metric": {
                "Value": 4.4,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 8,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "ApparentTemperature": {
            "Metric": {
                "Value": 38.9,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 102,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "WindChillTemperature": {
            "Metric": {
                "Value": 37.2,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 99,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "WetBulbTemperature": {
            "Metric": {
                "Value": 23.2,
                "Unit": "C",
                "UnitType": 17
            },
            "Imperial": {
                "Value": 74,
                "Unit": "F",
                "UnitType": 18
            }
        },
        "Precip1hr": {
            "Metric": {
                "Value": 0,
                "Unit": "mm",
                "UnitType": 3
            },
            "Imperial": {
                "Value": 0,
                "Unit": "in",
                "UnitType": 1
            }
        },
        "PrecipitationSummary": {
            "Precipitation": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "PastHour": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "Past3Hours": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "Past6Hours": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "Past9Hours": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "Past12Hours": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "Past18Hours": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            },
            "Past24Hours": {
                "Metric": {
                    "Value": 0,
                    "Unit": "mm",
                    "UnitType": 3
                },
                "Imperial": {
                    "Value": 0,
                    "Unit": "in",
                    "UnitType": 1
                }
            }
        },
        "TemperatureSummary": {
            "Past6HourRange": {
                "Minimum": {
                    "Metric": {
                        "Value": 34.6,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 94,
                        "Unit": "F",
                        "UnitType": 18
                    }
                },
                "Maximum": {
                    "Metric": {
                        "Value": 37.6,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 100,
                        "Unit": "F",
                        "UnitType": 18
                    }
                }
            },
            "Past12HourRange": {
                "Minimum": {
                    "Metric": {
                        "Value": 25.2,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 77,
                        "Unit": "F",
                        "UnitType": 18
                    }
                },
                "Maximum": {
                    "Metric": {
                        "Value": 37.6,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 100,
                        "Unit": "F",
                        "UnitType": 18
                    }
                }
            },
            "Past24HourRange": {
                "Minimum": {
                    "Metric": {
                        "Value": 25.2,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 77,
                        "Unit": "F",
                        "UnitType": 18
                    }
                },
                "Maximum": {
                    "Metric": {
                        "Value": 37.6,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 100,
                        "Unit": "F",
                        "UnitType": 18
                    }
                }
            }
        },
        "MobileLink": "http://m.accuweather.com/en/in/amritsar/205593/current-weather/205593?lang=en-us",
        "Link": "http://www.accuweather.com/en/in/amritsar/205593/current-weather/205593?lang=en-us"
    }
]
'''

# headers = {'referer':"https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/search"}

# Now make the request
#r = requests.get('http://dataservice.accuweather.com/locations/v1/cities/search', params=payload)

url_hourly = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + City_Keys["amritsar"]



r_fiveDays = 3
r_hourly = 3


def getCurrentConditions():
    payload_curr = {"apikey": MAPS_API_KEY, "q": "amritsar", "details":"true"}
    url_curr = "http://dataservice.accuweather.com/currentconditions/v1/"+City_Keys["amritsar"]
    # TODO: Make the get request call now
    r_currWeather = requests.get(url_curr, payload_curr)
    currData = r_currWeather.text
    currDict = json.loads(currData)
    currCondition = {
        "weather_text": currDict[0]["WeatherText"],
        "weather_icon": currDict[0]["WeatherIcon"],
        "temperature": currDict[0]["Temperature"]["Metric"]["Value"],
        "humidity" : currDict[0]["RelativeHumidity"],
        "wind_direction": currDict[0]["Wind"]["Direction"]["English"],
        "wind_speed" : currDict[0]["Wind"]["Speed"]["Metric"]["Value"],    
    }


def getHourlyConditions():
    date_str = "2020-06-12T13:00:00+05:30"
    hours = date_str[11:13]
    mins = date_str[14:16]
    hoursInt = int(hours)
    amPm ="am"

    if hourInt >= 0 and hoursInt <= 12 :
        amPm = "am"
    elif hoursInt > 12 and hoursInt <= 23 :
        amPm = "pm"



