mvps = ['Faker', 'fredy112', 'Youngbuck']

print(f"Dear {mvps[0]}, please come to my dinner party, ur the goat fr")
print(f"Dear {mvps[1]}, please come to my dinner party, ur the goat fr")
print(f"Dear {mvps[2]}, please come to my dinner party, ur the goat fr")

print(f"{mvps[0]} can't make it, since he's not really the goat")

mvps[0] = 'xPeke'

print(f"{mvps[0]} is the real goat and he will come to the dinner party instead, with {mvps[1]} and {mvps[2]}")

print("Guys I found a bigger table, we need more gamers")

mvps.insert(0, 'baussi')
mvps.insert(2, 'Bram van Polen')
mvps.insert(-1, 'Robert Gesink')

print(f"This is an invite for {mvps[0]}, {mvps[2]} and {mvps[-2]}")

disinvited = mvps.pop(-1)
print(f"Sorry, {disinvited} but there is no room for you at the table :(")
disinvited = mvps.pop(-1)
print(f"Sorry, {disinvited} but there is no room for you at the table :(")
disinvited = mvps.pop(-1)
print(f"Sorry, {disinvited} but there is no room for you at the table :(")
disinvited = mvps.pop(-1)
print(f"Sorry, {disinvited} but there is no room for you at the table :(")

print(f"Don't worry {mvps[0]} & {mvps[1]}, you are still invited")

del mvps[0]
del mvps[0]

print(mvps)