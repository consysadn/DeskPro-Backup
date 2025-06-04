import shared_library
import json

####################################################
## PEOPLE  #########################################
####################################################
def get_data():
    print("Get data for people.")
    total_pages = shared_library.get_pages_number("/people",100,"")
    existing_data = []
    for i in range(1,total_pages+1):
        new_data = shared_library.get_json_response_by_page("/people",100,i) #new_data è un type dictionary
        existing_data.append(new_data["data"])
        print("got data of page:",i,"of: ",total_pages)

    with open("./Backup_files/People.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)
        print("Data saved in People.json file.")
    print("###############################\n")
