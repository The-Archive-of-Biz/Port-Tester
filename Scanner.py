import logging
import requests
import time

# Define the target server and the range of ports to scan
target = 'http://portquiz.net/'
port_range = range(1, 65536)

# Set up logging
logging.basicConfig(filename='scan.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info(f'Log started for {target} on ports {port_range}')
print("start")
# Open a file to write the successful requests to
with open('successful_requests.txt', 'w') as f:
    # Loop through each port in the range and attempt to connect to the server
    for port in port_range:
        # Construct the URL for the current port
        url = f'{target}:{port}'
        # Attempt to make a GET request to the URL
        try:
            response = requests.get(url, timeout=1)
            # If the request is successful, write the port number to the file and log the success
            if response.status_code == 200:
                f.write(f'Successful connection to port {port}\n')
                logging.info(f'Successful connection to port {port}')
                print(f'Successful connection to port {port}')
        except:
            # If the request fails, log the failure
            logging.error(f'Connection to port {port} failed')
            print(f'unsuccessful connection to port {port}')
        # Add a delay of 1 seconds between each port scan
        time.sleep(1)
