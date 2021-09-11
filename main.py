#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "F43CA525-F03C-4F57-B347-87B8A699A064",
  "name": "Pirate",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631393246762,
  "passages": [
    {
      "name": "Empty Island",
      "tags": "",
      "id": "1",
      "text": "You wake up on a barren beach that goes around the whole island. There is  In front of you there is a little wooden raft with some paddles that you could ride on. To the north you see an island with a wooden building on it.\n\n[[NORTH->Tavern island]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Tavern island",
          "original": "[[NORTH->Tavern island]]"
        }
      ],
      "hooks": [],
      "cleanText": "You wake up on a barren beach that goes around the whole island. There is  In front of you there is a little wooden raft with some paddles that you could ride on. To the north you see an island with a wooden building on it."
    },
    {
      "name": "Tavern island",
      "tags": "",
      "id": "2",
      "text": "On this island there is a run down wooden building. The door to the building is slightly open, you could go IN. While going around the island you see more islands in the distance.\nTo the north there is an island with a larger hill and cave that goes through it. \nTo the east there is a larger island with a large mountain in the middle. \nTo the west there is a smaller island with what looks to be some sort of stone stucture in the center.\n\n[[INSIDE->Abandoned Tavern]] \n[[IN->Abandoned Tavern]] \n[[TAVERN->Abandoned Tavern]] \n[[NORTH->Cave Island]] \n[[EAST->Mountain Island]] \n[[WEST->Statue Island]] \n[[SOUTH->Empty Island]]",
      "links": [
        {
          "linkText": "INSIDE",
          "passageName": "Abandoned Tavern",
          "original": "[[INSIDE->Abandoned Tavern]]"
        },
        {
          "linkText": "IN",
          "passageName": "Abandoned Tavern",
          "original": "[[IN->Abandoned Tavern]]"
        },
        {
          "linkText": "TAVERN",
          "passageName": "Abandoned Tavern",
          "original": "[[TAVERN->Abandoned Tavern]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Cave Island",
          "original": "[[NORTH->Cave Island]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Mountain Island",
          "original": "[[EAST->Mountain Island]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Statue Island",
          "original": "[[WEST->Statue Island]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Empty Island",
          "original": "[[SOUTH->Empty Island]]"
        }
      ],
      "hooks": [],
      "cleanText": "On this island there is a run down wooden building. The door to the building is slightly open maybe you could fit. While going around the island you see more islands in the distance.\nTo the north there is an island with a larger hill and cave that goes through it. \nTo the east there is a larger island with a large mountain in the middle. \nTo the west there is a smaller island with what looks to be some sort of stone stucture in the center.\nThe structures door is slightly open."
    },
    {
      "name": "Cave Island",
      "tags": "",
      "id": "3",
      "text": "On the island there are many trees and bushes. In an opening through the foliage there is a large cave. The cave is too dark to see into.\n\n[[SOUTH->Tavern island]] \n[[CAVE->Cave start]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "Tavern island",
          "original": "[[SOUTH->Tavern island]]"
        },
        {
          "linkText": "CAVE",
          "passageName": "Cave start",
          "original": "[[CAVE->Cave start]]",
          "require" : "lantern"
        }
      ],
      "hooks": [],
      "cleanText": "On the island there are many trees and bushes. In an opening through the foliage there is a large cave. The cave is too dark to see into."
    },
    {
      "name": "Mountain Island",
      "tags": "",
      "id": "4",
      "text": "At the center of the island there is a tall mountain. As you are looking up you cannot see the top of the mountain through the clouds. At the base of the mountain there is a lot of bushes and low trees. Through the trees you can see a small path, it looks like it goes to a little ledge above the trees.\n\n[[PATH->Mountain ledge]]\n[[WEST->Tavern island]]",
      "links": [
        {
          "linkText": "PATH",
          "passageName": "Mountain ledge",
          "original": "[[PATH->Mountain ledge]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Tavern island",
          "original": "[[WEST->Tavern island]]"
        }
      ],
      "hooks": [],
      "cleanText": "At the center of the island there is a tall mountain. As you are looking up you cannot see the top of the mountain through the clouds. At the base of the mountain there is a lot of bushes and low trees. Through the trees you can see a small path, it looks like it goes to a little ledge above the trees."
    },
    {
      "name": "Statue Island",
      "tags": "",
      "id": "5",
      "text": "There is a circle of trees on the edge of the island. In the middle there is a stone statue of a monkey with many chucks out of it. There are many pieces of the statue on the ground around it. There appears to be something on top of the statue but you cant see what it is. It feels loose like if you had something sharp you could free it if you HIT it. \n\n[[EAST->Tavern island]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "Tavern island",
          "original": "[[EAST->Tavern island]]"
        },
        {
          "linkText": "HIT",
          "passageName": "Statue Island",
          "original": "[[WEST->Statue Island]]",
          "require": "knife",
          "item" : "ruby"
        }
      ],
      "hooks": [],
      "cleanText": "There is a circle of trees on the edge of the island. In the middle there is a stone statue of a monkey with many chucks out of it. There are many pieces of the statue on the ground around it. There appears to be something on top of the statue but you cant see what it is. It feels loose like if you had something sharp you could free it if you HIT it."
    },
    {
      "name": "Abandoned Tavern",
      "tags": "",
      "id": "6",
      "text": "While inside the building you can see many table and chair sets with empty wooded mugs on the tables. Toward the back of the building there is a bar with more mugs on it. Behind the bar there are many glass bottles of different sizes, many of which are shattered. There is a pile of table and chairs blocking door behind the bar. On the wall there is a lantern that looks like it is in good condition, you could PICKUP the lantern. \n\n[[BACK->Tavern island]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Tavern island",
          "original": "[[BACK->Tavern island]]"
        },
        {
          "linkText": "PICKUP",
          "passageName": "Abandoned Tavern",
          "original": "[[INSIDE->Abandoned Tavern]]",
          "item": "lantern"
        }
      ],
      "hooks": [],
      "cleanText": "While inside the building you can see many table and chair sets with empty wooded mugs on the tables. Toward the back of the building there is a bar with more mugs on it. Behind the bar there are many glass bottles of different sizes, many of which are shattered. There is a pile of table and chairs blocking door behind the bar. On the wall there is a lantern that looks like it is in good condition, you might be able to GRAB it."
    },
    {
      "name": "Mountain ledge",
      "tags": "",
      "id": "7",
      "text": "There is a tent set up in a little opening in mountain. The tent is empty. On the ground there are burnt sticks gathered in pile. On the ground there is a large knife you can PICKUP. Looking out over the edge you can see the other islands. There is a weird shine coming from the statue.\n\n[[BACK->Mountain Island]] \n[[DOWN->Mountain Island]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Mountain Island",
          "original": "[[BACK->Mountain Island]]"
        },
        {
          "linkText": "DOWN",
          "passageName": "Mountain Island",
          "original": "[[DOWN->Mountain Island]]"
        },
        {
          "linkText": "PICKUP",
          "passageName": "Mountain ledge",
          "original": "[[PATH->Mountain ledge]]",
          "item" : "knife"
        }
      ],
      "hooks": [],
      "cleanText": "There is a tent set up in a little opening in mountain. The tent is empty. On the ground there are burnt sticks gathered in pile. On the ground there is a large knife you can pick up. Looking out over the edge you can see the other islands. There is a weird shine coming from the statue."
    },
    {
      "name": "Cave start",
      "tags": "",
      "id": "8",
      "text": "The light shines from OUT of the cave. With the light of your lantern you walk through the cave. There are many stalactites hanging from the celling. Under many of the stalactites there are tall stalagmites, some even meeting with the stalactites above. At the end of the cave there is a strange looking stalagmite with hole cut out of it. Maybe you could INSERT something.  \n\n[[OUT->Cave Island]] \n[[INSERT->Secret Opening]]",
      "links": [
        {
          "linkText": "OUT",
          "passageName": "Cave Island",
          "original": "[[OUT->Cave Island]]"
        },
        {
          "linkText": "INSERT",
          "passageName": "Secret Opening",
          "original": "[[INSERT->Secret Opening]]",
          "require": "ruby"
        }
      ],
      "hooks": [],
      "cleanText": "The light shines from OUT of the cave. With the light of your lantern you walk through the cave. There are many stalactites hanging from the celling. Under many of the stalactites there are tall stalagmites, some even meeting with the stalactites above. At the end of the cave there is a strange looking stalagmite with hole cut out of it. Maybe you could INSERT something."
    },
    {
      "name": "Secret Opening",
      "tags": "",
      "id": "9",
      "text": "After inserting the ruby a path opened, allowing you to go further into the cave. The cave opens up to a larger cave and in the center you see a large ship. There is a massive opening to the sea on the otherside of the cave. The ship is parked close enough for you to be able to BOARD it.\n\n[[BACK->Cave start]] \n[[BOARD->Ship]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Cave start",
          "original": "[[BACK->Cave start]]"
        },
        {
          "linkText": "BOARD",
          "passageName": "Ship",
          "original": "[[BOARD->Ship]]"
        }
      ],
      "hooks": [],
      "cleanText": "After inserting the ruby a path opened, allowing you to go further into the cave. The cave opens up to a larger cave and in the center you see a large ship. There is a massive opening to the sea on the otherside of the cave. The ship is parked close enough for you to be able to BOARD it."
    },
    {
      "name": "Ship",
      "tags": "",
      "id": "10",
      "text": "Being on the ship feels familiar. The deck of the ship has cannons on both sides. There are many boxes and barrels around the mast and toward the front and back of the ship. A capstan sits in the middle of the deck. The low area of the ship is blocked by a steel grate. Toward the back of the ship there is a door but it is locked. There are stairs up to a higher deck. This upper deck is where the wheel sits. It is in working condition and it looks like you can set SAIL whenever you are ready.\n\n[[SAIL->The end]]\n[[BACK->Secret Opening]]",
      "links": [
        {
          "linkText": "SAIL",
          "passageName": "The end",
          "original": "[[SAIL->The end]]"
        },
        {
          "linkText": "BACK",
          "passageName": "Secret Opening",
          "original": "[[BACK->Secret Opening]]"
        }
      ],
      "hooks": [],
      "cleanText": "Being on the ship feels familiar. The deck of the ship has cannons on both sides. There are many boxes and barrels around the mast and toward the front and back of the ship. A capstan sits in the middle of the deck. The low area of the ship is blocked by a steel grate. Toward the back of the ship there is a door but it is locked. There are stairs up to a higher deck. This upper deck is where the wheel sits. It is in working condition and it looks like you can set SAIL whenever you are ready."
    },
    {
      "name": "The end",
      "tags": "",
      "id": "11",
      "text": "The feeling of loss fills you as you lift the anchor with the capston. The ship starts to slowly float out of the cave. Once you get out of the cave you lower the sail. You take a second to look at the sail. It feels very familiar somehow. As the ship begins to pick up speed, you take your postion at the wheel. You sail away from the islands you woke up on. After a bit you look back and cant help but wonder if you forgot something. The End",
      "links": [],
      "hooks": [],
      "cleanText": "The feeling of loss fills you as you lift the anchor with the capston. The ship starts to slowly float out of the cave. Once you get out of the cave you lower the sail. You take a second to look at the sail. It feels very familiar somehow. As the ship begins to pick up speed, you take your postion at the wheel. You sail away from the islands you woke up on. After a bit you look back and cant help but wonder if you forgot something. The End"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location,inventory):
	print("\nInventory: " + str(inventory))
	if "name" in current_location and "cleanText" in current_location:
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response, inventory):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				if "require" in link:
					if link["require"] in inventory:
						if "item" in link:
							if link["item"] not in inventory:
								inventory.append(link["item"])
						return link["passageName"]
					print("You lack something")
					return location_label
				if "item" in link:
					if link["item"] not in inventory:
						inventory.append(link["item"])
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Empty Island"
current_location = {}
response = ""
inventory = []


while True:
	if response == "QUIT" or current_location in "The end":
		break
	location_label = update(current_location, location_label, response, inventory)
	current_location = find_current_location(location_label)
	render(current_location,inventory)
	response = get_input()


print("Thanks for playing!")