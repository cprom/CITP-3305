import csv


#def read_csv_dict():
 #   with open('sofware.csv') as software:
  #      reader = csv.DictReader(software)
   #     for row in reader:
    #        print(("{} has {} user".format(row["name"], row["users"])))


users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, {"name": "Charlie Grey", "username": "grecy", "department": "Development"}]
keys = ["name", "username", "department"]
def generate_dict():
    with open('by_department.csv', 'w') as by_department:
        writer = csv.DictWriter(by_department, fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)

generate_dict()