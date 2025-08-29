#4-1
pizzas = ['Carbonara', 'Salami', 'Margherita', 'Diavola']

for pizza in pizzas:
    print(f"I hecking love {pizza} pizza!!")

print("Man I hecking love pizza you guys")

#4-11
my_pizzas = pizzas
friend_pizzas = pizzas[:]

my_pizzas.append('idk')
friend_pizzas.append('Pepperoni')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)