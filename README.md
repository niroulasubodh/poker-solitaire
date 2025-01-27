# Solitaire Texas Hold'em Poker

This Python project is a solitaire version of the classic Texas Hold'em poker game, designed for a single-player experience. The player competes against an automated dealer to achieve the best five-card poker hand. The game involves strategic decision-making with an emphasis on predicting outcomes and optimizing points. 

The project was developed as part of a computer science class assignment, focusing on implementing Object-Oriented Programming (OOP) principles to create an engaging and functional application. To successfully run the program, ensure you have the graphics.py module available in the same directory as the program.

# Gameplay Overview

The game follows the traditional Texas Hold'em rules but with simplified mechanics:
    Betting Round 1: The player and dealer receive two "hole" cards. The player chooses to "stay" or "fold."
    Betting Round 2: Three community cards ("the flop") are dealt. The player again decides to "stay" or "fold."
    Betting Round 3: A fourth community card ("the turn") is dealt, followed by another decision round.
    Betting Round 4: The final community card ("the river") is dealt. The player makes their last decision.

At the end of the game, the hands are compared based on standard poker rankings, and points are awarded or deducted based on the player's decisions and the game outcome.

# Rules and Scoring

    Players aim to either:
        Win by "staying" in the game if their hand is better than the dealer's.
        Fold early if their hand is weak to minimize point loss.
    Points are calculated as follows:
        Winning after staying: +100 points.
        Folding early when losing: Up to +100 points, depending on the betting round.
        Folding early when winning: Up to -100 points, depending on the betting round.
        Losing after staying: -100 points.

# Acknowledgment

I would like to acknowledge Professor Anna Varvak for assigning this project and providing guidance and support throughout its completion. 
