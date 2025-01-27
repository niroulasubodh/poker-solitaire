#Name: Subodh Niroula
#Texas Hold'em Poker Game
from graphics import *
import random
 
#This function creates the background in the window for a game like player's hole, dealear's hole, Result and Quit
def createBackground(win):

    rect=Rectangle(Point(0,0), Point(250,165))
    rect.draw(win)
    txt=Text(Point(125, 175), "DEALER'S HOLE")
    txt.draw(win)
    #Controls
    rect1=Rectangle(Point(800,0), Point(550,165))
    rect1.draw(win)
    txt1=Text(Point(700, 175), "CONTROLS")
    txt1.draw(win)
    #Results
    rect2=Rectangle(Point(0,800), Point(250,635))
    rect2.draw(win)
    txt2=Text(Point(125, 625), "RESULTS")
    txt2.draw(win)
    #Players hole
    rect3=Rectangle(Point(800,800), Point(550,635))
    rect3.draw(win)
    txt3=Text(Point(700, 625), "PLAYER'S HOLE")
    txt3.draw(win)
    
#This Card class takes the random ranks and suits from hands class and returns the cards with its symbols
class Card():

    Ranks = list("23456789TJQKA")
    Suits = list("CDHS")
    SuitSymbol = {"C": chr(9827), "D" : chr(9830), "H" : chr(9829), "S": chr(9824)}

    def __init__(self, rank, suit):
        """ Pt is the lowest-left Point of the card's rectangle,
            height is the height of the rectangle. """

        if rank in Card.Ranks:
            self.rank = rank
        else:
            raise ValueError("Incorrect rank given.")
        if suit in Card.Suits:
            self.suit = suit
        else:
            raise ValueError("Incorrect suit given.")

    def __str__(self):
        return self.rank + Card.SuitSymbol[self.suit]
    
#this class randomly selects the ranks and suit from a list of ranks and suits and returns it.
class Hands():
    Ranks = list("23456789TJQKA")
    Suits = list("CDHS")
    
    def randomCards(self,n):
         self.card_list = []
         for i in range(n):
            random_rank= random.randint(0, len(Hands.Ranks))
            random_suit= random.randint(0, len(Hands.Suits))
            
            card = Card(Hands.Ranks[random_rank-1], Hands.Suits[random_suit-1])
            self.card_list.append(str(card))
         return self.card_list

#playGame class is for taking the number of cards in different rounds of the poker
class PlayGame():
    def hole_cards(self):
        hand=Hands()
        self.player_card = hand.randomCards(2)
        self.dealer_card = hand.randomCards(2)
        return self.player_card, self.dealer_card
    
    def flop_round(self):
        hand=Hands()
        self.display_card=hand.randomCards(3)
        return self.display_card
    def turnRiver_round(self):
        hand=Hands()
        self.display_card=hand.randomCards(1)
        return self.display_card
        
#This class is really important in this game, which takes the list of cards and return the category of the list of cards 
class CountingHands():
    
    def __init__(self, cards):
        self.cards=cards
        
    def is_straght_flush(self):
        #check if all cards have same suit
        suits = [card[-1] for card in self.cards]
        if len(set(suits)) != 1:
            return False
        
        #sort cards by rank
        ranks= [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        
        #check if ranks form a consecutive sequence
        for i in range(len(ranks)-1):
            if "23456789TJQKA".index(ranks[i]) +1 != "23456789TJQKA".index(ranks[i+1]):
                return False
        
        #if we reach here, it's straight flush
        return True
        
    def is_four_of_a_kind(self):
        ranks= [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
        return False
    
    def is_full_house(self):
        ranks= [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        for rank in ranks:
            if ranks.count(rank) == 3:
                for other_rank in ranks:
                    if other_rank != rank and ranks.count(other_rank) >= 2:
                        return True
        return False

        
    def is_flush(self):
        #check if all cards have same suit
        suits = [card[-1] for card in self.cards]
        #check if all cards have same suit
        suits = [card[-1] for card in self.cards]
        for suit in set(suits):
            if suits.count(suit) >=5:
                return True
        return False
        
    def is_straight(self):
        #sort cards by rank
        ranks= [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        
        #check if ranks form a consecutive sequence
        for i in range(len(ranks)-1):
            if "23456789TJQKA".index(ranks[i]) +1 != "23456789TJQKA".index(ranks[i+1]):
                return False
        
        #if we reach here, it's straight flush
        return True
    
    def is_three_of_a_kind(self):
        ranks= [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        for rank in ranks:
            if ranks.count(rank) == 3:
                return True
        return False
    
    def is_two_pair(self):
        ranks = [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        found_first_pair = False
        for i in range(len(ranks) - 1):
            if ranks[i] == ranks[i + 1]:
                if not found_first_pair:
                    found_first_pair = True
                else:
                    return True
        return False

    
    def is_one_pair(self):
        ranks= [card[:-1] for card in self.cards]
        ranks.sort(key=lambda x: "23456789TJQKA".index(x))
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
        return False
    
#This draws the rectangle for the cards and shows it.
class DrawCards():
    def __init__(self, win, P1, P2, lebel,center):
        self.win=win
        self.P1=P1
        self.P2=P2
        self.center= center
        self.lebel=lebel
    def draw_cards(self):
        self.rect=Rectangle(self.P1, self.P2)
        self.rect.setFill("grey")
        self.rect.draw(self.win)
        
    def show_cards(self):
        self.rect.setFill("White")
        self.txt=Text(self.center, self.lebel)
        if self.lebel[-1] in ["♥", "♦"]:
            self.txt.setTextColor('red')
        self.txt.setSize(35)
        self.txt.draw(self.win)

              
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False        

#This is the another main class that communicates with other classes and functions to actually run the game
class StartGame():
    def winningCheck(self,win, numGame, avg):
        self.win=win
        game=PlayGame()
        self.numGame=numGame
        self.avg=avg
        self.actions=''
        
#print the average in the first round
        txt_avg=Text((Point(125,785)), f"AVG: {float(self.avg)} pts out of {self.numGame-1} games")
        txt_avg.setSize(15)
        txt_avg.draw(self.win)
        
        self.player, self.dealer =game.hole_cards()
        self.fround=game.flop_round()
        self.tround=game.turnRiver_round()
        self.rround=game.turnRiver_round()
        
        self.player_cards= self.player+self.fround+self.tround+self.rround
        self.dealer_cards= self.dealer+self.fround+self.tround+self.rround
        self.pScore=ComparingHands()
        self.player_score,pStatus=self.pScore.WhoWins(self.player_cards)
        self.dScore=ComparingHands()
        self.dealer_score,dStatus=self.dScore.WhoWins(self.dealer_cards)
      
        
        #draw players cards
        Pp1, Pp2=Point(685,795), Point(795,655)
        center= Point(740, 725)
        for lebel in self.player:
            draw_pcard=DrawCards(self.win, Pp1,Pp2,lebel,center)
            dp_card=draw_pcard.draw_cards()
            show_pcard=draw_pcard.show_cards()
            center= Point(625,725 )
            Pp1, Pp2=Point(570,795), Point(680,655)

#facedown cards
        p1, p2 = Point(345,470), Point(455,330)
        p3, p4 = Point(345,325), Point(455,185)
        p5, p6 = Point(345,615), Point(455, 475)
        p7, p8 = Point(230,470), Point(340, 330)
        p9, p10 = Point(460,470), Point(570, 330)
       
        draw_f1card=DrawCards(self.win, p1,p2,self.fround[0], Point(400,400))
        draw_f1card.draw_cards()
        
        draw_f2card=DrawCards(self.win, p3,p4,self.fround[1],Point(400,255))
        draw_f2card.draw_cards()
        
        draw_f3card=DrawCards(self.win, p5,p6,self.fround[2],Point(400,545))
        draw_f3card.draw_cards()

        draw_tcard=DrawCards(self.win, p7,p8,self.tround[0],Point(285,400))
        draw_tcard.draw_cards()
        
        draw_rcard=DrawCards(self.win, p9,p10,self.rround[0],Point(515,400))
        draw_rcard.draw_cards()
        
        #draw dealers cards
        Pd1, Pd2= Point(5,5), Point(115,145)
        for lebel in self.dealer:
            draw_dcard=DrawCards(self.win, Pd1,Pd2,lebel,center)
            dd_card=draw_dcard.draw_cards()
            Pd1, Pd2=Point(120,5), Point(230,145)
        
 #Draw controls_bottons       
        
        controls_deals=Button(win,Point(612.5,41.25),75,32.5,"DEAL")
        controls_quit=Button(win,Point(737.5,41.25),75,32.5,"QUIT")
        controls_stay=Button(win,Point(612.5,123.75),75,32.5,"STAY")
        controls_fold=Button(win,Point(737.5,123.75),75,32.5,"FOLD")
#before starting the game activate the stay and fold button        
        controls_stay.activate()
        controls_fold.activate()
        
        p=win.getMouse()
        if controls_stay.clicked(p):
            r1=Rounds(win,"Rounds 1")
            r1.showRounds()
            self.actions+='S'
            draw_f1card.show_cards()
            draw_f2card.show_cards()
            draw_f3card.show_cards()
            p=win.getMouse()
            if controls_stay.clicked(p):
                r1.undrawRounds()
                r2=Rounds(win,"Rounds 2")
                r2.showRounds()
                self.actions+='/'+'S' 
                draw_tcard.show_cards()
                p=win.getMouse()
                if controls_stay.clicked(p):
                    r2.undrawRounds()
                    r3=Rounds(win,"Rounds 3")
                    r3.showRounds()
                    self.actions+='/'+'S' 
                    draw_rcard.show_cards()
                    Pd1, Pd2= Point(5,5), Point(115,145)
                    cent=Point(60,75)
                    p=win.getMouse()
                    if controls_stay.clicked(p) or controls_fold.clicked(p):
                        r3.undrawRounds()
                        r4=Rounds(win,"Rounds 4")
                        r4.showRounds()
                        if controls_stay.clicked(p):
                            self.actions+='/'+'S'
                        elif controls_fold.clicked(p):
                            self.actions+='/'+'F' 
                        for lebel in self.dealer:
                            draw_dcard=DrawCards(self.win, Pd1,Pd2,lebel,cent)
                            dd_card=draw_dcard.draw_cards()
                            dd_card=draw_dcard.show_cards()
                            cent=Point(175,75)
                            Pd1, Pd2=Point(120,5), Point(230,145)
                                 
                elif controls_fold.clicked(p):
                    r2.undrawRounds()
                    r3=Rounds(win,"Rounds 3")
                    r3.showRounds()
                    self.actions+='/'+'F'
                    draw_rcard.show_cards()
                    Pd1, Pd2= Point(5,5), Point(115,145)
                    cent=Point(60,75)
                    for lebel in self.dealer:
                        draw_dcard=DrawCards(self.win, Pd1,Pd2,lebel,cent)
                        dd_card=draw_dcard.draw_cards()
                        dd_card=draw_dcard.show_cards()
                        cent=Point(175,75)
                        Pd1, Pd2=Point(120,5), Point(230,145)
            elif controls_fold.clicked(p):
                r1.undrawRounds()
                r2=Rounds(win,"Rounds 2")
                r2.showRounds()
                self.actions+='/'+'F'
                draw_tcard.show_cards()
                draw_rcard.show_cards()
                Pd1, Pd2= Point(5,5), Point(115,145)
                cent=Point(60,75)
                for lebel in self.dealer:
                    draw_dcard=DrawCards(self.win, Pd1,Pd2,lebel,cent)
                    dd_card=draw_dcard.draw_cards()
                    dd_card=draw_dcard.show_cards()
                    cent=Point(175,75)
                    Pd1, Pd2=Point(120,5), Point(230,145)
                
        elif controls_fold.clicked(p):
            r1=Rounds(win,"Rounds 1")
            r1.showRounds()
            self.actions+='F'
            draw_f1card.show_cards()
            draw_f2card.show_cards()
            draw_f3card.show_cards()
            draw_tcard.show_cards()
            draw_rcard.show_cards()
            Pd1, Pd2= Point(5,5), Point(115,145)
            cent=Point(60,75)
            for lebel in self.dealer:
                draw_dcard=DrawCards(self.win, Pd1,Pd2,lebel,cent)
                dd_card=draw_dcard.draw_cards()
                dd_card=draw_dcard.show_cards()
                cent=Point(175,75)
                Pd1, Pd2=Point(120,5), Point(230,145)
        
        if pStatus=='One Pair' and dStatus=='One Pair':
            self.player_score=check_rank(self.player_cards)
            self.dealer_score=check_rank(self.dealer_cards)

        if self.player_score > self.dealer_score:
            score=0
            if self.actions[0]=='F':
                score= -100
            else:
                if self.actions[2]=='F':
                    score = -75
                else:
                    if self.actions[4]=='F':
                        score= -50
                    else:
                        if self.actions[6]=='F':
                            score= -25
                        else:
                            score= 100
            

            player_won(win,pStatus,dStatus,score,self.actions)
            
            average=self.avg+ score
            self.avg=float(average/self.numGame)
            # print the average of the game:
            txt_avg.undraw()
            txt_newavg=Text((Point(125,785)), f"AVG: {round(self.avg,1)} pts out of {self.numGame} games")
            txt_newavg.setSize(15)
            txt_newavg.draw(self.win)
            
            controls_stay.deactivate()
            controls_fold.deactivate()            
            controls_deals.activate()
            controls_quit.activate()
            
            a=win.getMouse()
            if controls_quit.clicked(a):
                win.close()
            if controls_deals.clicked(a):
                controls_deals.deactivate()
                self.numGame+=1
                win.close()
                newGame(self.numGame, round(self.avg,1))
        
        elif self.dealer_score > self.player_score:
            score=0
            if self.actions[0]=='F':
                score= 100
            else:
                if self.actions[2]=='F':
                    score= 75
                else:
                    if self.actions[4]=='F':
                        score= 50
                    else:
                        if self.actions[6]=='F':
                            score = 25
                        else:
                            score=-100

            dealer_won(win,pStatus,dStatus,score,self.actions)
            average=self.avg+ score
            self.avg=float(average/self.numGame)
            # print the average of the game:
            txt_avg.undraw()
            txt_newavg=Text((Point(125,785)), f"AVG: {round(self.avg,1)} pts out of {self.numGame} games")
            txt_newavg.setSize(15)
            txt_newavg.draw(self.win)
            
            controls_stay.deactivate()
            controls_fold.deactivate() 
            controls_deals.activate()
            controls_quit.activate()
            b=win.getMouse()
            if controls_quit.clicked(b):
                win.close()
            if controls_deals.clicked(b):
                controls_deals.deactivate()
                self.numGame+=1
                win.close()
                newGame(self.numGame,round(self.avg,1))
    
        else:
            score=0
            status=showStatus(win,pStatus,"blue",'')
            status.status_dealer()
            
            status=showStatus(win,dStatus,"blue",'')
            status.status_player()

            #print the points
            txt_points=Text((Point(125,755)), "Draw")
            txt_points.setSize(20)
            txt_points.draw(self.win)
            
            #print the actions
            txt_actions=Text((Point(125,725)), f"Actions: {self.actions}")
            txt_actions.setSize(20)
            txt_actions.draw(self.win)
            
            average=self.avg+ score
            self.avg=float(average/self.numGame)
            
            # print the average of the game:
            
            txt_avg.undraw()
            txt_newavg=Text((Point(125,785)), f"AVG: {round(self.avg,1)} pts out of {self.numGame} games")
            txt_newavg.setSize(15)
            txt_newavg.draw(self.win)
        
            controls_stay.deactivate()
            controls_fold.deactivate()             
            controls_deals.activate()
            controls_quit.activate()
            c=win.getMouse()
            if controls_quit.clicked(c):
                win.close()
            if controls_deals.clicked(c):
                controls_deals.deactivate()
                self.numGame+=1
                win.close()
                newGame(self.numGame, round(self.avg,1))

# function runs only if both players and dealers cards is a pair. This takes cards and returns the rank of pair card.
def check_rank(cards):
    ranks=[card[:-1] for card in cards]
    ranks.sort(key=lambda x: "23456789TJQKA".index(x))
    set_ranks=set()
    for i in ranks:
        if i=='T':
            i=10
        if i=='J':
            i=11
        if i=='Q':
            i=12
        if i=='K':
            i=13
        if i=='A':
            i=14
        if i in set_ranks:
            return int(i)
        else:
            set_ranks.add(i)
        
      
#This is the extension function for start game class
def dealer_won(win,pStatus,dStatus,score, actions):
    
    #print the points
    txt_points=Text((Point(125,755)), f"Points: {score}")
    txt_points.setSize(20)
    txt_points.draw(win)

    status=showStatus(win,dStatus,"red",chr(10003))
    status.status_dealer()
    
    status=showStatus(win,pStatus,"blue",'')
    status.status_player()
    
    #print the actions
    txt_actions=Text((Point(125,725)), f"Actions: {actions}")
    txt_actions.setSize(20)
    txt_actions.draw(win)

def player_won(win,pStatus,dStatus,score,actions):

    status=showStatus(win,pStatus,"red",chr(10003))
    status.status_player()

    status=showStatus(win,dStatus,"blue",'')
    status.status_dealer()

    #print the points
    txt_points=Text((Point(125,755)), f"Points: {score}")
    txt_points.setSize(20)
    txt_points.draw(win)

    #print the actions
    txt_actions=Text((Point(125,725)), f"Actions: {actions}")
    txt_actions.setSize(20)
    txt_actions.draw(win)
    
#This prints the rounds of the functions 
class Rounds():
    def __init__(self, win, rounds):
        self.win=win
        self.rounds=rounds
    def showRounds(self):
        self.txt_actions=Text((Point(400,50)), f"{self.rounds}")
        self.txt_actions.setSize(20)
        self.txt_actions.draw(self.win)
    def undrawRounds(self):
        self.txt_actions.undraw()
            
#this class draws the results of dealers and players
class showStatus():
    def __init__(self, win, status, color, check):
        self.win=win
        self.status= status
        self.color=color
        self.check=check
        
    def status_player(self):
        txt_player=Text((Point(125,695)), f"{self.check} Player: {self.status}")
        txt_player.setSize(20)
        txt_player.setTextColor(self.color)
        txt_player.draw(self.win)
        
    def status_dealer(self):
        txt_dealer=Text((Point(125,665)), f"{self.check} Dealer: {self.status}")
        txt_dealer.setSize(20)
        txt_dealer.setTextColor(self.color)
        txt_dealer.draw(self.win)

        
        
#class for comparing hands and return its rank:
    
class ComparingHands():
    def WhoWins(self,cards):
        self.cards=cards
        play_game= CountingHands(self.cards)
        rank, status=0, ''
        if play_game.is_straght_flush():
            rank, status=22, 'Straight Flush'
        elif play_game.is_four_of_a_kind():
            rank, status=21, " Four of a Kind"
        elif play_game.is_full_house():
            rank, status =20, "Full House"
        elif play_game.is_flush():
            rank, status =19, "Flush"
        elif play_game.is_straight():
            rank, status=18, "Straight"
        elif play_game.is_three_of_a_kind():
            rank, status=17, "Three of a Kind"
        elif play_game.is_two_pair():
            rank, status=16, "Two Pair"  
        elif play_game.is_one_pair():
            rank, status= 15, "One Pair"
            
        elif rank==0:
            ranks=[card[:-1] for card in self.cards]
            ranks.sort(key=lambda x: "23456789TJQKA".index(x) )
            if ranks[0]=='T':
                ranks[0]=10
            if ranks[0]=='J':
                ranks[0]=11
            if ranks[0]=='Q':
                ranks[0]=12
            if ranks[0]=='K':
                ranks[0]=13
            if ranks[0]=='A':
                ranks[0]=14
            check=ranks[0]
            for i in ranks:
                if i=='T':
                    i=10
                if i=='J':
                    i=11
                if i=='Q':
                    i=12
                if i=='K':
                    i=13
                if i=='A':
                    i=14
                if int(i)> int(check):
                    check=int(i)
            rank,status=check, "High Card"
            
        return(rank, status)
        
#function to start a new game
def newGame(numGame, avg):
    # Create a white graphics window, 800-by-800 pixels
    win = GraphWin("Poker-Solitaire", 800, 800)
    win.setBackground("lightgrey")
    background = createBackground(win)
    game=StartGame()
    won=game.winningCheck(win,numGame, avg)
    
    
def main_test():
    numGame, avg= 1,0
    start_game=newGame(numGame, avg)
    

if __name__ == "__main__":
    main_test()        
            
          







