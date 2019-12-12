# Final-Report

## Description

This Project for INST 326 uses the https://openweathermap.org/api API to get the daily weather data 
for a specified location inputted. The data pulled includes location, temperature,
humidity and other data depending on the what the user wants. 

And we also make a temperature converter which can conver Kelvin to celsius and fahrenheit. 

The finalmain.py file located in this repository, uses the supplied API 
and modules to output the data of the locations wanted.

And the test.py can actually test if the converter calculate correctly.

## Run
A sample program call finalmain.py will use the module to go through all the weather information from the API. You can run it like this:
   
   
       python3 finalmain.py


You will also need to get a openweather API key and store it in a file in this directory called *key.txt*.

You can run a test for the program using these terminal commands:

       pytest test.py
       
       or
       
       pytest finaltest.py

In order to successfully execute the test, you must have a file titled __init__.py in the same directory as the finalmain.py and finaltest.py files.

## Install

You will need Python3 to use this project. 
You can install it using this link: https://www.python.org/downloads/

For the pytest, you may need to install
Run the following command in your command line:

       pip3 install -U pytest

## License

[Open WeatherMap API]: https://openweathermap.org/api
[key]: 219b74026949c164fc504f625a7b805c
