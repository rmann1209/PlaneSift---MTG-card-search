import os

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

    def __str__(self):
        return self.name + " | " + self.typ + f" | Power: {str(self.power)} | Toughness: {str(self.tough)}"
    
def printArray(array):
    for i in array:
        print(i.name + " | " + i.typ + " | P/T = " + str(i.power) + " " + str(i.tough))

def printPower(array):
    for i in array:
        print(str(i.power))

def printTough(array):
    for i in array:
        print(str(i.tough))

def printCMC(array):
    for i in array:
        print(str(i.cmc))

#Used in quicksort to find partition position
def partition(array, low, high, str):
    if(str == "power"):
        pivot = int(array[low].power) #pivot starts at leftmost position
        up = low
        down = high

        #while up index is to the left of down index
        while(up < down):
            for j in range(up, high):
                if(int(array[up].power) > pivot):
                    break
                up += 1
            
            for j in range(high, low, -1):
                if(int(array[down].power) < pivot):
                    break
                down -= 1
            
            if(up < down):
                temp = array[up]
                array[up] = array[down]
                array[down] = temp
        temp = array[low]
        array[low] = array[down]
        array[down] = temp
        return down
    elif(str == "tough"):
        pivot = int(array[low].tough) #pivot starts at leftmost position
        up = low
        down = high

        #while up index is to the left of down index
        while(up < down):
            for j in range(up, high):
                if(int(array[up].tough) > pivot):
                    break
                up += 1
            
            for j in range(high, low, -1):
                if(int(array[down].tough) < pivot):
                    break
                down -= 1
            
            if(up < down):
                temp = array[up]
                array[up] = array[down]
                array[down] = temp
        temp = array[low]
        array[low] = array[down]
        array[down] = temp
        return down
    elif(str == "cmc"):
        pivot = int(array[low].cmc) #pivot starts at leftmost position
        up = low
        down = high

        #while up index is to the left of down index
        while(up < down):
            for j in range(up, high):
                if(int(array[up].cmc) > pivot):
                    break
                up += 1
            
            for j in range(high, low, -1):
                if(int(array[down].cmc) < pivot):
                    break
                down -= 1
            
            if(up < down):
                temp = array[up]
                array[up] = array[down]
                array[down] = temp
        temp = array[low]
        array[low] = array[down]
        array[down] = temp
        return down


def quickSort(array, low, high, str):
    if(low < high):
        pivot = partition(array, low, high, str)
        quickSort(array, low, pivot - 1, str)
        quickSort(array, pivot + 1, high, str)
    
def mergeSort(cards, str):
    if (len(cards) > 1):
        #split the list in half
        middle = len(cards)//2
        left = cards[:middle]
        right = cards[middle:]

        #recursively call
        mergeSort(left, str)
        mergeSort(right, str)

        i = 0
        j = 0
        k = 0

        # check what sorting factor
        if (str == "power"):
            while i < len(left) and j < len(right):
                if (not (left[i].power).isnumeric()):
                    del left[i]
                    continue
                if (not (right[j].power).isnumeric()):
                    del right[j]
                    continue
                if (int(left[i].power) <= int(right[j].power)):
                    cards[k] = left[i]
                    i += 1
                else:
                    cards[k] = right[j]
                    j += 1
                
                k+= 1

            while j < len(right):
                cards[k] = right[j]
                j += 1
                k += 1

            while i < len(left):
                cards[k] = left[i]
                i += 1
                k += 1

        elif (str == "tough"):
            while i < len(left) and j < len(right):
                if (not (left[i].tough).isnumeric()):
                    del left[i]
                    continue
                if (not (right[j].tough).isnumeric()):
                    del right[j]
                    continue
                if (int(left[i].tough) <= int(right[j].tough)):
                    cards[k] = left[i]
                    i += 1
                else:
                    cards[k] = right[j]
                    j += 1
                
                k+= 1

            while j < len(right):
                cards[k] = right[j]
                j += 1
                k += 1

            while i < len(left):
                cards[k] = left[i]
                i += 1
                k += 1

        elif (str == "cmc"):
            while i < len(left) and j < len(right):
                if (not (left[i].cmc).isnumeric()):
                    del left[i]
                    continue
                if (not (right[j].cmc).isnumeric()):
                    del right[j]
                    continue
                if (int(left[i].cmc) <= int(right[j].cmc)):
                    cards[k] = left[i]
                    i += 1
                else:
                    cards[k] = right[j]
                    j += 1
                
                k+= 1

            while j < len(right):
                cards[k] = right[j]
                j += 1
                k += 1

            while i < len(left):
                cards[k] = left[i]
                i += 1
                k += 1

#***************************START OF MAIN************************************

def read_in_cards():
    file = open("cardspipe.txt",encoding="utf-8");
    count = 0
    lineCount = 0
    cards = [] #Stores each variable needed to make a new card object, gets reset afterwards

    allCards = [] #this will hold every card, will NOT change throughout course of program (after reading in completes)
    allCreatures = []
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

    # if(name == "Interplanar Brushwagg"): #USE FOR DEBUGGING
    #     print(lineCount) #PUT BREAKPOINT TO SEE WHAT LINE THE ERROR OCCURS

    return allCards, allCreatures
allCards, allCreatures = read_in_cards()

print("Total Cards Added: " + str(allCards.__len__()))
print("Size of Creature array: " + str(allCreatures.__len__()))

#***************************************END OF FILE READ IN*******************************

# printArray(allCreatures)
import sys
sys.setrecursionlimit(100000)
print(sys.getrecursionlimit())


print('s')
# quickSort(allCreatures, 0, allCreatures.__len__()-1, "cmc")
print('q')
print("")
print("***************AFTER QUICK SORTING***********************")
print("")
# printCMC(allCreatures)
print('l')

search_options = ["name", "cmc", "color", "typ", "supTyp", "subTyp", "rarity", "text", "power", "tough"]
# mergeSort(allCreatures, "power")
print("")
print("***************AFTER MERGE SORTING***********************")
print("")
# printPower(allCreatures)

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

