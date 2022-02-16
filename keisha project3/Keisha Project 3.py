# imports
import urllib.request    
import datetime
from datetime import date, timedelta

# retrieve log file
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "http_access_log.txt")

#reads file
with open(r'http_access_log.txt','r') as request_log:
    readlines_request_log = request_log.readlines()
    
    #filters out lines with no requests
    remote_string = "remote - - ["
    local_string = "local - - ["

    strings_with_remote = [remote for remote in readlines_request_log if remote_string in remote]
    strings_with_local = [local for local in readlines_request_log if local_string in local]
    
    total_strings = strings_with_remote + strings_with_local
    
    # ****TOTAL REQUESTS MADE IN THE LOG TIME PERIOD****
    print(len(total_strings), "total request were made in the log time period.")

    # ****TOTAL REQUESTS MADE IN PAST 6 MONTHS****

    # formatting dates************************************************************
    # 6 month timeframe dates
    start_date = (datetime.datetime(1995,4,10)) #starts at 4/11/1995
    end_date = (datetime.datetime(1995,10,11))

    # gets total number of days in the past 6 months
    delta = end_date - start_date #184 days (183 days + 04/10/1995)
    # list to gather all log days within past 6 months
    date_list = []

    # month names
    month_name = ['April','May','June','July','August','September','October']
    # formats and appends each day to date_list
    for i in range(delta.days):
        day = (start_date +timedelta(days=i + 1)).strftime("%d/%b/%Y")
        date_list.append(day)   

    # filter out dates to only those within last 6 months**************************
        
    #removes extra character ('e') to make local and remote strings have the same character count in the beginning
    modified_list = [sub.replace('remote - - [', 'remot - - [') for sub in total_strings]
    
    #extracts date from the list of filtered data
    extract_date = [k[11:22] for k in modified_list]

    #counting requests within the past 6 months
    counter = 0
    #iteration count
    e = 0
    while e < len(extract_date):
        if extract_date[e] in date_list:
            counter += 1
        else:
            pass
        e += 1
    print(counter, "total requests were made in the last six months.")
