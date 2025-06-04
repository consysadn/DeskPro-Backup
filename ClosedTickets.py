import shared_library
import json

####################################################
# CLOSED TT ########################################
####################################################
def get_data():
    print("Get data for resolved Tickets.")
    total_pages = shared_library.get_pages_number("/tickets",500,"&status=resolved")
    existing_data = []
    for i in range(1,total_pages+1):
        new_data = shared_library.get_json_response_by_page("/tickets",500,i,"&status=resolved") #new_data è un type dictionary
        existing_data.append(new_data["data"])
        print("got data page: ",str(i),"of: ",str(total_pages))

    with open("./Backup_files/ClosedTickets.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=4)
    print("Data saved in ClosedTickets.json file.")

####################################################
## GET MESSAGES FROM Open Tickets ##################
####################################################
    existing_data_messages = []
    for item in existing_data[0]: # ciclo su tutti gli id degli open tickets
        ticket_id = item.get('id')
        messages_url = "/tickets/" + str(ticket_id) + "/messages" # costruisco la stringa per la chiamata dei messages /api/v2/tickets/<id>/messages
        total_pages = shared_library.get_pages_number(messages_url,100)
        for i in range(1,total_pages+1):  # faccio una chiamata per ogni id per prendere i messaggi (con gestione del paging)
            new_data = shared_library.get_json_response_by_page(messages_url,100,i) #new_data è un type dictionary
            existing_data_messages.append(new_data["data"]) # nella var dirctionary existing_data_messages ci sono i messaggi
            print("got messages for id:", str(ticket_id), "page:", str(i), "of: ", str(total_pages), "pages.") #salvo i messaggi nel file
    with open("./Backup_files/ClosedTickets_messages.json", "w") as json_file:
        json.dump(existing_data_messages, json_file, indent=4)
    print("Data saved in ClosedTickets_messages.json file.")
    print("###############################################\n")

