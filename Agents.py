import shared_library
import json

####################################################
## AGENTS  #########################################
####################################################

def get_data():
    print("Get data for agents...")
    total_pages = shared_library.get_pages_number("/agents",100,"")

    existing_data = []
    for i in range(1,total_pages+1):
        new_data = shared_library.get_json_response_by_page("/agents",100,i) #new_data è un type dictionary
        existing_data.append(new_data["data"])
        print("got data of page:",i,"of: ",total_pages)

    # existing_data.append(new_data)
    with open("./Backup_files/Agents.json", "w") as json_file:
        json.dump(new_data, json_file, indent=4)
        print("Data saved in Agents.json file.")
    print("Agents data successfully retrived.")
    print("##################################\n")
