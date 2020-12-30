# DCCRoller

This project aims to create a feature-complete DCC Character generator. At present, it has the following functionalities:

1: Rolls for HP (taking into account the instance's Stamina modifier) on its own

2: Sets XP to 0 to start

3: Rolls for copper pieces

4: Rolls for Birth Augr and Lucky rolls

5: Rolls for character occupation

6: Follows all associated rules in rolling for occupation (rolls for what type of farmer if occupation = farmer, rolls for species of animal if farmer,
rolls for contents of pushcart in the 1/100 event a Wainright is rolled).

7: Rolls for random equipment

8: Gets trained equipment associated with occupation

9: Adds all equipment to inventory

10: If inventory contains either a sling or a dart-based weapon, rolls for amount of rocks or darts (ammo) and adds to inventory

11: Rolls for instance's ability scores, and stores their associated dice modifiers. 

The file in which these functions are called is Character.py.
