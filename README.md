# Solitaire Texas Hold'em Poker

This Python project is a solitaire version of the classic Texas Hold'em poker game, designed for a single-player experience. The player competes against an automated dealer to achieve the best five-card poker hand. The game involves strategic decision-making with an emphasis on predicting outcomes and optimizing points. 

The project was developed as part of a computer science class assignment, focusing on implementing Object-Oriented Programming (OOP) principles to create an engaging and functional application. To successfully run the program, ensure you have the graphics.py module available in the same directory as the program.

# Rules of the game
 
The game proceeds as follows:

**(Betting round 1)** First, you and the dealer both get two cards.  Those are your two “hole” cards.  You can see your cards (the are “face up), but not the dealer’s cards (they are “face down”).  You get a chance to bid (“stay” or “fold”).

If you stay:

**(Betting round 2)** Three more cards are dealt “face up”.  Those are “the flop”.  You get a chance to bid (“stay” or “fold”). 

If you stay:

**(Betting round 3)** One more card is dealt “face up”.  That’s “the turn”. You get a chance to bid (“stay” or “fold”).  

If you stay:

**(Betting round 4)** One last card is dealt “face up”.  That’s “the river”. You get a chance to bid (“stay” or “fold”).  

If you stay:

The dealer’s “hole” cards are revealed, and your hand is compared to the dealer’s hand according to the standard rules of poker.  Whoever has the best hand wins.  In an unlikely event of a tie, nobody wins.
 
If you stay all four betting rounds:

• If you win, you get 100 points—all your bets were correct for the occasion!

• If you lose, you get -100 points—all your bets were not correct this time around.
 
If you fold on any of the betting stages, then the dealer’s “hole” cards are revealed, the rest of the five community cards are dealt, and the would-be winner gets determined.  

• If you would have lost, you get 100 points if you folded on the 1st betting round, 75 points if you folded on the 2nd betting round, 50 points if you folded on the 3rd betting round, and 25 points if you folded on the 4th betting round.  The sooner you realized that you should fold, the more points you get!

• If you would have won, you get -25 points if you folded on the 4th round (and stayed before then), -50 points if you folded on the 3rd round (and stayed before then), -75 points if you folded on the 2nd round (and stayed before then), and -100 points if you folded on the 1st round.
 
After each game, the player’s average score gets displayed, and the player gets a chance to play again.  The cards that got played get put back into the deck, and the deck is reshuffled before each new game.

# Acknowledgment

I would like to acknowledge Professor Anna Varvak for assigning this project and providing guidance and support throughout its completion. 
