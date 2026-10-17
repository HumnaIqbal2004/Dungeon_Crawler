import random

class CharacterClasses:

    def __init__ (self, type: str, attack_power: float, health : float,):
        self.type = type
        self.attack_power = attack_power
        self.health = health
        
    def get_summary(self) -> str:
        return f"{self.type} selected!, Your attack is {self.attack_power} and your health is {self.health}!"

    def character_attack(self):
        return f"Your character hit the enemy for {self.attack_power}!" 

    def character_miss(self):
        return f"Your character missed :("

    

class EnemyClasses:
    def __init__(self, type: str, attack_power: float, health: float):
        self.type = type
        self.attack_power = attack_power
        self.health = health

    def enemy_summary(self):
        return f"You encountered a {self.type}, It has {self.health} hp!"

    def enemy_attack_prepare(self):
        return f"{self.type} prepares for an attack"

    def enemy_attack(self):
        return f"{self.type} attacks. You take {self.attack_power} of damage!"
    


class Styles:
    front_page = """
    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣴⣶⣶⣶⣴⣿⣯⣶⣶⣾⣧⣾⣿⣿⣿⣿⡆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢤⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢆⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠈⠉⠋⠉⠙⠛⠛⠛⠛⢛⣿⣿⠛⠛⠛⠙⠉⠉⠙⠪⠉⠁⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣄⠀⠀⢴⣄⣦⣴⣄⣀⡀⣠⣭⣿⡀⣀⡀⣠⣦⣴⣠⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣄⣉⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣍⣉⣁⣼⣷⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡻⣿⣿⣿⣿⣿⣟⣹⣿⣿⣿⣯⣙⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡹⢿⣿⣿⣿⡿⠻⣿⣿⣿⠿⠟⢿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣿⣿⣿⣧⠀⠀⠉⠀⠀⠀⣼⣿⣿⣿⣿⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⡿⠛⡏⠀⠀⠀⠀⢠⠀⢈⠻⠟⠻⣯⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢋⠀⠀⠀⠐⠢⠴⣆⣤⠏⠎⠊⠁⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⣤⣶⣶⣶⣶⣦⣴⣶⣶⣶⣶⣦⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠛⠙⠋⠉⠁⠙⠛⠙⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠀⠀⠀⠀⠀⣠⣄⣤⣤⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠻⠹⠛⠟⠻⠙⠿⠿⠊⠅⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    """

class adventure:
    def continue_forward(hero):
                
            encounters = ["chest", "enemy", "hall"]
    
            encounter = random.choices(encounters, weights=[2, 1, 4], k = 1)[0]
            if encounter == "hall":
                input("As you go deeper into the dungeon you notice something!")
                print("More walls..")
    
            if encounter == "chest":
                input("As you go deeper into the dungeon you notice something!")
                print("You see a chest")
    
            if encounter == "enemy":
                print("You encounter an enemy")
                enemy_fight_start(hero)




def enemy_fight_start(hero):
    enemies = [
                EnemyClasses("Goblin", 3, 10),
                EnemyClasses("Orc", 5, 20)
            ]

    

    which_enemies = ["Goblin", "Orc"]
    which_enemy = random.choices(which_enemies, weights=[3, 1], k = 1)[0]

    

    character_land_chances = ["hits", "misses"]
    character_land_enemy = random.choices(character_land_chances, weights = [3, 1], k = 1)[0]

    enemy_land_chances = ["hits", "misses"]
    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]

    
    
    
    if which_enemy == "Goblin":
        print(EnemyClasses.enemy_summary(enemies[0]))
        goblin = enemies[0]


        while hero.health > 0 and goblin.health > 0:

            if character_land_enemy == "hits":
                input(f"You hit goblin for {hero.attack_power} points of damage")
                goblin.health = goblin.health - hero.attack_power
                input(f"Goblin has {goblin.health}hp!")
                if goblin.health <= 0:
                    print("Goblin faints")
                    break

                character_land_chances = ["hits", "misses"]
                character_land_enemy = random.choices(character_land_chances, weights = [3, 1], k = 1)[0]
                

                if enemy_land_hero == "hits":
                    input(f"Goblin hits you for {goblin.attack_power} points of damage")
                    hero.health = hero.health - goblin.attack_power
                    input(f"Your {hero.type} currently has {hero.health}hp")
                    if hero.health <= 0:
                        #ADD A DIED FUNCTION
                        break

                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]

                else:
                    input("Goblin misses its attack")

                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]

            else:
                input(f"You miss")
                character_land_chances = ["hits", "misses"]
                character_land_enemy = random.choices(character_land_chances, weights = [3, 1], k = 1)[0]

                if enemy_land_hero == "hits":
                    input(f"Goblin hits you for {goblin.attack_power} points of damage")
                    hero.health = hero.health - goblin.attack_power
                    input(f"Your {hero.type} currently has {hero.health}hp")
                
                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]
                
                else:
                    input("Goblin misses its attack")
                
                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]     

    elif which_enemy == "Orc":
        print(EnemyClasses.enemy_summary(enemies[1]))
        Orc = enemies[1]
        
        
        while hero.health > 0 and Orc.health > 0:
        
            if character_land_enemy == "hits":
                input(f"You hit Orc for {hero.attack_power} points of damage")
                Orc.health = Orc.health - hero.attack_power
                input(f"Orc has {Orc.health}hp!")
                if Orc.health <= 0:
                    print("Orc faints")
                    break
        
                character_land_chances = ["hits", "misses"]
                character_land_enemy = random.choices(character_land_chances, weights = [3, 1], k = 1)[0]
                        
        
                if enemy_land_hero == "hits":
                    input(f"Orc hits you for {Orc.attack_power} points of damage")
                    hero.health = hero.health - Orc.attack_power
                    input(f"Your {hero.type} currently has {hero.health}hp")
                    if hero.health <= 0:
                    #ADD A DIED FUNCTION
                        break
        
                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]
        
                else:
                    input("Orc misses its attack")
        
                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]
        
            else:
                input(f"You miss")
                character_land_chances = ["hits", "misses"]
                character_land_enemy = random.choices(character_land_chances, weights = [3, 1], k = 1)[0]
        
                if enemy_land_hero == "hits":
                    input(f"Orc hits you for {Orc.attack_power} points of damage")
                    hero.health = hero.health - Orc.attack_power
                    input(f"Your {hero.type} currently has {hero.health}hp")
                        
                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]
                        
                else:
                    input("Orc misses its attack")
                        
                    enemy_land_chances = ["hits", "misses"]
                    enemy_land_hero = random.choices(enemy_land_chances, weights=[1, 2], k = 1)[0]
    
    print(f"__________________________________")
    print("---------YOU WON THE FIGHT---------")
    print(f"You currently have {hero.health}hp")
    print(f"__________________________________")


def main():


    

    maincharacter = [
                CharacterClasses("Mage", 5, 30), #elf
                CharacterClasses("Warrior", 3, 40), # warrior
                CharacterClasses("Assassin", 6, 25) #assassin
    
            ]
    

    print("-------------------------------------------------------------")
    print("               Welcome to RogueLite PYTHON ver.               ")
    print("___________________________🎮🔮🎮___________________________")
    print(Styles.front_page)

    input("Press ENTER to start dungeon decent!")

    
    
    chracter_selection_page = True

    while chracter_selection_page == True:
        race_selection = input("Please Select your Character type - (Mage, Warrior, Assassin): " ).lower()
        
        if race_selection == 'mage':
            print(CharacterClasses.get_summary(maincharacter[0]))
            chracter_selection_page = False
            hero = maincharacter[0]
            
            print(f"You current health is {hero.health}")
            
        elif race_selection == 'warrior':
            print(CharacterClasses.get_summary(maincharacter[1]))
            chracter_selection_page = False
            hero = maincharacter[1]
                        
            print(f"You current health is {hero.health}")

        elif race_selection == 'assassin':
            print(CharacterClasses.get_summary(maincharacter[2]))
            chracter_selection_page = False
            hero = maincharacter[2]
                        
            print(f"You current health is {hero.health}")

        else:
            print("Wrong input!!")


        input(f"Your {hero.type} enters the dungeon")

        
        input("Theres a chill in the air")
        input("You feel on edge")


    

    while hero.health > 0:

        print(adventure.continue_forward(hero))

    

    
    
            


    





if __name__ == '__main__':
    main()