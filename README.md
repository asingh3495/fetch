Python Script to check health check of the URL - fetch_method_main.py

1# Import necessary pythonlibraries: 
================
import yaml # To read input YAML file
import requests # To hit the URL with args (method,url,headers,body)
import time # To run the script after each 15 sec
from collections import defaultdict # To collect the total hists and successful hits

2# Define 3 functions:
================
A) load_config() # To load the input YAML file 
       Variable - config(list) 

B) check_health() # To do the health-check of the URL
        Fetch URL, Method, Body, Headers from dict endpoint
        Use requests library to hit above params using request method and capture the response

       *** response = requests.request(method, url, headers=headers, json=body) ***

       If the response is from 200 to 299 and response time is below 500ms, return 'UP' else 'DOWN' 

C)  monitor_endpoints # To do the cummulative caculation for the URL being UP or DOWN   
        Create a variable domain_stats to maintain the count of total hits done to the URL and success hits.
        Calculate the percentage of the availability
        Sleep for 15 sec and retry again

MAIN Function:
        Starts the execution of the above functions and aborts on Keyboard Interrupt


Execute the script using command:
python fetch_method_main.py sample.yaml




