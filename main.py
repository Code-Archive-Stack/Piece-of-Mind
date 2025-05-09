import psutil
import time
import IP2Location
from rich.console import Console
from rich.table import Table 
from splunklib.binding import HTTPError
from splunklib.client import Service
import os 

database = IP2Location.IP2Location('/home/ai/Documents/Detection projects/IP2LOCATION-LITE-DB11.CSV/IP2LOCATION-LITE-DB11.BIN')


# def WriteToSplunk():

#     splunk_host = 'localhost'
#     splunk_port = 8080
#     splunk_username = 'admin'
#     splunk_password = '<password>'

#     serivice = Service(host = splunk_host, port = splunk_port, username= splunk_username, password = splunk_password)

#     log_event = {
#     'time': 1643723400,  # Unix timestamp c8e240a7-c737-49fd-8577-b94f7c107f9f
#     'host': 'localhost',
#     'source': 'python_logger',
#     'sourcetype': 'log',
#     'index': 'main',
#     'event': {
#         'message': 'This is a test log event'
#     }
# }

#     try:
#         serivice.indexes(log_event)
#         print('Log event sent successfully')
#     except HTTPError as e:
#         print(f'Erro sendiong log event: {e}')



def GeoIP_check(IP):
    
    IP_info = database.get_all(IP)
    timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
    country_name = IP_info.country_long
    region =  IP_info.region
    latitude = IP_info.latitude
    longitude = IP_info.longitude
    
    data = (
        {"Timestamp":timestamp,
         "IP":IP,
         "Country":country_name,
         "Region":region,
         "Latitude":latitude,
         "Longtitude":longitude
         }
    )
    
    print(data)


def display_connection():

    while True:
        # Clear the console
        print("\033c", end="")

        connections = psutil.net_connections(kind='tcp')

        "limit how many rows you want to see"
        # print(f"{'Local Address': <30} {'Remote Address': <30} {'Status': <15}")
        # print("=" * 75)

        for con in connections:
            local_addr = f"{con.laddr.ip}:{con.laddr.port}"
            # Check if there is a remote address
            if con.raddr:
                remote_addr = f"{con.raddr.ip}:{con.raddr.port}"
                remote_ip = f"{con.raddr.ip}"
                GeoIP_check(remote_ip)
            
            else:
                remote_addr = "N/A"  # No remote address for listening sockets
            status = con.status

            # print(f"found {local_addr:<30} {remote_addr:<30} {status:<15}")

            if remote_addr == "N/A":
                print("\nnot found")
            
        time.sleep(5)

if __name__ == "__main__":
    print("start")
    # WriteToSplunk()
    display_connection()
    
