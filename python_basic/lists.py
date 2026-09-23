item1=["Aayush","Aniket","mummy","papa"]
print(item1[1:2])
item1.append("mukul")
print(item1)
item1.insert(1,"kobra")
print(item1)

print("Aayush" not in item1)
print(item1.sort())
print("tota no. =",len(item1))

# list practice
# Initial Avengers team
avengers = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye"]

# 1. Calculate how many members are in the Avengers team
print("Total members:", len(avengers))

# 2. Add Spider-Man as a new member
avengers.append("Spider-Man")
print("After adding Spider-Man:", avengers)

# 3. Move Captain America before Iron Man
avengers.remove("Captain America")
avengers.insert(0, "Captain America")
print("After placing Captain America before Iron Man:", avengers)

# 4. Separate Thor and Hulk by moving Black Widow between them
avengers.remove("Black Widow")
avengers.insert(3, "Black Widow")
print("After separating Thor and Hulk:", avengers)

# 5. Remove original six Avengers and add new superheroes
original_six = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye"]

for hero in original_six:
    if hero in avengers:
        avengers.remove(hero)

new_heroes = ["Doctor Strange", "Vision", "Wanda", "Kate Bishop", "Ant-Man"]
avengers.extend(new_heroes)

print("After End Game:", avengers)

# 6. Sort list alphabetically
avengers.sort()
print("Sorted Avengers List:", avengers)

# Leader will be at index 0
print("New Leader:", avengers[0])