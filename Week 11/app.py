import requests
from bs4 import BeautifulSoup
import csv

car = input("Enter manufacturer name: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com"
}

url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
response = requests.get(url, headers=headers)

# function to save data to csv file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Car Name", "Price"])   # header row
        for row in data:
            writer.writerow(row)
    print(f"Data saved to {filename}")

# scrape and collect data
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')

    all_data = []   # list to store all car data

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                name  = cols[0].get_text(strip=True)
                price = cols[1].get_text(strip=True)
                print(f"Car Name: {name} - Price: {price}")
                all_data.append([name, price])  # add to list

    # save collected data to CSV
    if all_data:
        save_to_csv(all_data, f"{car}_prices.csv")
    else:
        print("No data found for this manufacturer.")

else:
    print("Page not available!")