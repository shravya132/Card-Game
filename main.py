from a2_support import *

"""Interactive card game"""

class Card(object):
    """
    Represents characteristics of a card in a card game. 
    
    """
    
    
    def get_damage_amount(self) -> int:
        """
        Returns amount of damage card deals. 

        Return: An integer value of damage amount.

        """
        return 0

    
    def get_block(self) -> int:
        """
        Returns amount of block card applies. 

        Return: An integer value of block amount. 

        """
        return 0

    
    def get_energy_cost(self) -> int:
        """
        Returns amount of energy cost required to play card.
        
        Return: An integer value of energy cost. 

        """
        return 1

    
    def get_status_modifiers(self) -> dict[str, int]:
        """
        Returns status modifiers card inflicts on target. 

        Return: A dictionary containing a string and integer value. 

        """
        return {}
    

    def get_name(self) -> str:
        """
        Returns the name of the card.  

        Return: A string value of given card name. 

        """
        return f"{self.__class__.__name__}"
    

    def get_description(self) -> str:
        """
        Returns a description of card characteristics. 

        Return: A string value of card description. 

        """
        return "A card."
    

    def requires_target(self) -> bool:
        """
        Identifies if a card requires a target to be played. 

        Return: A boolean value that if True, requires a target and
        if False, doesn't require a target to be played. 

        """
        return True 
    


    def __str__(self) -> str:
        """
        Returns a string representation of the class. 

        Return: A string value containing the card's name
        and its description.

        """
        return f"{self.get_name()}: {self.get_description()}"
    

    def __repr__(self) -> str:
        """
        Returns a string representation of instance to recreate it. 

        Return: A string value containing card instance. 

        """
        return f"{self.__class__.__name__}()"



class Strike(Card):
    """
    Represents a type of card called Strike.
    """
    def get_damage_amount(self) -> int:
        return 6
    

    def get_description(self) -> str:
        return f"Deal {self.get_damage_amount()} damage."



class Defend(Card):
    """
    Represents a type of card called Defend.
    """
    def get_block(self) -> int:
        return 5


    def requires_target(self) -> bool:
        return False


    def get_description(self) -> str:
        return f"Gain {self.get_block()} block."



class Bash(Card):
    """
    Represents a type of card called Bash.
    """
    def get_damage_amount(self) -> int:
        return 7


    def get_block(self) -> int:
        return 5


    def get_description(self) -> str:
        return (f"Deal {self.get_damage_amount()} damage. "
                f"Gain {self.get_block()} block.")

    
    def get_energy_cost(self) -> int:
        return 2



class Neutralize(Card):
    """
    Represents a type of card called Neutralize.
    """
    def get_damage_amount(self) -> int:
        return 3


    def get_energy_cost(self) -> int:
        return 0


    def get_status_modifiers(self) -> dict[str, int]:
        return {'weak': 1,'vulnerable': 2}


    def get_description(self) -> str:
        return (f"Deal {self.get_damage_amount()} damage. "
                f"Apply {self.get_status_modifiers()['weak']} weak. "
                f"Apply {self.get_status_modifiers()['vulnerable']} vulnerable.")



class Survivor(Card):
    """
    Represents a type of card called Survivor.
    """
    def get_block(self) -> int:
        return 8


    def get_status_modifiers(self) -> dict[str, int]:
        return {'strength': 1}


    def requires_target(self) -> bool:
        return False


    def get_description(self) -> str:
        return (f"Gain {self.get_block()} block and "
                f"{self.get_status_modifiers()['strength']} strength.")



class Entity(object):
    """
    Represents characteristics of an entity in a card game. 

    """


    def __init__(self, max_hp:int) -> None:
        """
        Parameters:
            max_hp: maximum hp of the entity.
            hp = hp of entity at the current stage.
            block = amount of block entity has.
            strength = amount of strength entity has.
            weak = amount of weakness entity has applied to them.
            vulnerable = amount of vulnerability entity has applied to them.
            
        """
        self._max_hp = max_hp
        self._hp = max_hp
        self._block = 0
        self._strength = 0
        self._weak = 0
        self._vulnerable = 0

        
    def get_hp(self) -> int:
        """
        Returns the hp of entity during the current stage. 

        Return: An integer of current hp.

        """
        return self._hp


    def get_max_hp(self) -> int:
        """
        Returns the maximum hp of entity.

        Return: An integer value of maximum entity hp.

        """
        return self._max_hp


    def get_block(self) -> int:
        """
        Returns the block amount entity has. 

        Return: An integer value fo block.

        """
        return self._block


    def get_strength(self) -> int:
        """
        Returns the current value strength of the entity.

        Return: An integer value of strength.
        """
        
        return self._strength


    def get_weak(self) -> int:
        """
        Returns the amount of weak entity has.

        Return: An integer value of weak.
        """
        return self._weak


    def get_vulnerable(self) -> int:
        """
        Returns the amount of vulnerability entity has.

        Return: An integer value of weak.
        """
        return self._vulnerable


    def get_name(self) -> str:
        """
        Returns the name of entity.

        Return: A string value containing the name of the entity.
        """
        return f"{self.__class__.__name__}"


    def reduce_hp(self, amount:int) -> None:
        """
        Function reduces the hp when given amount.

        Parameter:
            amount = number to reduce hp by.
        """
        self._amount = amount
        if self._block > 0:
            self._block -= self._amount
            if self._block < 0:
                self._hp += self._block
                self._block = 0
        else:
            self._hp -= self._amount
            if self._hp < 0:
                self._hp = 0

                
    def is_defeated(self) -> bool:
        """
        Returns True when entity is defeated and false when not.

        Return: A boolean when defeated or still alive.
        """
        if self._hp == 0:
            return True
        else:
            return False


    def add_block(self, amount:int) -> None:
        """
        Adds given amount to block.

        Parameter:
            amount = given number to increase block.
        """
        self._amount = amount
        self._block += amount


    def add_strength(self, amount:int) -> None:
        """
        Adds given amount to strength.

        Parameter:
            amount = given number to increase strength.
        """
        self._amount = amount
        self._strength += amount


    def add_weak(self, amount:int) -> None:
        """
        Adds given amount to weak.

        Parameter:
            amount = given number to increase weak.
        """
        self._amount = amount
        self._weak += amount


    def add_vulnerable(self, amount:int) -> None:
        """
        Adds given amount to vulnerable.

        Parameter:
            amount = given number to increase vulnerable.
        """
        self._amount = amount
        self._vulnerable += amount


    def new_turn(self) -> None:
        """
        Initiates when the entity starts a new turn.

        """
        #resets block to 0, and takes away 1 from weak and vulnerable.
        self._block = 0
        if self._weak > 0:
            self._weak -= 1
        if self._vulnerable >0:
            self._vulnerable -= 1

        
    def __str__(self) -> str:
        """
        Returns a current hp against maximum hp of entity. 

        Return: A string value of entity hp. 

        """
        return f"{self.get_name()}: {self._hp}/{self._max_hp} HP"


    def __repr__(self) -> str:
        """
        Returns a string representation of instance to recreate it. 

        Return: A string value containing entity instance. 

        """
        return f"Entity({self._max_hp})"



class Player(Entity):
    """
    Represents characteristics of a player in a card game. 

    """
    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        super().__init__(max_hp)
        """
        Parameters:
            cards = set of cards specific to each player.
            energy = set energy of player.
            card_deck = player's card deck.
            card_hand = available cards for olay in player's hand.
            card_discarded = used cards.
        """
        self._cards = cards
        self._energy = 3
        self._card_deck = cards if cards is not None else None
        self._card_hand = []
        self._card_discarded = []

        
    def get_energy(self) -> int:
        """
        Returns energy of player.
        Returns: An integer value of energy.
        """
        return self._energy


    def get_hand(self) -> list[Card]:
        """
        Returns the card hand of player.
        Cards in which are available to be played.

        Returns: List of cards. 
        """
        return self._card_hand 


    def get_deck(self) -> list[Card]:
        """
        Returns the card deck of all cards of player.
        Returns: List of cards.
        """
        return self._card_deck 


    def get_discarded(self) -> list[Card]:
        """
        Returns discarded deck containing used cards.
        Returns: List of cards.
        """
        return self._card_discarded

    def start_new_encounter(self) -> None:
        """
        A new encounter is started for the player.
        """
        #When the length of card hand is 0, a new encounter is triggered. 
        if len(self._card_hand) == 0:
            self._card_deck.extend(self._card_discarded)
            self._card_discarded = []

    def end_turn(self)-> None:
        """
        Ends the player's turn.
        """
        self._card_discarded += self._card_hand
        self._card_hand = []

    def new_turn(self) -> None:
        super().new_turn()
        self._card_hand = []
        draw_cards(self._card_deck, self._card_hand, self._card_discarded)
        self._energy = 3

    def play_card(self, card_name: str) -> Card | None:
        """
        Allows the user to play the chosen player's card.
        Returns: A card if played, otherwise returns none. 
        """
        #identifies if given card is in card hand
        play_card_names = [card.get_name() for card in self._card_hand]
        played = False
        for index, name in enumerate(play_card_names):
            if name == card_name and not played:
                card = self._card_hand[index]
                #if so, card is played
                #removes energy from player and adds card to discard pile
                if self._energy >= card.get_energy_cost():
                    self._energy -= card.get_energy_cost()
                    removed_item = self._card_hand.pop(index)
                    self._card_discarded.append(removed_item)
                    played = True
                    return card
                else:
                    return None
        if not played:
            return None

    def __repr__(self) -> str:
        return f"{self.get_name()}{self._max_hp, self._card_deck}"


class IronClad(Player):
    """
    A type of player called IronClad.
    """
    def __init__(self):
        max_hp = 80
        cards = [
            Strike(),
            Strike(),
            Strike(),
            Strike(),
            Strike(),
            Defend(),
            Defend(),
            Defend(),
            Defend(),
            Bash()
            ]
        super().__init__(max_hp, cards)
        
    def __repr__(self) -> str:
        return f"{self.get_name()}()"

class Silent(Player):
    """
    A type of player called Silent.
    """
    def __init__(self) -> None:
        max_hp = 70
        cards = [
            Strike(),
            Strike(),
            Strike(),
            Strike(),
            Strike(),
            Defend(),
            Defend(),
            Defend(),
            Defend(),
            Defend(),
            Neutralize(),
            Survivor()
            ]
        super().__init__(max_hp, cards)

    def __repr__(self) -> str:
        return f"{self.get_name()}()"



class Monster(Entity):
    """
    Represents characteristics of a monster in a card game. 

    """
    monster_count = 0
    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)
        """
        Parameters:
            id = monster's specific identifying number.
        """
        self._id = Monster.monster_count
        Monster.monster_count += 1


    def get_id(self) -> int:
        """
        Returns the id of monster.
        """
        return self._id


    def action(self) -> dict[str, int]:
        """
        The monster's action during battle.
        """
        raise NotImplementedError


    def __repr__(self) -> str:
        """
        Returns a string representation of instance to recreate it. 

        Return: A string value containing monster instance. 

        """
        return f"Monster({self._max_hp})"



class Louse(Monster):
    """
    A type of monster called Louse.
    """
    def __init__(self, max_hp: int) -> None:
        """
        Parameter:
            dmg_amount = amount of damage Louse inflicts.
        """
        super().__init__(max_hp)
        self._dmg_amount = random_louse_amount()
 
    def action(self) -> dict[str, int]:
        return {'damage': self._dmg_amount}

    def __repr__(self) -> str:
        return f"Louse({self._max_hp})"

class Cultist(Monster):
    """
    A type of monster called Cultist.
    """
    def __init__(self, max_hp:int):
        """
        Parameter:
            dmg_amount = amount of damage Cultist inflicts.
            weak_amount = weak amount of Louse
        """
        super().__init__(max_hp)
        self._dmg_amount = 0
        self._num_calls = 0
        self._first_call = True
        self._weak_amount = 0

    def action(self) -> dict[str, int]:
        if self._first_call:
            self._first_call = False
        else:
            self._dmg_amount = 6 + self._num_calls
        self._num_calls += 1
        self._weak_amount = (self._num_calls - 1) % 2
        return {'damage': self._dmg_amount, 'weak': self._weak_amount}

    def __repr__(self) -> str:
        return f"Cultist({self._max_hp})"
            

class JawWorm(Monster):
    """
    A type of monster called JawWorm.
    """
    def __init__(self, max_hp:int):
        """
        Parameter:
            dmg_amount = amount of damage JawWorm inflicts.
        """
        super().__init__(max_hp)
        self._dmg_taken = 0

    def action(self) -> dict[str, int]:
        dmg_taken_so_far = self._max_hp - self._hp
        self._block = ((dmg_taken_so_far + 1)//2)
        self._dmg_amount = (dmg_taken_so_far//2)    
        return {'damage': self._dmg_amount}

    def __repr__(self) -> str:
        return f"JawWorm({self._max_hp})"

        
class Encounter(object):
    """
    Represents characteristics of an encounter in a card game. 

    """
    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        Parameters:
            player = chosen player by user.
            monsters = monsters present in encounter for battle.
        """
        self._player = player
        self._monsters = monsters
        encounter_monsters = []
        for monster_tuple in self._monsters:
            name, max_hp = monster_tuple
            if name == 'Louse':
                monster = Louse(max_hp)
            elif name == 'Cultist':
                monster = Cultist(max_hp)
            elif name == 'JawWorm':
                monster = JawWorm(max_hp)
            else:
                pass
        
            encounter_monsters.append(monster)
        self._monsters = encounter_monsters
        self._player.start_new_encounter()
        
        print("New encounter!\n")
        self.start_new_turn()
        card_names = {"Strike": Strike(), "Defend": Defend(),
                      "Bash": Bash(), "Neutralize": Neutralize(),
                      "Survivor": Survivor()}
        self._card_names = card_names

    def start_new_turn(self) -> None:
        """
        Initiates a new turn.
        """
        self._player.new_turn()

    def end_player_turn(self) -> None:
        """
        Ends player turn.
        """
        self._player.end_turn()
        for monster in self._monsters:
            monster.new_turn()

    def get_player(self) -> Player:
        """
        Returns the player type.
        """
        return self._player

    def get_monsters(self) -> list[Monster]:
        """
        Gets monsters in encounter phase.
        Returns: List of monster/s in encounter.
        """
        return self._monsters

    def is_active(self) -> bool:
        """
        Determines whether monster is still alive.
        Returns: A boolean value, False if dead, True if alive.
        """
        empty = []
        if self._monsters == []:
            return False
        else:
            return True

    def player_apply_card(self, card_name: str, target_id: int | None = None) -> bool:
        """
        Player applied card to target.
        Parameters:
            card_name = card name used against target or used in battle.
            target_id = chosen target to use card against.
        """
        self._card_name = card_name
        self._target_id = target_id
        empty = []

        #check if it's the player's turn
        if self._player._card_hand == empty:
            return False
        else:
            pass

        #if card with given name requires a target bu no target was given
        if self._card_name in ["Strike", "Bash", "Defend",
                               "Neutralize", "Survivor"]:
            if self._card_names[self._card_name].requires_target() == True:
                if self._target_id is None:
                    return False
                else:
                    pass
        else:
            return False

        
        #if a target was given but no monster remains
        if self._target_id is not None: 
            for monster in self._monsters:
                x = monster.get_id()
                if x != self._target_id:
                    return False
                else:
                    pass
        

        #attempts to play card
        if self._player.play_card(self._card_name) == None:
            return False
        else:
            pass
        
    
        if self._card_names[self._card_name].get_block() > 0:
            self._player.add_block(self._card_names[self._card_name].get_block()
        )
        else:
            pass
                


        #any vulnerable or weak from card should be applied:
        for monster in self._monsters:
            x = monster.get_id()
            if self._target_id != None:
                if self._card_name == "Neutralize":
                    monster.add_weak(
                        self._card_names[self._card_name]
                        .get_status_modifiers()['weak']
                        )
                    monster.add_vulnerable(
                        self._card_names[self._card_name]
                        .get_status_modifiers()['vulnerable']
                        )
                elif self._card_name == "Survivor":
                    monster.add_strength(
                        self._card_names[self._card_name]
                        .get_status_modifiers()['strength']
                        )
                else:
                    pass

                #damage calculation 
                calc_dmg = (self._card_names[self._card_name]
                            .get_damage_amount()) + (self._player.get_strength()
                            )
                if monster.get_vulnerable() > 0:
                    calc_dmg *= 1.5
                else:
                    pass
                
                if self._player.get_weak() > 0:
                    calc_dmg *= 0.75
                else:
                    pass
                final_calc_dmg = int(calc_dmg)
                monster.reduce_hp(final_calc_dmg)
                if monster.is_defeated() == True:
                    self._monsters.remove(monster)
            else:
                pass

        return True

    def enemy_turn(self) -> None:
        """
        Starts enemy's turn. 
        """
        empty = []
        if self._player.get_hand() == []:
            for monster in self._monsters:
                monster.action()
                if ('weak' in monster.action() and
                    monster.action()['weak'] is not None):
                    self._player.add_weak(monster.action()['weak'])
                elif ('vulnerable' in monster.action() and
                      monster.action()['vulnerable'] is not None):
                    self._player.add_vulnerable(monster.action()['vulnerable'])
                elif ('strength' in monster.action() and
                      monster.action()['strength'] is not None):
                    monster.add_strength(monster.action()['strength'])
                else:
                    pass
                
            #damage calculation:
            calc_dmg = (monster.action()['damage']) + (monster.get_strength())
            if self._player.get_vulnerable() > 0:
                calc_dmg *= 1.5
            else:
                pass
                    
            if monster.get_weak() > 0:
                calc_dmg *= 0.75
            else:
                pass
            final_calc_dmg = int(calc_dmg)
            self._player.reduce_hp(final_calc_dmg)         
            self.start_new_turn()
        else:
            return None





def main():
    """
    The main code which user interacts with.
    """
    player = None  
    while not player:
        user_player = input("Enter a player type: ")
        if user_player == "ironclad":
            player = IronClad()
        elif user_player == "silent":
            player = Silent()
        else:
            print("Invalid input. Please choose either 'ironclad'"
                  " or 'silent' player types.")

    file_name = input("Enter a game file: ")
          
    encounters = read_game_file(file_name)
    monster_info = encounters[0]
    monsters = monster_info 
    encounter = Encounter(player, monsters)
    display_encounter(encounter)


    while True:
        empty = []
        if encounter.get_monsters() == empty:
            encounters.pop(0)
            if encounters == empty:
                encounter.end_player_turn()
                print(GAME_WIN_MESSAGE)
                break
            else:
                monster_info = encounters[0]
                monsters = monster_info
                encounter = Encounter(player, monsters)
                display_encounter(encounter)                        
                         
        command = input("Enter a move: ")
        
        if command.lower().startswith('inspect'):
            command_cards = command.split()
            second_word = command_cards[1]
            if second_word == "deck":
                print("\n", player.get_deck(), "\n", sep="")
            elif second_word == "discard":
                print("\n", player.get_discarded(), "\n", sep="")
     
        elif command.lower().startswith('describe'):
            command_cards = command.split()
            second_word = command_cards[1]
            if second_word == "Strike":
                print("\n", Strike().get_description(), "\n", sep="")
            elif second_word == "Defend":
                print("\n", Defend().get_description(), "\n", sep="")
            elif second_word == "Bash":
                print("\n", Bash().get_description(), "\n", sep="")
            elif second_word == "Neutralize":
                print("\n", Neutralize().get_description(), "\n", sep="")
            elif second_word == "Survivor":
                print("\n", Survivor().get_description(), "\n", sep="")

        elif command.lower().startswith('play'):
            command_cards = command.split()
            empty = []
            if encounter.get_monsters() != empty: 
                if len(command_cards) == 3:
                    card_name = command_cards[1]
                    target_id = int(command_cards[2])
                    if (encounter.player_apply_card(card_name, target_id) ==
                        False):
                        print(CARD_FAILURE_MESSAGE)
                    else:
                        display_encounter(encounter)
                        if encounter.get_monsters() == []:
                            encounter.end_player_turn()
                            print(ENCOUNTER_WIN_MESSAGE)
                        
                elif len(command_cards) == 2:
                    card_name = command_cards[1]
                    if encounter.player_apply_card(card_name) == False:
                        print(CARD_FAILURE_MESSAGE)
                    else:
                        display_encounter(encounter)
                        print(encounter.get_monsters())
                        if encounter.get_monsters() == []:
                            encounter.end_player_turn()
                            print(ENCOUNTER_WIN_MESSAGE)
            else:
                pass
            
            
        elif command == "end turn":
            empty = []
            encounter.end_player_turn()
            encounter.enemy_turn()
            if player.is_defeated() == True:
                print(GAME_LOSE_MESSAGE)
                break
            else:
                display_encounter(encounter)

            
    
    # Implement this only once you've finished and tested ALL of the required
    # classes.
    
    pass

if __name__ == '__main__':
    main()