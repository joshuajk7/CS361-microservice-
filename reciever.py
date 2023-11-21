import random
import time


def suggestLocation():
    while True:
        with open('location-microservice.txt', 'w') as file:
            file.write("run")
        time.sleep(5)
        with open('location-microservice.txt', 'r') as file:
            content = file.read().strip()
            if content != 'run':
                file.seek(0)
                rand_city = file.read()
                with open('location-microservice.txt', 'w') as file:
                    file.write("")
                return rand_city



print(suggestLocation())
