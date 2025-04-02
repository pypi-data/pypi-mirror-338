
import requests
import getpass
from pyarrow import flight
from pyarrow.flight import FlightClient
import time
import requests
import json
import time
import urllib3
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


def get_nni():
    nni = getpass.getpass(prompt="NNI ?")
    password = getpass.getpass(prompt="password ?")
    return nni, password


def get_token():

    uri = os.getenv("DREMIO_URI")
    cert_path = os.getenv("CERT_PATH")
    dremio_username = os.getenv("DREMIO_USERNAME")
    dremio_password = os.getenv("DREMIO_PASSWORD")

    # Verification of the certificate, else False
    verify = cert_path if cert_path else False 

    # Get NNI and password 
    try:
        username = dremio_username
        password = dremio_password 
        
        payload = {'userName': username, 'password': password}
        
         # First login attempt
        response = requests.post(uri, json=payload, verify=verify) 

        if response.status_code == 200:
            pass
        else:
            username, password = get_nni()
            payload = {'userName': username, 'password': password}

            #Second login attempt
            response = requests.post(uri, json=payload, verify=verify) 

        if response.status_code != 200:
            raise ValueError("Authentication failed")
        
    except Exception as e:
        print("Error:", str(e))
        return None, None
   
    # Parse the JSON response
    data = response.json()
    token = data.get("token", "") #Extract the token 
    expires = data.get("expires", 0)/1000 # Expiration time in secondes 
    expiration = datetime.fromtimestamp(expires).strftime("%m/%d/%Y at %I:%M:%S")
    time_left = datetime.fromtimestamp(expires) - datetime.today()
    days = time_left.days
    seconds = time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    print(f"Token aquired, it will expire on {expiration}")
    print(f"Time remaining : {days} days, {hours} hours, {minutes} minutes")

    return token, expires 


def get_results(query, token):
    try:
        token = token[0]
        location = os.getenv("DREMIO_LOCATION")
        headers = [(b"authorization", f"bearer {token}".encode("utf-8"))]
        client = flight.FlightClient(location=location, disable_server_verification=False)
        options = flight.FlightCallOptions(headers=headers)
        flight_info = client.get_flight_info(flight.FlightDescriptor.for_command(query), options)
        results = client.do_get(flight_info.endpoints[0].ticket, options)
        return results.read_pandas()
    except:
        print("Failed to get the token")


def time_left(expires):
    expires = expires[1]
    expiration = datetime.fromtimestamp(expires).strftime("%B %d, %Y at %I:%M:%S")
    time_left = datetime.fromtimestamp(expires) - datetime.today()
    days = time_left.days
    seconds = time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    print(f"It will expire on {expiration}")
    print(f"Time remaining : {days} days, {hours} hours, {minutes} minutes")





