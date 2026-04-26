# Write code below 💖
class Pokemon:
  def __init__(self, entry, name, types, description, level, region, is_caught,):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.level = level
    self.region = region
    self.is_caught = is_caught
  def speak(self):
    print(self.name + ', ' + self.name + " !")
  def display_details(self):
    print("Entry Number: " + str(self.entry))
    print("Name: " + self.name)
    if len(self.types) == 1:
      print("Type: " + self.types[0])
    else:
      print("Type: " + self.types[0] + " / " + self.types[1])
    print("Description: " + self.description)
    print("Level: " + str(self.level))
    print("Region: " + self.region)
    if self.is_caught == True:
      print(self.name + " has already been caught!")
    else:
      print(self.name + " has not been caught!")
pikachu = Pokemon(25, "Pikachu", ["Electric"], "Pikachu, an Electric-type Pokémon, is the first Pokémon owned by Ash Ketchum.", 25, "Kanto", True)
bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "Bulbasaur is known to be the first Pokémon introduced in the National Pokédex Order that is a genuine Pokémon.", 98, "Kanto", True)
slowpoke = Pokemon(79, "Slowpoke", ["Water", "Psychic"], "Slowpoke is a Water/Psychic-type Pokémon with a calm demeanor.", 37, "Kanto", False)

pikachu.speak()
pikachu.display_details()
print("\n")
bulbasaur.speak()
bulbasaur.display_details()
print("\n")
slowpoke.speak()
slowpoke.display_details()
