import random
import time


def generateRandomCity():
    us_cities = [
        "New York City",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Philadelphia",
        "San Antonio",
        "San Diego",
        "Dallas",
        "San Jose",
        "Austin",
        "Jacksonville",
        "San Francisco",
        "Columbus",
        "Indianapolis"
    ]

    while True:
        time.sleep(2)
        with open("location-microservice.txt", "r+") as file:
            content = file.read().strip()
            if content == "run":
                random_number = random.randint(0, len(us_cities) - 1)
                file.seek(0)  # Move the file cursor to the beginning
                file.truncate(0)  # Clear the file content
                file.write(us_cities[random_number])
                break



generateRandomCity()
