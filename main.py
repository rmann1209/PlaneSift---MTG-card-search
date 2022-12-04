import os
import sys
sys.setrecursionlimit(100000)
print(sys.getrecursionlimit())

class Card:
    def __init__(self, name, cmc, color, typ, supTyp, subTyp, rarity, text, power, tough, url):
        self.name = name
        self.supTyp = supTyp
        self.typ = typ
        self.subTyp = subTyp
        self.power = power
        self.tough = tough
        self.color = color
        self.cmc = cmc
        self.text = text
        self.rarity = rarity
        self.url = url

    def printCard(self):
        print(self.name + " | " + self.typ + " | P/T = " + str(self.power) + " " + str(self.tough))
    
    
def printArray(array):
    for i in array:
        print(i.name + " | " + i.typ + " | " + i.color + " | P/T = " + str(i.power) + " " + str(i.tough))

def printPower(array):
    for i in array:
        print(str(i.power))

def printTough(array):
    for i in array:
        print(str(i.tough))

def printCMC(array):
    for i in array:
        print(str(i.cmc))

def printColor(array):
    for i in array:
        print(str(i.color))

def printSupType(array):
    for i in array:
        print(str(i.supTyp))

def printType(array):
    for i in array:
        print(str(i.typ))

def printSubType(array):
    for i in array:
        print(str(i.subTyp))

#Used in quicksort to find partition position

#search_tags is dictionary or search parameters, sort type = merge or quick, array is all Cards to be sorted
# def findCards(search_tags, sort_type, array):
#     searchSuptype(array, search_tags["superType"])
#     searchType(array, searchTags["type"])

#supArr is list of strings containing super types (ie "Legendary", "Basic", "Snow", etc)


def searchType(array, typeArr):
    index = 0
    count = 0
    size = array.__len__()
    deleted = False

    while count != size:

        for i in typeArr:
            if i.lower() not in array[index].typ.lower():
                del array[index]
                deleted = True
                break

        if(not deleted):
            index += 1
        deleted = False
        count += 1

#subArr is list of strings containing desired subtypes (ie "human", "soldier", etc)
def searchSubType(array, subArr):
    index = 0
    count = 0
    size = array.__len__()
    deleted = False

    while count != size:

        for i in subArr:
            if i.lower() not in array[index].subTyp.lower():
                del array[index]
                deleted = True
                break

        if(not deleted):
            index += 1
        deleted = False
        count += 1

#pass array as reference, c is color  letter as string (ie "W", "R", "G", "U", "B")
def searchColor(array, c):
    index = 0
    count = 0
    size = array.__len__()

    while count != size:
        if c.lower() not in array[index].color.lower():
            del array[index]
        else:
            index += 1
        count += 1

#rar is string containing rarity ("common", "uncommon", "rare", "mythic")
def searchRarity(array, rar):
    index = 0
    count = 0
    size = array.__len__()

    while count != size:
        if rar.lower() not in array[index].rarity.lower():
            del array[index]
        else:
            index += 1
        count += 1

#sorted array, txtArr is list of keywords to check for
def searchText(array, txtArr):
    index = 0
    count = 0
    size = array.__len__()
    deleted = False

    while count != size:

        for i in txtArr:
            if i.lower() not in array[index].txt.lower():
                del array[index]
                deleted = True
                break

        if(not deleted):
            index += 1
        deleted = False
        count += 1

#THE ARRAY PASSED HERE SHOULD BE ALL CREATURES, NOT ALL CARDS
#min = lowest val, max = highest val (inclusive)
#sortType = "quick" for quicksort, or "merge" for merge sort
def searchPower(array, min, max, sortType):
    if(sortType == "quick"):
        quickSort(array, 0, allCreatures.__len__()-1, "power")
    else:
        mergeSort(array, "power")
    
    index = 0
    #first, delete all powers that are too small
    while int(array[index].power) < min:
        del array[index]
    #find the last index of the max power allowed
    while int(array[index].power) <= max:
        index += 1
    del array[index:] #should delete all indices after index, inclusive
    
#THE ARRAY PASSED HERE SHOULD BE ALL CREATURES, NOT ALL CARDS
#min = lowest val, max = highest val (inclusive)
#sortType = "quick" for quicksort, or "merge" for merge sort
def searchTough(array, min, max, sortType):
    if(sortType == "quick"):
        quickSort(array, 0, allCreatures.__len__()-1, "tough")
    else:
        mergeSort(array, "tough")
    
    index = 0
    #first, delete all powers that are too small
    while int(array[index].tough) < min:
        del array[index]
    #find the last index of the max power allowed
    while int(array[index].tough) <= max:
        index += 1
    del array[index:] #should delete all indices after index, inclusive
        
#min = lowest val, max = highest val (inclusive)
#sortType = "quick" for quicksort, or "merge" for merge sort

#***************************START OF MAIN************************************

file = open("cardspipetest.txt",encoding="utf-8");
count = 0
lineCount = 0
cards = [] #Stores each variable needed to make a new card object, gets reset afterwards

allCards = [] #this will hold every card, will NOT change throughout course of program (after reading in completes)
allCreatures = [] #this will hold every CREATURE CARD (use if searching for creatures)

#read in all cards and save to respective arrays
for line in file:
    lineCount += 1
    #temp will always have newest line
    temp = []
    temp += (line.split("@"))

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

    #if no URL, the card is a duplicate
    if (url == "" or url == "\n"):
        cards.clear()
        continue
    
    temp = ""

    #In order to prevent typ from storing redundant info, such as "creature - Human Soldier" -> "creature"
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

    #Create card object
    card = Card(name, cmc, color, typ, supTyp, subTyp, rarity, text, power, tough, url)

    #Add card to array
    allCards.append(card)
    # allCards[count].print()
    # print("")

    #if card type is creature, add to creature array
    if(typ.__contains__("creature") and power.isnumeric() and tough.isnumeric()):
        allCreatures.append(card)

    count += 1
    cards.clear()


print("Total Cards Added: " + str(allCards.__len__()))
print("Total Creature Cards Added: " + str(allCreatures.__len__()))

#**********************************END OF FILE READ IN*******************************

#printArray(allCreatures)

quickSort(allCreatures, 0, allCreatures.__len__()-1, "power")
print("")
print("***************AFTER QUICK SORTING***********************")
print("")
printPower(allCreatures)

mergeSort(allCreatures, "power")
print("")
print("***************AFTER MERGE SORTING***********************")
print("")
printPower(allCreatures)

# sortedArray = allCards #Will start will all cards and progressively get smaller
# # printArray(sortedArray)

# print("\n**************PERFORMING SUPTYPE SORT**************\n")
# searchSupType(sortedArray, "Legendary")
# printSupType(sortedArray)

# print("\n**************PERFORMING TYPE SORT**************\n")
# searchType(sortedArray, "creature")
# printType(sortedArray)

def get_noncreature_types(all_cards):
    from tqdm import tqdm
    # creature = allCreatures[0]
    all_noncreature_types = set()
    for noncreature in tqdm(allCards):
        types = noncreature.subTyp.replace("'", "").split(" ")
        for t in types:
            all_noncreature_types.add(''.join(filter(str.isalnum, t)))

    return all_noncreature_types

def get_creature_types(all_creatures):
    from tqdm import tqdm
    # creature = allCreatures[0]
    all_creature_types = set()
    for creature in tqdm(allCreatures):
        types = creature.subTyp.replace("'", "").split(" ")
        for t in types:
            all_creature_types.add(''.join(filter(str.isalnum, t)))
    for item in ["", "Island", "of"]:
        all_creature_types.remove(item)

    return all_creature_types

creatureSubtypes = get_creature_types(allCreatures)
allSubtypes = get_noncreature_types(allCards)
print(allSubtypes - creatureSubtypes)

# print("\n**************FINAL RESULTS**************\n")
# printArray(sortedArray)
