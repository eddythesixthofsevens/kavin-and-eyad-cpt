import random

name = input("Enter a character name: ")
age = input("Enter an age: ")
SuperGoodTraits = ["Speed II","Strength II", "Skill II", "Power II", "Sneak II", "Intelligence II", "Sharpness"]
goodTraits = ["Speed I", "Strength I", "Skill I", "Power I", "Sneak I", "Intelligence I"]
NeutralTraits = ["Kindness", "Loyalty", "Greed", "Honor", "Knitter", "Grace", "Generosity"]
badTraits = ["Blindness I", "Slowness I", "Cursed I", "Brittle I", "Dullness I", ""]
SuperBadTraits = [  ]

def listChooser():
    listChoice = random.randint(1,5)
    

charTraits = []
charTotalValue = 0
def trait_chooser(traitNum, listName):
    for num in range(traitNum):
        charTraits = r