# A list of actors
Actors = [ "Tom Cruise",
            "Angelina Jolie",
            "Kristen Stewart",
            "Blake lively"
]

# A dictionary of an actor
Actor = { "Name": "Tom Cruise"}
print(f'{Actor["Name"]}')

# A dictionary can contain multiple pairs of information
Actor_info = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
}   

# A dictionary can contain multiple types of information
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best_movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]
}
print(f'{another_actor["name"]} was in {another_actor["best_movies"][0]}')

# A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")


