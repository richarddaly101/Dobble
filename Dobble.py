# # Dobble Generator
# 
# 
# -The code in cell 1 and cell 2 was provided with the exercise. 
# 
# -I modified the code in cell 2 to store a carddeck in a dictionary with the card number as key and image id in a set as the value. This is per the requirement of part 1. 
# 
# -This carddeck will be used to generate my source dobble deck to select cards from and then create a game dobble deck.


import random
import emoji

imageDict = dict()
fin = open('emoji_names.txt',"r")
lines = fin.readlines()
for i, el in enumerate(lines):
        imageDict[i+1] = emoji.emojize(el.strip())
        print(i+1,imageDict[i+1],end=' ')
nIm = 8
n = nIm - 1
r = range(n)
rp1 = range(n+1)
c = 0

carddeck={}

# First card
c += 1
print('Card %2d: ' % c, end='');
for i in rp1:
    print(i+1, end=' ')
    carddeck.setdefault(c,[])
    carddeck[c].append(i+1)
print()

# n following cards
for j in r:
    c = c+1
    print('Card %2d: ' % c, end='');
    print(1,end=' ')
    carddeck.setdefault(c,[])
    carddeck[c].append(1)
    for k in r:
        set1=(n+2+n*j+k)
        print(n+2 + n*j +k, end=' ')
        carddeck[c].append(set1)
    print()

# n x n following cards
for i in r:
    for j in r:
        c = c+1
        print('Card %2d: ' % c, end='');
        print(i+2,end=' ')
        carddeck.setdefault(c,[])
        carddeck[c].append(i+2)
        for k in r:
            set2=((n+1 +n*k + (i*k+j) % n)+1)
            print ((n+1 +n*k + (i*k+j) % n)+1, end=' ')
            carddeck[c].append(set2)
        print()


# -The check validity function is run using the carddeck dictionary defined in the cell above. 
# 
# -After the validity check is done the emojis images will be mapped in to their respective id number in carddeck. 


def check_validity(check, verbose=True):
    """This function tests that each card matches on one and only one image."""
    incorrectcard=0
    for key,value in check.items():#iterate through each card in dictionary.
        values=set(value)#change value in dictionary to a set to allow intersection function.
        for key,value in check.items():#for each card iterate through every other card.
            values2=set(value)
            if values==values2:#If card is same as comparison skip.
                pass
            else:
                if verbose:#Only ran if verbose=True.
                    checker=(values.intersection(values2))#Use intersection to see where two set variables match in values.
                    print(values)
                    print(values2)
                    if (len(checker))==1:
                        print(checker, ' is the only common value in the above two cards')
                    else:
                        print(checker, 'there are more than one common values in the above cards')
                        incorrectcard+=1  
                elif not verbose:#Only ran if verbose=False.
                    checker=(values.intersection(values2))
                    if (len(checker))==1:
                        pass
                    else:
                        incorrectcard+=1
                
    if incorrectcard==0:
        print("All cards match on only value")
    else:
        print('Error, not all cards match on only one value')

        

#Run the carddeck created in cell two in check validity function. Set verbose=False for overall result
#or verbose=True to see output for each pair and overall result.
check_validity(carddeck, verbose=True)


# -Sourcedeck below is initially an empty list. This is a global variable that will be used to create dobble cards.
# 
# -It is passed into DobbleGenerator to create dobble cards. and iterates through images id numbers and emojis received and maps emoji image to corresponding image id number.
# 
# 


sourcedeck=[]

def DobbleGenerator(deck):
    """Iterates through images id numbers in card.deck(cell 2) and emojis received(cell 1) and maps 
    emoji images to corresponding image id numbers. The images are then
    addedd to the sourcedeck list"""
    for keycard,value in carddeck.items(): 
        for keyemoj,valuepic in imageDict.items():
            if keyemoj in value:
                deck.append(valuepic)

    return deck
                 

    
DobbleGenerator(sourcedeck)

#List comprehension is used below to create a new list from sourcedeck which containts sub lists containing 8 elements, 
#each of which only contains one matching image when compared against each other.

sourcedeck = [sourcedeck[image:image + 8] for image in range(0, len(sourcedeck), 8)]



class DobbleCard:
    """DobbleCard initalizes as a random element selected from sourcedeck and stores in self.card"""
    def __init__(self):#Dobblecard initalizes as a random card selected from the sourcedeck.
        self.card=random.choice(sourcedeck)
        #Images in each card are shuffled below so matching images are not always in same index number in list.
        random.shuffle(self.card)
        #After card is selected it is removed from sourcedeck below to avoid a card being picked twice.
        sourcedeck.remove(self.card)
        




class DobbleDeck():
    """I am assuming the dobbledeck is initially empty, and that it will add cards stored as Dobblecard instances 
    for playing in the game."""
    def __init__(self):#Dobbledeck initializes self.deck as an empty list. 
        self.deck=[]
        
    #Add_card adds DobbleCards from Dobblecard class. 
    #The number of cards added is based on the amount of cards requested by the user. One extra card is added which is involved
    #in only one test at the start of the game to match sample games provided.
    def add_card(self, number):
        for x in range(number+1): 
            card=DobbleCard()
            self.deck.append(card)#Add in dobblecard instances to dobbledeck.
            
    def play_card(self):#Play_card displays card at top of deck in self.deck to players.
        print("")
        print(self.deck[0].card[0], self.deck[0].card[1], self.deck[0].card[2])
        print(self.deck[0].card[3], self.deck[0].card[4], self.deck[0].card[5])
        print(self.deck[0].card[6], self.deck[0].card[7])
        print("")
        
    def remove_card(self):#Remove_card removes card at top of dobbledeck i.e. index 0 in self.deck list after it is shown.
        del self.deck[0]
        







# -The game of dobble is played below.
# 
# -Selectedcard is instance of dobblecard and gamedeck instance of Dobbledeck.
# 
# -The user is prompted for the number of cards they want (minimum answer is 1 which will show 2 cards i.e. one round of Dobble.
# 
# -Main play loop is exited count variable is greater than number of cards i.e. all cards shown.
# 
# 



def DobbleGame():
    """Parameters of dobblegame are stored here. DobbleGame run in cell below."""
    count=0
    scoreA=0
    scoreB=0
    
    selectedcard=DobbleCard()
    gamedeck=DobbleDeck()
    

    number_of_cards = int(input('How many cards (<56)?'))   
    while number_of_cards<1 or number_of_cards>56:
        number_of_cards = int(input('Please pick at least 1 card to a maximum of 56'))
   
    createdeck=gamedeck.add_card(number_of_cards)#number of cards in gamedeck is created here based on user input.
    print('If you want to record a draw type "d" or "D"')


    #Main play loop
    while count<number_of_cards:
            card1=gamedeck.play_card()#First card in deck is shown to player.
            #The first card is only card involved in one test i.e. shown only once. It is then removed below from the gamedeck
            #with remove_card method below.
            gamedeck.remove_card()
            #The second card is shown below with play_card. During the next round it will be shown again as the first card, 
            #after which it is removed from the gamedeck.
            card2=gamedeck.play_card()
            winner=input('Who wins (A or B)? ').lower()
            while winner not in 'abd':
                winner = input("Input must be either A or B for a win, or D for a draw: ").lower()
            if winner=='a':
                scoreA+=1
            elif winner=='b':
                scoreB+=1
            count+=1    
            
    print('Score')
    print('A:', scoreA)
    print('B:', scoreB)
    #Below code refills the sourcedeck for players if they wish play another game
    global sourcedeck
    sourcedeck=[]#reset sourcedeck to empty list
    DobbleGenerator(sourcedeck)#generate dobble images in function
    sourcedeck = [sourcedeck[image:image + 8] for image in range(0, len(sourcedeck), 8)]#split out dobble images into 8 elements
    #per sublist


    

DobbleGame()






