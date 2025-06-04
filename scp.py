import paramiko
import os

def transfert_data(_local_path,_remote_path,_remote_host,_user,_pwd):
    print("Start copiyng json files from " + _local_path + " to " + _remote_host + "/" + _remote_path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(_remote_host, username=_user, password=_pwd)# SCP command
    scp = paramiko.SFTPClient.from_transport(ssh.get_transport())# Define remote and local paths
    for _filename in os.listdir(_local_path):
        if _filename.endswith(".json"):
            # Prints only text file present in My Folder
            _local_item = _local_path + '/' + _filename
            _remote_item = _remote_path +'/' + _filename
            print(_filename," - ", _local_item, ' - ', _remote_item)
            scp.put(_local_item, _remote_item)# Start copy process
    scp.close()
    ssh.close()
    print("Files have been copied successfully from " + _local_path + " to " + _remote_host + "/" + _remote_path)
