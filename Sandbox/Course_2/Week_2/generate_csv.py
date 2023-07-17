import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

def generate_csv():
    with open('hosts.csv', 'w') as hosts_csv:
        writer = csv.writer(hosts_csv)
        writer.writerows(hosts)

generate_csv()