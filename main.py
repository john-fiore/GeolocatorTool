import os, sys
import requests
from colorama import Fore as col

clear = lambda: os.system('cls')


def get_location():
    try:
        ipdata = requests.get("https://ipinfo.io/json", timeout=5).json()

        city = ipdata.get('city', 'Unknown')
        region = ipdata.get('region')
        country = ipdata.get('country', 'Unknown')
        ip = ipdata.get('ip', 'Unknown')
        postal = ipdata.get('postal', '')
        timezone = ipdata.get('timezone', 'Unknown')

        clear()

        if region:
            print(f"{col.GREEN}Location:{col.RESET} {city}, {region}, {country} {postal}")
        else:
            print(f"{col.GREEN}Location:{col.RESET} {city}, {country} {postal}")

        print(f"{col.GREEN}IP:{col.RESET} {ip}")
        print(f"{col.GREEN}Timezone:{col.RESET} {timezone}")
        print()
        cont = input("Enter 'Y' to restart and 'N' to exit: ").upper()

        if cont == "Y":
            clear()
            main()
        else:
            sys.exit(0)

    except requests.RequestException:
        print("Failed to fetch IP information.")

def main():
    print("Welcome.")
    print()
    print("This tool will simply give you your current location, including")
    print("your city, state/province (if applicable), country, and IP. This")
    print("tool is not for commercial use, and is merely an app I developed")
    print(f"to test using the {col.YELLOW}requests library{col.RESET} with the {col.BLUE}ipinfo API{col.RESET}.")
    print()
    print(f"{col.RED}Please Note:{col.RESET} this app does NOT collect any information regarding")
    print("your location or IP - only you'll be able to see it.")
    print()
    input("Press ENTER to start.")
    
    clear()
    print("Fetching data...")
    get_location()

if __name__ == "__main__":
    main()