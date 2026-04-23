import random

print("🛰️ Welcome to Space Adventure!👾")
print("\nYou are the captain of a spaceship exploring an unknown galaxy🌌...\n")

name = input("Enter your name, Captain: ")
hp = 20

print(f"\nCaptain {name}🌚, your journey begins now!\n")

# CHOICE 1
print("\nYou encounter two planets:")
print("1. Lunar Flare Sherbet 🪸")
print("2. Quagmire Thicket 🦥\n")

choice1 = input("Where do you go? (1/2): ")

if choice1 == "1":
    print("\nYou land on the icy planet. It's peaceful... but suddenly an alien appears!")

    alien_hp = 15

    while alien_hp > 0 and hp > 0:
        print(f"\nYour HP: {hp} | Alien HP: {alien_hp}")
        print("1. Attack")
        print("2. Heal")

        action = input("Choose your action: ")
        # Playeer Attack
        if action == "1":
            damage = random.randint(3, 6)
            alien_hp -= damage
            print(f"You hit the alien for {damage} damage!")
        # Player Heal
        elif action == "2":
            heal = random.randint(2, 5)
            hp += heal
            print(f"You healed for {heal} HP!")

        else:
            print("Invalid choice!")

        # Alien attacks
        if alien_hp > 0:
            alien_damage = random.randint(2, 5)
            hp -= alien_damage
            print(f"Alien hits you for {alien_damage} damage!")

    if hp > 0:
        print("\n💥 You defeated the alien and now you are the savior!")
    else:
        print("\n💀 You were defeated by the alien...")

# CHOICE 2
elif choice1 == "2":
    print("\nYou land on the swampy planet... it's too quiet.")
    print("Suddenly, your ship starts sinking into the ground!")

    print("\n1. Run back to ship")
    print("2. Explore further\n")

    choice2 = input("What do you do? (1/2): ")

    if choice2 == "1":
        print("\nYou did it! 🚀")
    elif choice2 == "2":
        print("\nYou missed it... 💀")
    else:
        print("\nInvalid choice")

else:
    print("\nInvalid choice!")
