#!/usr/bin/env python3

#! python3
import random

#List for Races to choose from
races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling']

#List for Classes to choose from
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin','Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
charName = input('Enter the name of your character: ')

#Funtion to prompt user to choose race and class
def player():
	global charClass
	global charRace
	global subRace 
	
	charRace = input('Choose Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Half-Orc, Halfling, Human, Tiefling: ')
	while charRace not in (races):
		charRace =input('Choose Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Half-Orc, Halfling, Human, Tiefling: ')
	
	if (charRace) == "Dwarf":
		subRace = input("Choose your sub-race: Hill Dwarf or Mountain Dwarf: ")

	if (charRace) == "Elf":
		subRace = input("Choose your sub-race: High Elf, Wood Elf or Dark Elf: ")

	if (charRace) == "Halfling":
		subRace = input("Choose your sub-race: Lightfoot or Stout: ")

	if (charRace) == "Gnome":
		subRace = input("Choose your sub-race: Rock Gnome or Forest Gnome: ")

		
	charClass =input('Choose Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard: ')
	while charClass not in (classes):
		charClass =input('Choose Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard: ')

player()

print('')

# Print name, race, class and subrace if applicable 
if (charRace) == "Human" or "Tiefling" or "Half-Elf" or "Half-Orc":
	print (f'{charName} the {charRace} {charClass}.')
else:
	print (f'{charName} the {charRace} {charClass} {subRace}.')

stats = []
#Stats generation
def statGen():
	stat = []
	#stats = []
	count = 0
	while count < 6:
		for i in range(4):
			roll = random.randint(1,6)
			stat.append(roll)
		stat.sort(reverse=True)
		del stat[3]
		statTotal = 0
		for i in stat:
			statTotal += i
		stats.append(statTotal)
		stat = []
		statTotal = 0
		count += 1
	stats.sort(reverse=True)

	
statGen()

ability_modifiers = {1:'-5', 2:'-4', 3:'-4', 4:'-3', 5:'-3', 6:'-2',7:'-2', 8:'-1', 9:'-1', 10:'0',
		     						11:'0', 12:'+1', 13:'+1', 14:'+2', 15:'+2', 16:'+3', 17:'+3', 18:'+4'}

#Output with character information:
if (charClass) == 'Barbarian':
	print('')
	print('The stats for', (charName),'are: ')
	print('Constitution:  ', (stats[0]), '\tConstitution modifier is:', ability_modifiers[(stats[0])])
	print('Strength:      ', (stats[1]), '\tStrength modifier is:',ability_modifiers[(stats[1])])
	print('Dexterity:     ', (stats[2]), '\tDexterity modifier is:', ability_modifiers[(stats[2])])
	print('Charima:       ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
	print('Wisdom:        ', (stats[4]), '\tWisdom modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]), '\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 12 + int(ability_modifiers[(stats[0])]))
	
if (charClass) == 'Bard':
	print('')
	print('The stats for', (charName),'are: ')
	print('Charisma:      ', (stats[0]),'\tCharisma modifier is:', ability_modifiers[(stats[0])])
	print('Dexterity:     ', (stats[1]),'\tDexterity modifier is:',ability_modifiers[(stats[1])])
	print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
	print('Wisdom:        ', (stats[3]), '\tWisdom modifier is:', ability_modifiers[(stats[3])])
	print('Strength:      ', (stats[4]), '\tStrength modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))
	
if (charClass) == 'Cleric':
	print('')
	print('The stats for', (charName),'are: ')
	print('Wisdom:        ', (stats[0]),'\tWisdom modifier is:', ability_modifiers[(stats[0])])
	print('Strength:      ', (stats[1]),'\tStrength modifier is:',ability_modifiers[(stats[1])])
	print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
	print('Charima:       ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
	print('Dexterity:     ', (stats[4]), '\tDexterity modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))


if (charClass) == 'Druid':
	print('')
	print('The stats for', (charName),'are: ')
	print('Wisdom:        ', (stats[0]),'\tWisdom modifier is:', ability_modifiers[(stats[0])])
	print('Dexterity:     ', (stats[1]),'\tDexterity modifier is:',ability_modifiers[(stats[1])])
	print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
	print('Charisma:      ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
	print('Intelligence:  ', (stats[4]), '\tIntelligence modifier is:', ability_modifiers[(stats[4])])
	print('Strength:      ', (stats[5]),'\tStrength modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))
	
if (charClass) == 'Fighter':
	print('')
	print('The stats for', (charName),'are: ')
	print('Strength:      ', (stats[0]),'\tStrength modifier is:', ability_modifiers[(stats[0])])
	print('Constitution:  ', (stats[1]),'\tConstitution modifier is:',ability_modifiers[(stats[1])])
	print('Dexterity:     ', (stats[2]), '\tDexterity modifier is:', ability_modifiers[(stats[2])])
	print('Charisma:      ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
	print('Wisdom:        ', (stats[4]), '\tWisdom modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 10 + int(ability_modifiers[(stats[1])]))
	
if (charClass) == 'Monk':
	print('')
	print('The stats for', (charName),'are: ')
	print('Dexterity:     ', (stats[0]),'\tDexterity modifier is:', ability_modifiers[(stats[0])])
	print('Wisdom:        ', (stats[1]),'\tWisdom modifier is:',ability_modifiers[(stats[1])])
	print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
	print('Charisma:      ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
	print('Intelligence:  ', (stats[4]), '\tIntelligence modifier is:', ability_modifiers[(stats[4])])
	print('Strength:      ', (stats[5]),'\tStrength modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))
	
if (charClass) == 'Ranger':
	print('')
	print('The stats for', (charName),'are: ')
	print('Dexterity:     ', (stats[0]), '\tDexterity modifier is:', ability_modifiers[(stats[0])])
	print('Wisdom:        ', (stats[1]), '\tWisdom modifier is:',ability_modifiers[(stats[1])])
	print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
	print('Charisma:      ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
	print('Intelligence:  ', (stats[4]), '\tIntelligence modifier is:', ability_modifiers[(stats[4])])
	print('Strength:      ', (stats[5]), '\tStrength modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 10 + int(ability_modifiers[(stats[2])]))
	
if (charClass) == 'Paladin':
	print('')
	print('The stats for', (charName),'are: ')
	print('Strength:      ', (stats[0]),'\tStrength modifier is:', ability_modifiers[(stats[0])])
	print('Constitution:  ', (stats[1]),'\tConstitution modifier is:',ability_modifiers[(stats[1])])
	print('Charisma:      ', (stats[2]), '\tCharisma modifier is:', ability_modifiers[(stats[2])])
	print('Dexterity:     ', (stats[3]), '\tDexterity modifier is:', ability_modifiers[(stats[3])])
	print('Wisdom:        ', (stats[4]), '\tWisdom modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 10 + int(ability_modifiers[(stats[1])]))
	
if (charClass) == 'Rogue':
	print('')
	print('The stats for', (charName),'are: ')
	print('Dexterity:     ', (stats[0]),'\tDexterity modifier is:', ability_modifiers[(stats[0])])
	print('Charisma:      ', (stats[1]),'\tCharisma modifier is:',ability_modifiers[(stats[1])])
	print('Strength:      ', (stats[2]), '\tStrength modifier is:', ability_modifiers[(stats[2])])
	print('Constitution:  ', (stats[3]), '\tConstitution modifier is:', ability_modifiers[(stats[3])])
	print('Wisdom:        ', (stats[4]), '\tWisdom modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 8 + int(ability_modifiers[(stats[3])]))
	
if (charClass) == 'Sorcerer':
	print('')
	print('The stats for', (charName),'are: ')
	print('Charisma:      ', (stats[0]),'\tCharisma modifier is:', ability_modifiers[(stats[0])])
	print('Dexterity:     ', (stats[1]),'\tDexterity modifier is:',ability_modifiers[(stats[1])])
	print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
	print('Wisdom:        ', (stats[3]), '\tWisdom modifier is:', ability_modifiers[(stats[3])])
	print('Intelligence:  ', (stats[4]), '\tIntelligence modifier is:', ability_modifiers[(stats[4])])
	print('Strength:      ', (stats[5]),'\tStrength modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 6 + int(ability_modifiers[(stats[2])]))
	
if (charClass) == 'Warlock':
	print('')
	print('The stats for', (charName),'are: ')
	print('Charisma:      ', (stats[0]),'\tCharisma modifier is:', ability_modifiers[(stats[0])])
	print('Constitution:  ', (stats[1]),'\tConstitution modifier is:',ability_modifiers[(stats[1])])
	print('Dexterity:     ', (stats[2]), '\tDexterity modifier is:', ability_modifiers[(stats[2])])
	print('Wisdom:        ', (stats[3]), '\tWisdom modifier is:', ability_modifiers[(stats[3])])
	print('Strength:      ', (stats[4]), '\tStrength modifier is:', ability_modifiers[(stats[4])])
	print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 8 + int(ability_modifiers[(stats[1])]))
	
if (charClass) == 'Wizard':
	print('')
	print('The stats for', (charName),'are: ')
	print('Intelligence:  ', (stats[0]),'\tIntelligence modifier is:', ability_modifiers[(stats[0])])
	print('Constitution:  ', (stats[1]),'\tConstitution modifier is:',ability_modifiers[(stats[1])])
	print('Dexterity:     ', (stats[2]), '\t Dexterity modifier is:', ability_modifiers[(stats[2])])
	print('Wisdom:        ', (stats[3]), '\t Wisdom modifier is:', ability_modifiers[(stats[3])])
	print('Charisma:      ', (stats[4]), '\t Charisma modifier is:', ability_modifiers[(stats[4])])
	print('Strength:      ', (stats[5]),'\t Strength modifier is:', ability_modifiers[(stats[5])])
	print('Hit Points:    ', 6 + int(ability_modifiers[(stats[1])]))
	
if (charRace) == 'Dwarf':
	print('')
	print('You have a plus 2 to Constitution')
	print('Speed: 25ft')
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.")
	print('Weapon Proficiency: Battleaxe, handaxe, throwing hammer, and warhammer.')
	print("Tool Proficiency: You gain proficiency with 1 tool set: smith's tools, brewer's supplies, or mason's tools.")
	print("Stonecunning: Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check.")
	print("Languages: You can speak, read, and write Common and Dwarfish")
	print("")
	
	if (subRace) == 'Hill Dwarf':
		print("")
		print("Hill Dwarf bonuses:")
		print("Ability Score Increase: Your Wisdom score increases by 1.")
		print("Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level")

	if (subRace) == 'Mountain Dwarf':
		print("")
		print("Mountain Dwarf bonuses:")
		print("Ability Score Increase: Your Strength score increases by 2.")
		print("Dwarven Armor Training: You have proficiency with light and medium armor.")

if (charRace)	== 'Elf':
	print('')
	print("Ability Score Increase: Plus 2 to dexterity")
	print("Speed: 30ft")
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Keen Senses: You have proficiency in the Perception skill")
	print("Fey Ancestry: You have advantage on saving throws against being charmed , and magic can't put you to sleep.")
	print("Trance: You don't need sleep. Instead you meditate deeply, remaining semiconscious, for 4 hours a day.")
	print("Language: You can speak, read and write Common and Elvish.")
	
	if (subRace) == "High Elf":
		print("")
		print("High Elves bonuses:")
		print("Ability Score Increase: Plus 1 to Intelligence.")
		print("Weapon Proficiencies:  Longsword, Shortsword, and Longbow")
		print("Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spell casting ability for it. ")
		print("Language: You can speak, read and write an extra language.")
		
	if (subRace) == "Wood Elf":
		print("")
		print("Wood Elves bonuses:")
		print("Ability Score Increase: Plus 1 to Wisdom")
		print("Weapon Proficiencies:  Longsword, Shortsword, Shortbow and Longbow")
		print("Speed: 35ft")
		print("Mask of the wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, failing snow, mist and other natural phenomena.")
		
	if (subRace) == "Dark Elf":
		print("")
		print("Dark Elves bonuses:")
		print("Ability Score Increase: Plus 1 to Charisma")
		print("Darkvision: 120 feet")
		print("Drow Weapon Training: Rapiers, Shortsword, and Hand Crossbows")
		print("Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom(Perception) checks that rely on sight when you, the target or whatever you are trying to perceive is in direct sunlight.\nDrow Magic: You know the Dancing light cantrip. At level 3 you can cast Faerie Fire once a day, and at level 5you can cast Darkness once a day. Charisma is your spelling casting ability.")
	
	

if (charRace)	== 'Halfling':
	print("Ability Score Increase: Your Dexterity score increases by 2.")
	print("Speed: 25 feet")
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Lucky: When you roll a 1 on an attack roll, ability check, or saving throw, you can re-roll the die and must use the new roll.")
	print("Brave: You have advantage on saving throws against being frightened.")
	print("Halfling Nimbleness: You can move through the space of any creature that is of a size larger than yours.")
	print("")
	if (subRace) == 'Lightfoot':
		print("Lightfoot Bonus:")
		print("Ability Score Increase: Your Charisma score increases by 1.")
		print("Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.")
	if (subRace) == 'Stout':
		pritn("Stout bonus:")
		print("Ability Score Increase: Your Constitution score increases by 1.")
		print("Stout Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.")
		

if (charRace) == "Human":
	print("")
	print("Ability Score Increase: Your ability scores each increase by 1")
	print("Alignment: Humans tend toward no particular alignment. The best and the worst are around among them")
	print("Size: Medium")
	print("Speed: Your base walking speed is 30 feet")
	print("Languages: You can speak, read, and write Common and one extra language of your choice.")

if (charRace) == "Gnome":
	print("")
	print("Ability Score Increase: Your Intelligence score increases by 2.")
	print("Size: Small.")
	print("Speed: 25 feel")
	print("Gnome Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.")
	print("Languages: You can speak, read, and write Common and Gnomish. ")
	print("")
	
	if (subRace) == 'Forest Gnome':
		print("Forest Gnome Bonus:")
		print("Ability Score Increase: Your Dexterity score increases by 1.")
		print("Natural Illusionist: You know the minor illusion cantrip. Intelligence is your spellcasting ability for it.")
		print("Speak with Small Beasts: Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animaIs and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.")
		
	if (subRace) == 'Rock Gnome':
		print("Rock Gnome Bonus:")
		print("Ability Score Increase: Your Constitution score increases by 1.")
		print("Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, at technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally appIy.")
		print("Tinker: You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:")
		print("Clockwork Toy: This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, ar soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.")
		print("Fire Starter: The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.")
		print("Music Sox: When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed")
	


if (charRace) == "Half-Elf":
	print("")
	print("Ability Score Increase: Your Strength score increases by 2, and your Constitution score increases by 1.")
	print("Size: Medium")
	print("Speed: 30 feel")
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.")
	print("Skill versatility: You gain proficiency in two skills of your choice.  ")
	print("Languages: You can speak, read, and write Common, Elvish, and one extra language of your choice.")
	print("")
	
if (charRace) == "Half-Orc":
	print("")
	print("Ability Score Increase. Your Charisma score increases by 2, and plus 1 to 2 other attributes.")
	print("Size: Medium")
	print("Speed: 30 feel.")
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Menacing: You gain proficiency in the Intimidation skill.")
	print("Relentless Endurance: When you are reduced to O hit points but not killed outright. You can drop to I hit point instead. You can't use this feature again until you finish a long rest. ")
	print("Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it lo the extra damage of the critical hit.")
	print("Languages: You can speak. read, and write Common and Ore. Ore is a harsh. grating language with hard consonants.")
	print("")

if (charRace) == "Tiefling":
	print("")
	print("Ability Score Increase: Your Intelligence score increases by 1, and your Charisma score increases by 2.")
	print("Size: Medium")
	print("Speed: 30 feel")
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Hellish Resistance: You have resistance to fire damage.")
	print("Infernal Legacy: You know the thaumaturgy cantrip. Once you reach 3rd level, you can cast the hellish rebuke spell once per day as a 2nd-level spell. Once you reach 5th level, you can also cast the darkness spell once per day. Charisma is your spellcasting ability for these spells.")
	print("Languages: You can speak. read. and write Common and Infernal.")
	print("")

if (charRace) == "Dragonborn":
	print("")
	print("Ability Score Increase: Your Strength score increases by 2. and your Charisma score increases by 1.")
	print("Size: Medium")
	print("Speed: 30 feet")
	print("Darkvision: You can see in dim light within 60 feet of you as if it were bright light. In darkness as if it were dim light, but only shades of gray.")
	print("Draconic Ancestry. You have draconic ancestry.\n Choose one type of dragon from the Draconic Ancestry table. Your breath weapon and damage resistance are determined by the dragon type. as shown in the table.")
	print("Dragon Damage Type                Breath Weapon")
	print("Black  Acid 		5 by 30 fI. line      (Dex. save)")
	print("Blue   Lightning 	5 by 30 ft. line      (Dex. save)")
	print("Brass  Fire 		5 by 30 ft. line      (Dex. save)")
	print("Bronze Lightning 	5 by 30 ft. line      (Dex. save)")
	print("Copper Acid 		5 by 30 fI. line      (Dex. save)")
	print("Gold   Fire 		15 ft. cone           (Dex. save)")
	print("Green  Poison 		15 ft. cone           (Con. save)")
	print("Red    Fire 		15 fI. cone           (Dex. save)")
	print("Silver Cold 		15 fI. cone           (Con. save)")
	print("White  Cold 		15 fI. cone           (Con. save)")
	print("Damage Resistance. You have resistance to the damage type associated with your draconic ancestry.")
	print("Languages: You can speak. read, and write Common and Draconic. ")
	print("")
