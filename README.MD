# Port Scanner

This Python script is a simple port scanner that attempts to make a connection to a specified target server over a range of port numbers. It utilizes the `requests` library to send HTTP GET requests to the server and logs the results.

## Features

- Scans a range of port numbers on a specified target server.
- Logs successful and unsuccessful connection attempts.
- Outputs a list of successful connections to a text file.

## Usage

1. Make sure you have Python installed on your system.
2. Install the `requests` library if it is not already installed. You can do this using pip:
   ```bash
   pip install requests```
3. Clone the repository to your local machine:
4. Modify the target and port_range variables to specify the target server and the range of ports you want to scan. By default, the script is set to scan all 65,535 ports.
```python
    target = 'http://portquiz.net/'  # Change this to your target server
    port_range = range(1, 65536)    # Specify the port range to scan
```
5. Run the script using the following command:
```bash
python port_scanner.py
```
## Output
The script will create a log file named scan.log where it records information about successful and unsuccessful connection attempts.

Successful connection attempts will also be displayed in the console.

A text file named successful_requests.txt will be generated, listing the ports to which a successful connection was made.

## Example
```bash
python port_scanner.py
```
Output:
```bash
start
Successful connection to port 80
Successful connection to port 8080
unsuccessful connection to port 25
...
```
## Note
This script is designed for educational purposes and should only be used on systems and servers for which you have explicit permission to scan ports. Unauthorized port scanning can potentially violate the law and terms of service of your internet service provider.

Be responsible and ethical when using this script.