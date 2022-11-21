import os

class Card:
    def __init__(self, name, super, type, sub, power, tough, color, cmc, text, rarity, url):
        self.name = name;
        self.super = super;
        self.type = type;
        self.sub = sub;
        self.power = power;
        self.tough = tough;
        self.color = color;
        self.cmc = cmc;
        self.text = text;
        self.rarity = rarity;
        self.url = url;

    def print(self):
        print(self.name + " " + str(self.power));


file = open("cardspipe.txt", "r");
count = 0
cards = []
for line in file:
    #temp will always have newest line
    temp = []
    temp += (line.split("|"))

    #If true (cards size is zero), new card is being added
    if(cards.__len__() == 0):
        cards += temp
    #otherwise, we know lines were split
    else:
        #append first index of new temp to last index of cards
        cards[cards.__len__()-1] += temp[0]
        del temp[0]
        cards += temp
         
    # print(cards.__len__()) #USED FOR TESTING

    if(cards.__len__() != 11):

        continue
        # moreCards = file.readline.split("|")
        # cards += moreCards 

    
    name = cards[0]
    cmc = cards[1]
    color = cards[2]
    typ = cards[3]
    supTyp = cards[4]
    subTyp = cards[5]
    rarity = cards[6]
    text = cards[7]
    power = cards[8]
    tough = cards[9]
    url = cards[10]
    print(cards)

    if (url == ""):
        cards.clear()
        continue
    
    # temp = ""

    # if (typ.__contains__("Artifact")):
    #     temp += "artifact "

    # if (typ.__contains__("Creature")):
    #     temp += "creature "

    # if (typ.__contains__("Enchantment")) :
    #     temp += "enchantment "

    # if (typ.__contains__("Instant")) :
    #     temp += "instant "

    # if (typ.__contains__("Land")) :
    #     temp += "land "

    # if (typ.__contains__("Sorcery")) :
    #     temp += "sorcery "

    # typ = temp
    # temp = ""

    # if(supTyp.contains("Legendary")):
    #     temp += "legendary "

    # if(supTyp.contains("Basic")):
    #     temp += "basic "

    # if(supTyp.contains("Snow")):
    #     temp += "snow "

    # if(supTyp.contains("World")):
    #     temp += "world "

    # subTyp = temp

    card = Card(name, cmc, color, typ, supTyp, subTyp, rarity, text, power, tough, url)
    print("")
    count += 1
    cards.clear()

print("Cards added: " + str(count))

    
