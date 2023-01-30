print("Choose a starter, main and dessert")
starter = ["Starter", "Calamari", "garlic bread", "tomato soup"]
main = ["Main", "bologanse", "margarita", "spaghetti carbonara"]
dessert = ["Dessert", "sticky toffe pudding", "creme brule", "lemon sorbet"]
print(starter)
print(main)
print(dessert)

the_meal = []

print(f"Pleas select your starter from the list : {starter}")
starter = input()
the_meal.append(starter)
print(f"So far you have order : {the_meal}")
print(f"Pleas order your main course")
main = input()
the_meal.append(main)
print(f"So far you have order : {the_meal}")
print("Pleas choose a dessert")
dessert = input()
the_meal.append(dessert)
print(f"So far you have ordered : {the_meal}")
print(f"Your starter is the {the_meal[0]}. The main course youy have order is {the_meal[1]}. the dessert you have "
      f"ordered is {the_meal[2]}")
print("enjoy your meal!")


