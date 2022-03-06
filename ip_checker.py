import requests
import pyfiglet
import sys
from rich import print

sys.tracebacklimit = 0

def info(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        
        data = {
            "IP": response.get("query"),
            "Country": response.get("country"),
            "Region": response.get("regionName"),
            "City": response.get("city"),
            "Zip-code": response.get("zip"),
            "Lat": response.get("lat"),
            "Long": response.get("lon"),
            "Timezone": response.get("timezone"),
            "Provider": response.get("isp"),
            "Organization": response.get("org")
        }

        for k, e in data.items():
            print(f"[bold cyan]{k}: [bold yellow]{e}")

    except Exception as e:
        print(f"[bold red]An '{e}' error occurred")

def main():
    print(pyfiglet.figlet_format("IP CHECKER"))
    print("[cyan]Enter an IP that will be checked")
    try:
        ip = int(input("IP: "))
        info(ip)

    except Exception as e:
        print(f"[bold red][ERROR] {e}")

if __name__ == "__main__":
    main()