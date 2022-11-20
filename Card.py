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
        

testCard = Card("name", "super", "type", "sub", 3, 4, "blue", 7, "asdhf uh", "f jajsdifj ", "idk.com");
testCard.print();
