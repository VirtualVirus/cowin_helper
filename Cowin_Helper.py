import requests
import datetime
import json
from twilio.rest import Client


#account_sid = ""
#auth_token  = ""

#client = Client(account_sid, auth_token)

DIST_ID = 776
print_flag = 'y'
numdays = 10
age = 18
total_slots = 0

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 1))
        if resp_json["centers"]:
            print("Available on: {}".format(INP_DATE))
            if(print_flag=='y' or print_flag=='Y'):
                for center in resp_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age:
                            print("\t", center["name"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            print("\n\n")
                            
            
print("Total Slots =" +str(total_slots))

if(total_slots <= 0):
    print("No slots for Today")

if(total_slots > 0):
    print("Some Slots are there")