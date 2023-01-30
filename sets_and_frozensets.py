#Set and Frozen sets

#lists and sets are very similar. sets are un orderd

#creating a set

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

#removing parts from the set
car_parts.discard("doors")
print(car_parts)

#add to a set
car_parts.add("windows")
print(car_parts)#

#Frozen sets are immutable
x = frozenset([1, 2, 3, 4, "Five"])
print(x)

