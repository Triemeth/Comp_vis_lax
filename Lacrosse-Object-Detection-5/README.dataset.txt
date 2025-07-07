# Lacrosse-Object-Detection > Dataset 500 with Augments
https://universe.roboflow.com/ryseai/lacrosse-object-detection

Provided by a Roboflow user
License: MIT

# Project Overview

The objective of the project is to detect lacrosse players and referees on the field. In the future I'm planning to detect the ball and field lines aswell.

There three types of players: Goalie, Longpoles and Shortsticks.

You can find my Code on [Github](https://github.com/RySE-AI/Lacrosse-Object-Detection) when I'm finished with the labeling ;) I'll probably use YOLO-NAS for this task.

# Labeling Guide

Probably I will reiterate and change the guide but for the first let's start with:

### Version 0.1

- Label each player with their sticks
- If there is no indicator or if you're unsure what kind of player it is, label this player as a shortstick
- Player's on the sideline/off field will not be labeled (may lead to problems)
- If you only see the stick of the player, don't label it
- It's subjective but I want at least see 30% of the person (e.g. Head+Chest, Lower Body) 

# Class Descriptions

### Facts:
- Ten Players per team on the field, goalie included
- 4 Longpoles per team on the field
- Only 6 players (longpole or shortstick doesnt matter) can be in the attacking zone
- Only 7 players (usually 4 longpoles + Goalie + 2 Shortsticks) can be in the defending zone
- 4 Referees per game 
	- usually 3 Referees on the field -> 2 on the side of the bench/team zones and 1 on the far side
	- 1 Referee in the benching zone as a CBO (Chief Bench Official)

##### Goalie:
- Attributes
	-  Special shaped Stick (Large head)
	-  Helmet with Throatguard
	-  large Chestpad
	-  usually no elbow-/armguards
	
##### Longpole:
- Attributes
	-  Stick Length about 132.08 cm to 182.88 cm
	-   usually only elbowguards (only convering the elbow joint)

##### Shortstick:
- Attributes
	-  Stick Lenght about 101.60 cm to 106.68 cm
	-   carrying elbowguards or armguards (Attacker usually have bigger guards which cover more than the joint)

##### Referee: 
- Attributes
	- striped black/white or yellow shirt depending on the league (PLL: yellow)
	- wears a hat
	- 2 carries yellow flags for indicating fouls

##### Sports Ball:
Lacrosse Ball -> Isnt of Interest in the first run but I'm labeling it sometimes (THE DATASET DOESNT INCLUDE THIS CLASS)


Disclaimer
This project uses images and videos sourced from YouTube (loaded via roboflows UI). I do not claim ownership of any of the content used, and all rights and ownership remain with the original creators and copyright holders. This project is strictly intended for research purposes and is not for commercial use.