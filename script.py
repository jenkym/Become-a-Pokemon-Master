class Pokemon:
#Pokemon Class
  def __init__(self, name, genre, level = 5, xp = 0, is_knocked_out = False):
    #variables to define a pokemon
    self.name = name
    self.level = level
    self.genre = genre
    self.max_health = level * 10
    self.health = level * 10
    self.xp = xp
    self.max_xp = level * 10
    self.is_knocked_out = is_knocked_out
  
  def __repr__(self):
    #When printing the Pokemon object the below string is displayed
    return "{} is level {}. It has a {} hit points remaining. This is a pokemon of the {} type.".format(self.name, self.level, self.health, self.genre.lower())
  
  def level_up(self):
    #when xp reaches the maximum experience, it evolves
    print("{} is increasing level! The new level is: {}".format(self.name, self.level))
    self.level += 1
    self.max_xp = self.level * 10
  
  def knock_out(self):
    #method that knocks the pokemon out
    if self.health != 0:
      self.health = 0
    self.is_knocked_out = True
    print("{} is knocked out!".format(self.name))
  
  def revive(self):
    #method that revives the pokemon
    self.is_knocked_out = False
    self.health = 1
    print("{} has revived: current health is {}.".format(self.name, self.health))
    
  def lose_health(self, amount):
    #method that decreases pokemon's health
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    else:
      return "{} now has {} health.".format(self.name, self.health)
  
  def gain_health(self, amount):
    #methods that increases pokemon's health
    if self.health == 0:
      self.revive()
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
      print("{} now has {} health.".format(self.name, self.health))
  
  def attack(self, other):
    #method that inflicts damage to another pokemon when our pokemon attacks
    #our pokemon cannot attack if knocked out
    if self.is_knocked_out == True:
      print("{} cannot attack because is KO!".format(self.name))
      return
    #our pokemon has disadvantage
    if (self.genre == "Grass" and other.genre == "Fire") or (self.genre == "Fire" and other.genre == "Water") or (self.genre == "Water" and other.genre == "Grass"):
      print("The attack is not effective")
      other.lose_health(round(0.5 * self.level))
      if other.is_knocked_out:
        self.xp += 2 * other.level
        if self.xp > self.max_xp:
          self.xp -= self.max_xp
          self.level_up()
        elif self.xp == self.max_xp:
          self.xp = 0
          self.level_up()
    #our pokemon has advantage
    elif (self.genre == "Fire" and other.genre == "Grass") or (self.genre == "Water" and other.genre == "Fire") or (self.genre == "Grass" and other.genre == "Water"):
      print("{pokemon_name} has attacked {other_pokemon} and has inflicted {damage} damage!".format(pokemon_name = self.name, other_pokemon = other.name, damage = 2 * self.level))
      other.lose_health(2 * self.level)
      if other.is_knocked_out:
        self.xp += 2 * other.level
        if self.xp > self.max_xp:
          self.xp -= self.max_xp
          self.level_up()
        elif self.xp == self.max_xp:
          self.xp = 0
          self.level_up()
    #same types of pokemon
    elif (self.genre == other.genre):
      print("{pokemon_name} has attacked {other_pokemon} and has inflicted {damage} damage!".format(pokemon_name = self.name, other_pokemon = other.name, damage = self.level))
      other.lose_health(self.level)
      if other.is_knocked_out:
        self.xp += 2 * other.level
        if self.xp > self.max_xp:
          self.xp -= self.max_xp
          self.level_up()
        elif self.xp == self.max_xp:
          self.xp = 0
          self.level_up()

#tests
#bulbasaur = Pokemon("Bulbasaur", "Grass", 10)
#charmender = Pokemon("Charmender", "Fire", 10)
#squirtle = Pokemon("Squirtle", "Water", 20)
#print(bulbasaur)
#bulbasaur.attack(charmender)
#squirtle.attack(charmender)
#squirtle.attack(squirtle)
#charmender.knock_out()
#charmender.attack(bulbasaur)
#charmender.revive()
#charmender.gain_health(99)

#Subclasses of Pokemon class
class Charmender(Pokemon):
  def __init__(self, xp = 0, level = 5):
    super().__init__("Charmender", "Fire", xp, level)
    
  def evolve(self):
    print("{ch} is evolving!".format(ch = self.name))
    print("...")
    print("...")
  
  def level_up(self):
    super().level_up()
    if self.level == 20:
      self.evolve()
      self.name = "Charmilion"
      print("Charmender became {ch}!".format(ch = self.name))
    elif self.level == 35:
      self.name == "Charizard"
      print("Charmilion became {ch}!".format(ch = self.name))
      
    
class Bulbasaur(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Bulbasaur", "Grass", level)

class Squirtle(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Squirtle", "Water", level)

#tests
#charmender = Charmender()
#bulbasaur = Bulbasaur()
#print(charmender)

class Trainer:
  def __init__(self, name, pokemon_list, num_potions=0):
    self.name = name
    #max 6 pokemons
    self.pokemon_list = pokemon_list
    self.potions = num_potions
    self.active_pokemon = 0
  
  def __repr__(self):
    print("The trainer {name_trainer} has the following pokemon:".format(name_trainer = self.name))
    for pokemon in self.pokemon_list:
      print("- ",pokemon)
    return "The current active pokemon is {active}.".format(active = self.pokemon_list[self.active_pokemon].name)
      
  def switch_pokemon(self, new_active):
    #method to switch between active pokemons
    if (new_active >= 0) and (new_active < len(self.pokemon_list)):
      if self.pokemon_list[new_active].is_knocked_out:
        print("{} is knocked out! Choose another pokemon.".format(self.pokemon_list[new_active].name))
      elif new_active == self.active_pokemon:
        print("{} is already your active pokemon.".format(self.pokemon_list[new_active].name))
      else:
        self.active_pokemon = new_active
        print("Go {}! It's your turn!".format(self.pokemon_list[self.active_pokemon].name))
    else:
      print("Invalid choice. Please, choose another pokemon")
      
  def use_potion(self):
    if self.potions > 0:
      #Potion increases active pokemon health of 20
      self.potions -= 1
      self.pokemon_list[self.active_pokemon].gain_health(20)
      print("{name_pokemon} has now {health} hit points.".format(name_pokemon = self.pokemon_list[self.active_pokemon].name, health = self.pokemon_list[self.active_pokemon].health))
      if self.potions == 0:
        print("{name_trainer} has no more potions.".format(name_trainer = self.name))
      else:
        print("{name_trainer} has {num_potions} remaining potions.".format(name_trainer = self.name, num_potions = self.potions))
    else:
      print("{name_trainer} has no potions.".format(name_trainer = self.name))
  
  def attack_trainer(self, other):
    self.pokemon_list[self.active_pokemon].attack(other.pokemon_list[other.active_pokemon])
      
      
    

#tests
#charmender = Charmender(19, 60)
#bulbasaur = Bulbasaur(20)
#squirtle = Squirtle()
#new_charmender = Charmender()


#ash = Trainer("Ash", [charmender, #bulbasaur], 1)
#print(ash)
#ash.switch_pokemon(1)
#ash.use_potion()

#bulbasaur.knock_out()
#bulbasaur.revive()
#betty = Trainer("Betty", [bulbasaur, #bulbasaur, bulbasaur])
#ash.attack(betty)


  
  

  