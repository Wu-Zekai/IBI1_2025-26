# PSEUDOCODE:
# 1. DEFINE a class named 'food_item' to act as a template for nutritional data.
#    - Initialize with attributes: name, calories, protein, carbohydrates, and fat.
# 2. DEFINE a function 'report_daily_nutrition' that accepts a list of 'food_item' objects.
#    - Initialize total counters for calories, protein, carbs, and fat to zero.
#    - ITERATE through each item in the input list:
#        a. Add the item's calories to the total_calories.
#        b. Add the item's protein to the total_protein.
#        c. Add the item's carbohydrates to the total_carbs.
#        d. Add the item's fat to the total_fat.
#    - PRINT a formatted report showing the sum of all nutrients.
#    - EVALUATE health thresholds:
#        a. IF total_calories exceeds 2,500, PRINT a specific excess warning.
#        b. IF total_fat exceeds 90g, PRINT a specific excess warning.
# 3. CREATE example instances of the 'food_item' class (e.g., Apple, Steak, Pizza).
# 4. EXECUTE the function using different combinations of food items to test 
#    normal consumption and the warning logic for excessive intake.
# Define the class to represent a food item with its nutritional information

class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

# Define the function to calculate and report daily nutrition intake
def report_daily_nutrition(consumed_list):
    """
    Receives a list of food_item objects, calculates and reports the total nutrition intake
    """
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    # Iterate through the consumed food items and sum up the nutritional values
    for item in consumed_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    # Print the nutrition report
    print("--- 24-hour Nutrition Intake Report ---")
    print(f"Total Calories: {total_calories:.1f} kcal")
    print(f"Total Protein: {total_protein:.1f} g")
    print(f"Total Carbohydrates: {total_carbs:.1f} g")
    print(f"Total Fat: {total_fat:.1f} g")

    # Health warning logic
    if total_calories > 2500:
        print("Warning: Your calorie intake has exceeded 2,500 calories!")
    
    if total_fat > 90:
        print("Warning: Your fat intake has exceeded 90 g!")
    
    # Return the total nutrition as a dictionary (optional, for further processing)
    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbs": total_carbs,
        "fat": total_fat
    }

# Example usage of the food_item class and report_daily_nutrition function

apple = food_item("Apple", 60, 0.3, 15, 0.5)
steak = food_item("Steak", 600, 50, 0, 45)
pizza = food_item("Pizza", 2000, 80, 250, 70)

# Example 1: Healthy diet
print("Example 1: Healthy diet")
my_diet_1 = [apple, steak]
report_daily_nutrition(my_diet_1)

print("\n" + "="*30 + "\n")

# Example 2: Overeating
print("Example 2: Overeating")
my_diet_2 = [steak, pizza]
report_daily_nutrition(my_diet_2)