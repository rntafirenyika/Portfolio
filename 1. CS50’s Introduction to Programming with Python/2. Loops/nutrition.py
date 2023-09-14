"""
Prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit,
"""

nutrition_facts = [
{"Fruit": "Apple",  "Calories": 130},
{"Fruit": "Avocado",  "Calories": 50},
{"Fruit": "Banana",  "Calories": 110},
{"Fruit": "Cantaloupe",  "Calories": 50},
{"Fruit": "Grapefruit",  "Calories": 60},
{"Fruit": "Grapes",  "Calories": 90},
{"Fruit": "Honeydew Melon",  "Calories": 50},
{"Fruit": "Kiwifruit",  "Calories": 90},
{"Fruit": "Lemon",  "Calories": 15},
{"Fruit": "Lime",  "Calories": 20},
{"Fruit": "Nectarine",  "Calories": 60},
{"Fruit": "Orange",  "Calories": 80},
{"Fruit": "Peach",  "Calories": 60},
{"Fruit": "Pear",  "Calories": 100},
{"Fruit": "Pineapple",  "Calories": 50},
{"Fruit": "Plums",  "Calories": 70},
{"Fruit": "Strawberries",  "Calories": 50},
{"Fruit": "Sweet Cherries",  "Calories": 100},
{"Fruit": "Tangerine",  "Calories": 50},
{"Fruit": "Watermelon",  "Calories": 80},

]

user_fruit = input("Item: ").title()
for nutrition in nutrition_facts:
    if user_fruit == nutrition["Fruit"] :
        print("Calories: ", nutrition["Calories"])