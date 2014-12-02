# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


 
__author__="jposenau"
__date__ ="$Nov 24, 2014 9:44:56 AM$"
 
 
import random
import os
import pygame, pygbutton
from pygame.locals import *
import sys, os
sys.path.insert(0, os.path.abspath('..'))
 
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
 
 
 
# initialize some useful global variables
FPS = 30
WINDOWWIDTH = 380
WINDOWHEIGHT = 350
in_play = False
outcome = ""
query = ""
pscore = 0
dscore = 0
spscore = ''
sdscore = ''
visible = False
 
#pygame.init()
canvas = pygame.display.set_mode([640,480])
pygame.display.set_caption("Blackjack duex 2")
fontObj3 = pygame.font.Font(pygame.font.match_font('timesnewroman'), 32)

gold_color = pygame.Color(255, 215, 0)
white_color = pygame.Color(255, 255, 255)
count = 0
draw_colour = white_color


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image, image.get_rect()

# Load Sound
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join( name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)
    return sound
 
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
 
card_images = pygame.image.load("cards_jfitz.png").convert()
 
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = pygame.image.load("card_jfitz_back.png").convert()    
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
 
 
# define card class
class Card:
    global visible, canvas
    
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank
 
    def __str__(self):
        return self.suit + self.rank
 
    def get_suit(self):
        return self.suit
 
    def get_rank(self):
        return self.rank
 
    def draw(self, canvas, pos):
       
        global card_images
        card_loc = ( CARD_SIZE[0] * RANKS.index(self.rank), 
                     CARD_SIZE[1] * SUITS.index(self.suit))
        
        cpos = (card_loc[0],card_loc[1],72,96)
        canvas.blit(card_images, pos , cpos)
        
        if pos == [220,200] and not visible :
            canvas.blit(card_back, pos ,(0,0,72,96))
        else:
            canvas.blit(card_images, pos , cpos)
        
# define hand class
 
class Hand:
    
    def __init__(self):
       self.h_player = [] # create Hand object
 
        # return a string representation of a hand       
    def __str__(self):       
        nstr = ""
        for n in self.h_player:
            nstr = nstr + " " + str(n)
        return nstr
          
    def add_card(self, card):
        self.h_player.append(card) 
    
# get values returns the value of a hand and does the heay lifting
    def get_value(self):
        global aces 
        value = 0
        for i in self.h_player:
            temp = VALUES.get(i.get_rank())
            if temp == 1:
                aces = aces +1
                temp = 11
            value = value + temp
            while value > 21 and aces > 0:
                value = value -10
                aces = aces -1
                
        return value
    def draw(self, canvas, pos): 
        
        x = pos[0]
        y = pos[1]
        for i in self.h_player:
            i.draw(canvas,[x,y])
            x = x + CARD_SIZE[0]
class Deck:
    
# create a Deck object   
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                c = Card(i,j)
                self.deck.append(c)
        
    def shuffle(self):
        random.shuffle(self.deck)
 
    def deal_card(self):
        return self.deck.pop(0)
    
    def __str__(self):
        nstr = ""
        for n in self.deck:
            nstr = nstr + " " + str(n)
        return nstr
def deal():
    
    global outcome, in_play, my_deck, player_hand, dealer_hand, query, dscore,sdscore
    global visible, aces 
    visible = False
    aces = 0
    if in_play:
        dscore = dscore+1
        sdscore = str(dscore)
    my_deck = Deck()
    my_deck.shuffle()
 
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    outcome = " Hit,  Stand, or New Deal ?"
   
 
    in_play = True
 
def hit():
    
        global in_play, outcome, dscorepscore, dscore, sdscore,spscore
        global visible
        
        if in_play:
            cc = my_deck.deal_card()
            player_hand.add_card(cc)
            total = player_hand.get_value()
#            print "Player total 1",total
            if total > 21:
                outcome = "Player BUSTED!!!"
                visible = True
                dscore = dscore + 1
                sdscore  =  str(dscore)
                in_play = False
                
def stand():
# build the dealer hand after player stands    
    global in_play, outcome, pscore, dscore, sdscore,spscore
    global visible, aces
    
    aces = 0
    total = 0
    if in_play: 
        visible = True
        total = dealer_hand.get_value()
#        print "Standing Total =",total
        while total < 17:
            cc = my_deck.deal_card()
            dealer_hand.add_card(cc)
            total= dealer_hand.get_value()
#            print "Dealer Total 1",total
            if total > 21:
                outcome = "Dealer BUSTED!!!"
                pscore = pscore + 1
                spscore  =  str(pscore)
                in_play = False
    if in_play == True:
        test = dealer_hand.get_value()
        if test >= player_hand.get_value() and test < 22:
#            print " Dealer Total 2", test
            outcome = "Dealer WINS!!!!"
            dscore = dscore + 1
            sdscore  =  str(dscore)
        else:
            outcome = "Player WINS!!!!"
            pscore = pscore +1
            spscore  =  str(pscore)
    in_play = False        
def draw(canvas):
    global player_hand, Outcome
 
    player_hand.draw(canvas,[220,100])
    dealer_hand.draw(canvas,[220,200])
    

def mc_handler(pos):
    print pygame.mouse.get_pressed()
 
def kd_handler(ichar):
    print str(ichar)
    if ichar == K_LEFT:
        print True
 
    
def ku_handler(ichar):
    print str(ichar)
   
    
def draw_handler(canvas):

    # clear canvas -- fill canvas with uniform colour, then draw everything below.
    # this removes everything previously drawn and refreshes 
    canvas.fill((0, 0, 0))
    
 
    # 
    global count, deal_button, hit_button, stand_button, outcome
    #count += 1
    #text_draw = fontObj3.render("CodeSkulptor Port", True, draw_colour)
    text_draw2 = fontObj3.render("Blackjack", True, draw_colour)
    text_draw3 = fontObj3.render(outcome,True, draw_colour)
    text_draw_player = fontObj3.render('Player',True, draw_colour)
    text_draw_dealer = fontObj3.render('Dealer',True, draw_colour)
    canvas.blit(text_draw_player,(125,150))
    canvas.blit(text_draw_dealer, (125, 250))
    text_draw4= fontObj3.render("Dealer Score     " + sdscore + "  Player Score     " +spscore,True,draw_colour)
    canvas.blit(text_draw2, (200,25))
    canvas.blit(text_draw3, (100,400))
    canvas.blit(text_draw4, ( 100,350))
    deal_button.draw(canvas)
    hit_button.draw(canvas)
    stand_button.draw(canvas)
    draw(canvas)
   
                                               
# call this function to start everything
# could be thought of as the implemntation of the CodeSkulptor frame .start() method.
def main():
    global deal_button, hit_button, stand_button
    # initialize loop until quit variable
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('PYG Blackjack')
  
 
    deal_button = pygbutton.PygButton((50, 150, 60, 30), 'Deal')
    hit_button = pygbutton.PygButton((50, 200, 60, 30), 'Hit')
    stand_button = pygbutton.PygButton((50, 250, 60, 30), 'Stand')
    deal()
    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
 
            if 'click' in deal_button.handleEvent(event):
                deal()
            if 'click' in hit_button.handleEvent(event):
                hit()
            if 'click' in stand_button.handleEvent(event):
                stand()
         
        draw_handler(canvas) 
     
        pygame.display.update()
        FPSCLOCK.tick(FPS)
 
if __name__ == '__main__':
    main()