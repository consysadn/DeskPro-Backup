import paramiko
import os
from smb.SMBConnection import SMBConnection

def transfert_data(_local_path, _remote_path, _remote_hostname, _remote_hostip, _remote_share, _user, _pwd):
    print("Start copiyng json files from " + _local_path + " to " + _remote_hostname + '\\' + _remote_share + '\\' + _remote_path)

    try:
        conn = SMBConnection(_user, _pwd, '', _remote_hostname, use_ntlm_v2=True, is_direct_tcp=True)
        conn.connect(_remote_hostip, 445)
        status = conn.auth_result

        for _filename in os.listdir(_local_path):
            if _filename.endswith(".json"):
                # Prints only text file present in My Folder
                _local_item = _local_path + '/' + _filename
                _remote_item = _remote_path +'\\' + _filename
                print(_filename," - ", _local_item, ' - ', _remote_item)
                with open(_local_item, 'rb', buffering=0) as file_obj:
                    conn.storeFile(_remote_share, _remote_item, file_obj)
                file_obj.closed
        print("CONNECTION Status:",status)
    except:
        conn.close()
        print("CONNECTION FAILED")

    conn.close()
