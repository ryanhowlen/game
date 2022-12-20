class Hero():
  def __init__ (self, health = 100, damage = 20, status = "Alive"):
    self.health = health
    self.damage = damage
    self.status = status
    

  def attack(self):
    if enemy == "goblin":
      goblin.health -= self.damage
    elif enemy ==  "fire slug":
      fire_slug.health -= self.damage
    elif enemy == "ice troll":
      ice_troll.health -= self.damage

  def cast_fire(self):
    if enemy == "goblin":
      goblin.health -= self.damage
    elif enemy ==  "fire slug":
      fire_slug.health -= self.damage / 2
    elif enemy == "ice troll":
      ice_troll.health -= self.damage * 3

  def cast_water(self):
    if enemy == "goblin":
      goblin.health -= self.damage
    elif enemy ==  "fire slug":
      fire_slug.health -= self.damage * 3
    elif enemy == "ice troll":
      ice_troll.health -= self.damage / 2

  def die(self):
    print("You have died.")
    player.status = "Dead"

    
    
class Monster():
  def __init__ (self, name = "none", health = 100, damage = 10, status = "Alive"):
    self.name = name
    self.health = health
    self.damage = damage
    self.status = status

  


  def die(self):
    print(self.name, "has died.")
    self.status = "Dead"

class Fire_monster(Monster):
  def __init__(self, name,health, damage, status):
    super().__init__(name, 200, 20, status)

class Ice_monster(Monster):
  def __init__(self,name, health, damage, status):
    super().__init__(name, 200, 20, status)

player = Hero()

goblin = Monster("Goblin")

fire_slug = Fire_monster("Fire Slug", 200, 20, "Alive")

ice_troll = Ice_monster("Ice Troll", 200, 20, "Alive")



while player.status == "Alive":

  print("You face", goblin.name + "!")
  print(" ")
  while goblin.status == "Alive":
    enemy = "goblin"
    

    attack = int(input("What will you do??:  (1)Attack    (2)Cast Fire    (3)Cast Water "))

    if attack == 1:
      print("You attack the monster!")
      player.attack()
      
    
    elif attack == 2:
      print("You cast a fireball!")
      player.cast_fire()
      

    elif attack == 3:
      print("You cast a jet of water!")
      player.cast_water()
      
      
    
    else:
      print("That isn't an option.")

    
    
    print("the monster has", goblin.health, "life remaining")
    if goblin.health <= 0:
        goblin.die()
    else:
      print(goblin.name, "Attacks!")
      player.health -= goblin.damage
      print("You have", player.health , "Health remaining")
      if player.health <=0:
        player.die()
        break
    
  if player.status != "Alive":
      break   


  print(" ")
  print("##################################################################################")
  print(" ")
  print("ROUND 2")
  print(" ")

  player.health = 100

  print("You face", fire_slug.name + "!")
  print(" ")

  while fire_slug.status == "Alive":
    enemy = "fire slug"
    

    attack = int(input("What will you do??:  (1)Attack    (2)Cast Fire    (3)Cast Water "))

    if attack == 1:
      print("You attack the monster!")
      player.attack()
      
    
    elif attack == 2:
      print("You cast a fireball!")
      player.cast_fire()
      print("It wasn't effective")

    elif attack == 3:
      print("You cast a jet of water!")
      player.cast_water()
      print("You hit the enemy's weakness!")
      
    
    else:
      print("That isn't an option.")
    
    print("the monster has", fire_slug.health, "life remaining")
    if fire_slug.health <= 0:
        fire_slug.die()
    else:
      print(fire_slug.name, "Attacks!")
      player.health -= fire_slug.damage
      print("You have", player.health , "Health remaining")
      if player.health <=0:
        player.die()
        break
    

  if player.status != "Alive":
   break   


  print(" ")
  print("##################################################################################")
  print(" ")
  print("ROUND 3")
  print(" ")

  player.health = 100

  print("You face", ice_troll.name + "!")
  print(" ")

  while ice_troll.status == "Alive":
    enemy = "ice troll"
    

    attack = int(input("What will you do??:  (1)Attack    (2)Cast Fire    (3)Cast Water "))

    if attack == 1:
      print("You attack the monster!")
      player.attack()
      
    
    elif attack == 2:
      print("You cast a fireball!")
      player.cast_fire()
      print("You hit the enemy's weakness!")
      

    elif attack == 3:
      print("You cast a jet of water!")
      player.cast_water()
      print("It wasn't effective")
      
      
    
    else:
      print("That isn't an option.")
    
    print("the monster has", ice_troll.health, "life remaining")
    if ice_troll.health <= 0:
        ice_troll.die()
    else:
      print(ice_troll.name, "Attacks!")
      player.health -= ice_troll.damage
      print("You have", player.health , "Health remaining")
      if player.health <=0:
        player.die()
        break
  if player.status != "Alive":
   break  
    
  print("Congratualtions, you beat all of the enemies!")
  break
      