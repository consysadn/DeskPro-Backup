import shared_library
import json

####################################################
## ORGANIZATIONS####################################
####################################################

def get_data():
    print("Get data for Organizations."
    total_pages = shared_library.get_pages_number("/organizations",100,"")
    existing_data = []
    for i in range(1,total_pages+1):
        new_data = shared_library.get_json_response_by_page("/organizations",100,i) #new_data è un type dictionary
        existing_data.append(new_data["data"])
        print("got data of page:",i,"of: ",total_pages)

    with open("./Backup_files/Organizations.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)
        print("Data saved in Organizations.json file.")
    print("######################################\n")
