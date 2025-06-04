import shared_library
import json
import Agents
import OpenTickets
import ClosedTickets
import Organizations
import People
import scp
import cifs

# Configuration paramters
remote_hostname = "veeam.consys.it"
remote_hostip = "192.168.11.16"
remote_share = "Consys"
user = "user"
pwd = "Parampa1994!"
remote_path = 'DeskPro_Backup'
local_path = '/var/deskpro/Backup_files'

# Start backup procedures
Agents.get_data()
Organizations.get_data()
People.get_data()
OpenTickets.get_data()
ClosedTickets.get_data()
#scp.transfert_data(local_path, remote_path, remote_host, user, pwd)
cifs.transfert_data(local_path, remote_path, remote_hostname, remote_hostip, remote_share, user, pwd)
