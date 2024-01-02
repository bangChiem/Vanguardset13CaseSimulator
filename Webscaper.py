from bs4 import BeautifulSoup

class vanguardCard:
    def __init__(self, price, name, rarity):
        self.name = name
        self.rarity = rarity
        self.price = price

    def appendToRarityLists(self):
        if(self.rarity == "C"):
            c.append(self)
        elif(self.rarity == "RR"):
            rr.append(self)
        elif(self.rarity == "RRR"):
            rrr.append(self)
        elif(self.rarity == "RE"):
            re.append(self)
        elif(self.rarity == "FFR"):
            ffr.append(self)
        elif(self.rarity == "ORRR"):
            orrr.append(self)

    def __str__(self):
        return f"{self.name}, {self.rarity}, {self.price}"
    
c = []
rr = []
rrr = []
re = []
ffr= []
orrr = []
SpecialRarity = []

#Record every card on webpage storing card name, price, and rarity into Vanguardcard object
def read_webpage_to_card(webpage_link):
    #read webpageinfo
    with open(webpage_link, 'r') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')
        cards = soup.find_all('section', class_ = "search-result__product search-result__product__add-to-cart")

    #sort info into Vanguardcard object
        for card in cards:
            name = card.select_one("span.search-result__title").contents
            try:
                price = card.select_one("span.search-result__market-price--value").contents
            except:
                price = card.select_one("span.inventory__price-with-shipping").contents
            rarity = card.span.contents
            van_card = vanguardCard(price, name, rarity)
            c.append(van_card)

for n in range(1,9):
    read_webpage_to_card(f"Set13Pg{n}.html")
    print(n)


read_webpage_to_card("Set13Pg8.html")

for cards in c:
    print(cards)