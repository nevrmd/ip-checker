import requests
from rich import print

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

    except:
        print("ann error occurred")

def main():
    ip = input("IP: ")
    info(ip)

if __name__ == "__main__":
    main()