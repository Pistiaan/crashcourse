import matplotlib.pyplot as plt

x_values = range(1,1001)
#I'm trying to use more list comprehension
y_values = [value**2 for value in x_values]
#Nevermind, the book does this two sentences later

plt.style.use('Solarize_Light2')
#The book uses the seaborn theme, but this does not seem 
#to be available for me
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(labelsize = 14)
ax.axis([0, 1100, 0, 1100000]) #Is this really necessary?

plt.savefig("test.png")