import subprocess
import re

def scan_wifi():
    result = subprocess.run(['sudo','iwlist','wlan0','scan'],stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')

    networks = re.findall(r'Cell \d+ - Address: (.*?)\n.*?ESSID:"(.*?)".*?Signallevel=(-\d+) dBm',output, re.DOTALL)

    wifi_list = []

    for network in networks:
        mac_address, ssid, signal_strength = network
        signal_strength = int(signal_strength)

    #convert dBM to percentage (this is an appoximation)
        signal_percentage = max(0,min(100,2*(signal_strength+100)))

        wifi_list.append({
            'SSID' : ssid,
            'MAC Address' : mac_address,
            'Signal Strength (dBm)' : signal_strength,
            'Signal Strength (%)' : signal_percentage
        })

    return wifi_list

def display_wifi(networks):
    print("Available Wi-Fi Networks: ")
    for network in networks:
        print(f"SSID:{network['SSID']},MAC:{network['MAC Address']},Signal Strength: {network['Signal Strength (%)']}%")

if __name__ == "__main__":
    networks = scan_wifi()
    display_wifi(networks)