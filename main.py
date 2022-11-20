from mimetypes import init
import csv

file = open("cards(pipe).txt", "r");
for line in file:
    cards = line.split("|")
    name = cards[0].toLowerCase()
    cmc = cards[1]
    color = cards[2]
    typ = cards[3]
    supTyp = cards[4]
    subTyp = cards[5].toLowerCase()
    rarity = cards[6]
    text = cards[7].toLowerCase()
    power = cards[8]
    tough = cards[9]
    url = cards[10]

    if (url == ""):
        continue

    temp = ""

    if (typ.__contains__("Artifact")):
        temp += "artifact "

    if (typ.__contains__("Creature")):
        temp += "creature "

    if (typ.__contains__("Enchantment")) :
        temp += "enchantment "

    if (typ.__contains__("Instant")) :
        temp += "instant "

    if (typ.__contains__("Land")) :
        temp += "land "

    if (typ.__contains__("Sorcery")) :
        temp += "sorcery "

    typ = temp
    temp = ""

    if(supTyp.contains("Legendary")):
        temp += "legendary "

    if(supTyp.contains("Basic")):
        temp += "basic "

    if(supTyp.contains("Snow")):
        temp += "snow "

    if(supTyp.contains("World")):
        temp += "world "

    subTyp = temp

    card = Card(name, cmc, color, typ, supTyp, subTyp, rarity, text, power, tough, url)
