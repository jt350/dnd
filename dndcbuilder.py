#! python3
import random

#List for Races to choose from

races=['Aarakocra', 'Dragonborn', 'Dwarf', 'Elf', 'Genasi', 'Gnome', 'Goliath', 'Half-Elf', 'Half-Orc', 'Halfing', 'Human', 'Tiefling', 'Aasimar']

#List for Classes to choose from

classes=['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin','Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
charName =input('Enter the name of your character: ')


#Funtion to prompt user to choose race and class

def player():
    global charClass
    global charRace

    charRace = input('Choose Aarakocra, Dragonborn, Dwarf, Elf, Genasi, Gnome, Goliath, Half-Elf, Half-Orc, Halfing, Human, Tiefling, Aasimar: ')
    while charRace not in (races):
        charRace =input('Choose Aarakocra, Dragonborn, Dwarf, Elf, Genasi, Gnome, Goliath, Half-Elf, Half-Orc, Halfing, Human, Tiefling, Aasimar: ')

    charClass =input('Choose Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard: ')
    while charClass not in (classes):
        charClass =input('Choose Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard: ')


player()

print('')
print ( (charName), 'the', (charRace), (charClass))

#Stats generation

stat1 = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
stat2 = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
stat3 = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
stat4 = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
stat5 = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
stat6 = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))
stats = [(stat1),(stat2),(stat3),(stat4),(stat5),(stat6)]
stats.sort(reverse=True)

ability_modifiers = {1:'-5', 2:'-4', 3:'-4', 4:'-3', 5:'-3', 6:'-2',7:'-2', 8:'-1', 9:'-1', 10:0,11:0, 12:+1, 13:+1, 14:+2, 15:+2, 16:+3, 17:+3, 18:+4}

#print(stats)
#int(ability_modifiers[(stats[5])])


#Output with character information

if (charClass) == 'Barbarian':
    print('')
    print('The stats for', (charName),'are: ')
    print('Constitution:  ', (stats[0]), '\tConstitution modifier is:', ability_modifiers[(stats[0])])
    print('Strength:      ', (stats[1]), '\tStrength modifier is:',ability_modifiers[(stats[1])])
    print('Dexterity:     ', (stats[2]), '\tDexterity modifier is:', ability_modifiers[(stats[2])])
    print('Charima:       ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
    print('Wisdom:        ', (stats[4]), '\tWisdon modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]), '\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 12 + int(ability_modifiers[(stats[0])]))

if (charClass) == 'Bard':
    print('')
    print('The stats for', (charName),'are: ')
    print('Charisma:      ', (stats[0]),'\tCharisma modifier is:', ability_modifiers[(stats[0])])
    print('Dexterity:     ', (stats[1]),'\tDexterity modifier is:',ability_modifiers[(stats[1])])
    print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
    print('Wisdom:        ', (stats[3]), '\tWisdon modifier is:', ability_modifiers[(stats[3])])
    print('Strength:      ', (stats[4]), '\tStrength modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))

if (charClass) == 'Cleric':
    print('')
    print('The stats for', (charName),'are: ')
    print('Wisdom:        ', (stats[0]),'\tWisdon modifier is:', ability_modifiers[(stats[0])])
    print('Strength:      ', (stats[1]),'\tStrength modifier is:',ability_modifiers[(stats[1])])
    print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
    print('Charima:       ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
    print('Dexterity:     ', (stats[4]), '\tDexterity modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))

if (charClass) == 'Druid':
    print('')
    print('The stats for', (charName),'are: ')
    print('Wisdom:        ', (stats[0]),'\tWisdon modifier is:', ability_modifiers[(stats[0])])
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
    print('Wisdom:        ', (stats[4]), '\tWisdon modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 10 + int(ability_modifiers[(stats[1])]))

if (charClass) == 'Monk':
    print('')
    print('The stats for', (charName),'are: ')
    print('Dexterity:     ', (stats[0]),'\tDexterity modifier is:', ability_modifiers[(stats[0])])
    print('Wisdom:        ', (stats[1]),'\tWisdon modifier is:',ability_modifiers[(stats[1])])
    print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
    print('Charisma:      ', (stats[3]), '\tCharisma modifier is:', ability_modifiers[(stats[3])])
    print('Intelligence:  ', (stats[4]), '\tIntelligence modifier is:', ability_modifiers[(stats[4])])
    print('Strength:      ', (stats[5]),'\tStrength modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 8 + int(ability_modifiers[(stats[2])]))

if (charClass) == 'Ranger':
    print('')
    print('The stats for', (charName),'are: ')
    print('Dexterity:     ', (stats[0]), '\tDexterity modifier is:', ability_modifiers[(stats[0])])
    print('Wisdom:        ', (stats[1]), '\tWisdon modifier is:',ability_modifiers[(stats[1])])
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
    print('Wisdom:        ', (stats[4]), '\tWisdon modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 10 + int(ability_modifiers[(stats[1])]))

if (charClass) == 'Rogue':
    print('')
    print('The stats for', (charName),'are: ')
    print('Dexterity:     ', (stats[0]),'\tDexterity modifier is:', ability_modifiers[(stats[0])])
    print('Charisma:      ', (stats[1]),'\tCharisma modifier is:',ability_modifiers[(stats[1])])
    print('Strength:      ', (stats[2]), '\tStrength modifier is:', ability_modifiers[(stats[2])])
    print('Constitution:  ', (stats[3]), '\tConstitution modifier is:', ability_modifiers[(stats[3])])
    print('Wisdom:        ', (stats[4]), '\tWisdon modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 8 + int(ability_modifiers[(stats[3])]))

if (charClass) == 'Sorcerer':
    print('')
    print('The stats for', (charName),'are: ')
    print('Charisma:      ', (stats[0]),'\tCharisma modifier is:', ability_modifiers[(stats[0])])
    print('Dexterity:     ', (stats[1]),'\tDexterity modifier is:',ability_modifiers[(stats[1])])
    print('Constitution:  ', (stats[2]), '\tConstitution modifier is:', ability_modifiers[(stats[2])])
    print('Wisdom:        ', (stats[3]), '\tWisdon modifier is:', ability_modifiers[(stats[3])])
    print('Intelligence:  ', (stats[4]), '\tIntelligence modifier is:', ability_modifiers[(stats[4])])
    print('Strength:      ', (stats[5]),'\tStrength modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 6 + int(ability_modifiers[(stats[2])]))

if (charClass) == 'Warlock':
    print('')
    print('The stats for', (charName),'are: ')
    print('Charisma:      ', (stats[0]),'\tCharisma modifier is:', ability_modifiers[(stats[0])])
    print('Constitution:  ', (stats[1]),'\tConstitution modifier is:',ability_modifiers[(stats[1])])
    print('Dexterity:     ', (stats[2]), '\tDexterity modifier is:', ability_modifiers[(stats[2])])
    print('Wisdom:        ', (stats[3]), '\tWisdon modifier is:', ability_modifiers[(stats[3])])
    print('Strength:      ', (stats[4]), '\tStrength modifier is:', ability_modifiers[(stats[4])])
    print('Intelligence:  ', (stats[5]),'\tIntelligence modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 8 + int(ability_modifiers[(stats[1])]))

if (charClass) == 'Wizard':
    print('')
    print('The stats for', (charName),'are: ')
    print('Intelligence:  ', (stats[0]),'\tIntelligence modifier is:', ability_modifiers[(stats[0])])
    print('Constitution:  ', (stats[1]),'\tConstitution modifier is:',ability_modifiers[(stats[1])])
    print('Dexterity:     ', (stats[2]), '\t Dexterity modifier is:', ability_modifiers[(stats[2])])
    print('Wisdom:        ', (stats[3]), '\t Wisdon modifier is:', ability_modifiers[(stats[3])])
    print('Charisma:      ', (stats[4]), '\t Charisma modifier is:', ability_modifiers[(stats[4])])
    print('Strength:      ', (stats[5]),'\t Strength modifier is:', ability_modifiers[(stats[5])])
    print('Hit Points:    ', 6 + int(ability_modifiers[(stats[1])]))