from bs4 import BeautifulSoup

# could request the webpage directly, but then I'd need my session cookie, or use mechanize and use my pw
soup = BeautifulSoup(open("tengelmann200's account.html"), "lxml")
rows = soup.find_all("tr", "wallet_table_row")

def valid_row(row):
    item = row.find("td", "wht_items").contents[0]
    wallet = "Wallet Credit" in item
    market = "Steam Community Market" in item
    return not any([wallet, market])
    
# filter rows that are about purchased wallet credit and things sold on market since I'm only interested in how much money I actually spent on games
valid = filter(valid_row, rows)
# do some string manipulation and convert all the totals to float
totals = map(float,
             map(lambda t: t.replace("\t", "").replace("\n", "").replace(",", ".")[:-1],
                 [row.find("td", "wht_total").contents[0] for row in valid]))

# the approx. total of all money spent on steam games 
total = sum(totals)

print(total)
