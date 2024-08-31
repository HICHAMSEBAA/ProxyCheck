
# Proxy Checker

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/github/license/HICHAMSEBAA/ProxyChecker)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## Overview

Welcome to the **Proxy Checker**! This tool allows you to efficiently test proxy servers for protocol support, validate their functionality, and retrieve geolocation information for each proxy. Built using Python and utilizing the `requests` library, this script is designed to handle multiple proxies concurrently, making it fast and efficient.

## Features

- **Protocol Support Check**: Verifies if a proxy supports `http`, `https`, `socks4`, and `socks5` protocols.
- **Geolocation Retrieval**: Fetches and displays the country, region, city, and coordinates of the IP address associated with the proxy.
- **Proxy Validation**: Checks if the proxy is functional by making an actual request and measuring the latency.
- **Concurrency**: Uses `ThreadPoolExecutor` to handle multiple proxies simultaneously, speeding up the process.

## Requirements

- Python 3.x
- `requests` library
- `colored` library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/HICHAMSEBAA/ProxyChecker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ProxyChecker
    ```

3. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your proxy list:

    - Create a file named `proxy_list.txt` in the root directory of the project.
    - Add your proxies in the following format, one per line:

      ```
      123.123.123.123:8080
      124.124.124.124:9090
      ```

2. Run the proxy checker:

    ```bash
    ./venv/bin/python3 proxy_checker.py
    ```

3. The script will display the results in the terminal, including protocol support, geolocation details, and whether each proxy is working.

## Example Output

```
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
Welcome To The Hicham Sebaa Proxy Checker

(Latency: 0.1234s) Proxy 123.123.123.123:8080 is working. IP: 123.123.123.123
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. All contributions are welcome!

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: h_sebaa@ensta.edu.dz
- **GitHub**: [HICHAMSEBAA](https://github.com/HICHAMSEBAA)
