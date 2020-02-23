from die1 import Die
import matplotlib.pyplot as plt
import pygal

die1 = Die()
die2 = Die()
list1 = []
list4 = []
#list2 = range(1000)


while len(list1) < 1000:
	list1.append(die1.roll_die())

while len(list4) < 1000:
	list4.append(die2.roll_die())

list3 = []
list2 = []
#print(die.sides+1)
for var in range(1, die1.sides+1):
	listy = list1.count(var)
	list3.append(listy)

for var in range(1, die2.sides+1):
	listy = list4.count(var)
	list2.append(listy)

print(list3)
print(list2)

hist = pygal.Bar()

hist.title = "Results"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Outcome"
hist.y_title = "Frequency of Outcome"

hist.add("Die1", list3)
hist.add("Die2", list2)
hist.render_to_file("die_trend.svg")
scat_labels = ['1','2','3','4','5','6']
plt.plot(scat_labels,list3)
plt.plot(scat_labels,list2)
plt.show()
