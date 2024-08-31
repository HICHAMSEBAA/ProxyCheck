#!/home/hicham/Hicham/Python/ProxyCheck/venv/bin/python3

import requests
from requests.exceptions import ProxyError, SSLError, ConnectionError, ConnectTimeout, RequestException
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from colored import fg, attr

# Function to check which protocols (http, https, socks4, socks5) are supported by a proxy
def check_protocol_support(proxy):
    # protocols = ["http", "https", "socks4", "socks5"]
    protocols = ["http"]
    supported_protocols = []
    
    # Loop through each protocol and attempt a connection to Google using the proxy
    for protocol in protocols:
        proxies = {
            "http": f"{protocol}://{proxy}",
            "https": f"{protocol}://{proxy}"
        }
        try:
            # Send a request to Google using the proxy
            response = requests.get("https://www.google.com", proxies=proxies, timeout=10)
            if response.status_code == 200:
                # If the response is successful, add the protocol to the list of supported protocols
                supported_protocols.append(protocol)
                print(f"{fg('green')}Proxy {proxy} supports {protocol.upper()} protocol.{attr('reset')}")
            else:
                # If the status code is not 200, report that the protocol is not supported
                print(f"{fg('yellow')}Proxy {proxy} does not support {protocol.upper()} protocol (status code: {response.status_code}).{attr('reset')}")
        
        except (ProxyError, SSLError, ConnectionError, ConnectTimeout):
            # Handle errors related to proxy connections and report that the protocol is not supported
            print(f"{fg('red')}Proxy {proxy} does not support {protocol.upper()} protocol.{attr('reset')}")
    
    return supported_protocols

# Function to get the geolocation of an IP address using the ipinfo.io API
def get_geolocation(ip):
    url = f"http://ipinfo.io/{ip}/json"
    try:
        start_time = time.time()
        response = requests.get(url)
        latency = time.time() - start_time
        data = response.json()
        
        # Extract and print location information from the API response
        country = data.get("country")
        region = data.get("region")
        city = data.get("city")
        loc = data.get("loc")
        
        print(f"{fg('green')}(Latency: {latency:.4f}s) IP: {ip} | Country: {country}, Region: {region}, City: {city}, Coordinates: {loc}{attr('reset')}")
        return country, region, city, loc
    
    except RequestException as e:
        # Handle any errors during the API request
        print(f"{fg('red')}Error fetching geolocation data for IP {ip}: {e}{attr('reset')}")
        return None, None, None, None

# Function to load a list of proxies from a file
def load_proxies(file_path):
    with open(file_path, 'r') as file:
        # Read the proxies from the file and return them as a list
        proxies = [line.strip() for line in file.readlines()]
    return proxies

# Function to test if a proxy is working by sending a request to httpbin.org
def test_proxy(proxy):
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        start_time = time.time()
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
        latency = time.time() - start_time
        
        if response.status_code == 200:
            # If the proxy works, print the latency and the IP address returned by the server
            ip = response.json().get("origin")
            print(f"{fg('green')}(Latency: {latency:.4f}s) Proxy {proxy} is working. IP: {ip}{attr('reset')}")
            return True
        else:
            # If the status code is not 200, report that the proxy did not work as expected
            print(f"{fg('yellow')}(Latency: {latency:.4f}s) Proxy {proxy} returned status code: {response.status_code}{attr('reset')}")
            return False
    
    except (ProxyError, ConnectTimeout, RequestException) as e:
        # Handle any errors during the proxy testing
        print(f"{fg('red')}Proxy {proxy} encountered an error: {e}{attr('reset')}")
        return False

# Function to process a proxy by getting its geolocation, checking its protocol support, and testing it
def process_proxy(proxy):
    ip = proxy.split(':')[0]
    get_geolocation(ip)
    check_protocol_support(proxy)
    return test_proxy(proxy)

def main():
    # Print a welcome message with colored ASCII art
    print(f"""{fg('yellow')}
 _   _ _      _                       _____      _                 
| | | (_)    | |                     /  ___|    | |                
| |_| |_  ___| |__   __ _ _ __ ___   \ `--.  ___| |__   __ _  __ _ 
|  _  | |/ __| '_ \ / _` | '_ ` _ \   `--. \/ _ \ '_ \ / _` |/ _` |
| | | | | (__| | | | (_| | | | | | | /\__/ /  __/ |_) | (_| | (_| |
\_| |_/_|\___|_| |_|\__,_|_| |_| |_| \____/ \___|_.__/ \__,_|\__,_|
                                                                   
                                                                   
______                      _____ _               _                
| ___ \                    /  __ \ |             | |               
| |_/ / __ _____  ___   _  | /  \/ |__   ___  ___| | _____ _ __    
|  __/ '__/ _ \ \/ / | | | | |   | '_ \ / _ \/ __| |/ / _ \ '__|   
| |  | | | (_) >  <| |_| | | \__/\ | | |  __/ (__|   <  __/ |      
\_|  |_|  \___/_/\_\\__, |  \____/_| |_|\___|\___|_|\_\___|_|      
                     __/ |                                         
                    |___/                                          
          {attr('reset')}""")
    print(f"{fg('yellow')}Wolcome To The Hicham Sebaa Proxy checker {attr('reset')}")

    is_working = 0
    not_working = 0
    
    # Load the list of proxies from a file
    proxy_file = 'proxy_list.txt'
    proxies = load_proxies(proxy_file)
    
    # Use a ThreadPoolExecutor to process proxies concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_proxy = {executor.submit(process_proxy, proxy): proxy for proxy in proxies}
        
        # As each future completes, check if the proxy was working or not
        for future in as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            try:
                if future.result():
                    is_working += 1
                else:
                    not_working += 1
            except Exception as e:
                # Handle any errors that occur during proxy processing
                print(f"{fg('red')}Error processing proxy {proxy}: {e}{attr('reset')}")
    
    # Print a summary of the number of working and non-working proxies
    print(f"{fg('green')}{is_working}  Proxies are working{attr('reset')}")
    print(f"{fg('red')}{not_working} Proxies are not working{attr('reset')}")

if __name__ == "__main__":
    main()
