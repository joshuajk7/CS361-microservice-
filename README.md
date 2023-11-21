# CS361-microservice-

Suggest a Location Microservice
This github repo contains the implementation for the suggest a location microservice. This readme contains the communication contract that demonstrates how to use the microservice

Communication Contract
# A - How to REQUEST data from the microservice
Instructions:

- git clone this repository
- Put files into project folder
- Either copy suggestLocation function into main project file or import from `receiver.py`
- Run `sender.py`

Communication contract

The following code shows an example call to the microservice to request (and receive) data
```
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
```
Example return
```
'Phoenix'
```
# B - How to RECEIVE data from the microservice
Make sure the microservice is running -- this means that the microservice is ready to accept requests and send back responses
Call the microservice using a call such as the one demonstrated above to request data from the microservice
The example call above demonstrates how to read to RECEIVE data from the microservice. The example above shows both how to REQUEST and RECEIVE data from the microservice.
# C - UML Diagram
![Alt Text](https://raw.githubusercontent.com/joshuajk7/CS361-microservice-/main/UML%20sequence%20diagram.PNG)
