
capitlas = {
    "France": "Paris"
    "Poland": "Warsaw"
}

#nesting a list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
    "Poland": ["Warsaw", "Cracow", "Poznan"]
}

#nesting dictionary in a dictionary

travel_log_details = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
    "Poland": {"cities_visited": ["Warsaw", "Cracow", "Poznan"], "total_visits": 30}
}

#nesting dictionary inside a single list

travel_log_details = {
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
    },
    {"country": "Poland",
     "cities_visited": ["Warsaw", "Cracow", "Poznan"],
     "total_visits": 30
    },
}