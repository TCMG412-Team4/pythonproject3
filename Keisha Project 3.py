#imports
import datetime
from datetime import date, timedelta

#Total requests made in the log time period
with open(r'http_access_log.txt','r') as request_log:
    readlines_request_log = request_log.readlines()
    remote_string = "remote - - ["
    local_string = "local - - ["

    strings_with_remote = [remote for remote in readlines_request_log if remote_string in remote]
    strings_with_local = [local for local in readlines_request_log if local_string in local]
    requests_total = len(strings_with_remote) + len(strings_with_local)
    
    print(requests_total, "total request were made in the log time period.")

#Total requests made in 6 months
start_date = (datetime.datetime(1995,4,10)) #starts at 4/11/1995
end_date = (datetime.datetime(1995,10,11))

#gets number of days in the past 6 months
delta = end_date - start_date
#print(delta) #checks number of days: 184 days (183 days + 04/10/1995)
date_list = []

# month name
month_name = ['April','May','June','July','August','September','October']
#formats and appends each day to date_list
for i in range(delta.days):
    day = (start_date +timedelta(days=i + 1)).strftime("%d/%b/%Y")
    date_list.append(day)   

with open(r'http_access_log.txt','r') as request_log:
    readlines_request_log = request_log.readlines()
    remote_string = "remote - - ["
    local_string = "local - - ["

    strings_with_remote = [remote for remote in readlines_request_log if remote_string in remote]
    #strings_with_remote = strings_with_remote[:1] + " " + strings_with_remote[1:]
    strings_with_local = [local for local in readlines_request_log if local_string in local]
    total_strings = strings_with_remote + strings_with_local
    
    #***********test model***************
    # string_list = ['local - - [24/Oct/1994:17:36:18 -0600] "GET 2.gif HTTP/1.0" 200 2555', 'remote - - [23/Oct/1994:17:36:18 -0600] "GET 2.gif HTTP/1.0" 200 2555', 'local - - [24/Oct/1994:17:36:18 -0600] ""GET 2.gif HTTP/1.0"" 200 2555']
    # modified_list = [sub.replace('remote - - [', 'remot - - [') for sub in string_list]
    # print(modified_list, "is this modified list.")
    

    # string_list = ['local - - [24/Oct/1994:17:36:18 -0600] "GET 2.gif HTTP/1.0" 200 2555', 'remote - - [23/Oct/1994:17:36:18 -0600] "GET 2.gif HTTP/1.0" 200 2555']
    # modified_list = [sub.replace('remote - - [', 'remot - - [') for sub in string_list]
    # print(modified_list, "is this modified list.")

    #*******lab model*******
    #removes extra character ('e') to make local and remote strings have the same character count in the beginning
    modified_list = [sub.replace('remote - - [', 'remot - - [') for sub in total_strings]
    
    #extracts date from the list of filtered data
    extract_date = [k[11:22] for k in modified_list]
  
    #double checking elements
    #print(extract_date[-1])
    #print(date_list[-1])

    counter = 0
    e = 0
    while e < len(extract_date):
        if extract_date[e] in date_list:
            counter += 1
        else:
            pass
        e += 1
    print(counter, "total requests were made in the last six months.")