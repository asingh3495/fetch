
import yaml
import requests
import time
from collections import defaultdict



def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


# Function to perform health checks
def check_health(endpoint):
    url = endpoint['url']
    method = endpoint.get('method')
    headers = endpoint.get('headers')
    body = endpoint.get('body')
    print("url=",url)
    print("method=",method)
    print("headers=",headers,'\n',"body=",body)

    try:
        response = requests.request(method, url, headers=headers, json=body)
        if 200 <= response.status_code < 300:
            print("UP")
            return "UP"
        else:
            print("DOWN")
            return "DOWN"
    except requests.RequestException:
        return "DOWN"


def monitor_endpoints(file_path):
    config = load_config(file_path)
    domain_stats = defaultdict(lambda: {"up": 0, "total": 0})

    while True:
        for endpoint in config:
            print('endpoint',endpoint)
            domain = endpoint["url"].split("//")[-1].split("/")[0]
            print("domain", domain)
            result = check_health(endpoint)

            domain_stats[domain]["total"] += 1
            if result == "UP":
                domain_stats[domain]["up"] += 1
            print("domain_stats",domain_stats)

        # Log cumulative availability percentages
        for domain, stats in domain_stats.items():
            availability = round(100 * stats["up"] / stats["total"])
            print(f"{domain} has {availability}% availability percentage")

        print("---")
        time.sleep(15)


# Entry point of the program
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python monitor.py <config_file_path>")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        monitor_endpoints(config_file)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")