#!/usr/bin/env python3

import re
import csv
import operator

logs = open("syslog.log","r").readlines()
log_count = dict()

for log in logs:
    error = re.findall(r'ERROR.*\(',log)

    if len(error) != 0:
        log_text = error[0].replace("ERROR","").replace("(","").strip()
        if log_text in log_count.keys():
            log_count[log_text] += 1
        else:
            log_count[log_text] = 1
            
log_count = sorted(log_count.items(), key = operator.itemgetter(1), reverse=True)

with open('error_message.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["Error","Count"])

for log in log_count:
    key,value = log
    with open('error_message.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([key,value])
        

i_count = dict()
e_count = dict()
for log in logs:
    username = re.search(r'\(.*\)',log).group().strip("()")
    error = re.search(r'(ERROR|INFO)',log).group()
    if error == "ERROR":
        if username in e_count.keys():
            e_count[username] += 1
        else:
            e_count[username] = 1
    else:
        if username in i_count.keys():
            i_count[username] += 1
        else:
            i_count[username] = 1

with open('user_statistics.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["Username", "INFO", "ERROR"])

info = set(i_count.keys())
error = set(e_count.keys())
z = error-info
dict_key = dict.fromkeys(z,0)
i_count.update(dict_key)

i_count = sorted(i_count.items(),key=operator.itemgetter(0))
e_count = sorted(e_count.items(),key=operator.itemgetter(0))

username = [i[0] for i in i_count]
value1 = [i[1] for i in i_count]
value2 = [i[1] for i in e_count]
error_info = zip(value1,value2)
final = list(zip(username,error_info))[:8]

for i,j in final:
    with open('user_statistics.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([i,j[0],j[1]])      