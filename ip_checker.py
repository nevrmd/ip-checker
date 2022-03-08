import requests
from pyfiglet import Figlet
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
        print("")

    except Exception as e:
        print(f"[bold red]An '{e}' error occurred")

def main():
    print(Figlet().renderText("IP checker"))
    while True:
        print("[bold cyan]1 - Your [yellow]IP adress[/yellow];\n2 - Info about [yellow]any IP adress[/yellow]\n")
        try:
            choice = int(input(">>> "))
        except:
            print("[bold red]Type 1 or 2!")
        else:
            if choice == 1:
                url = "https://icanhazip.com/"
                response = requests.get(url).text
                print(f"[bold green]Your IP is [bold yellow]{response}")
            elif choice == 2:
                print("[cyan]Enter an IP that will be checked")
                try:
                    ip = input("IP: ")
                    info(ip)

                except Exception as e:
                    print(f"[bold red][ERROR] {e}")

if __name__ == "__main__":
    main()