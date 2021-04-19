"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-13"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    is_vegetarian = False
    name = input("Name: ")
    print("Origin")
    print(Food.origins())
    origin = int(input(": "))
    is_v= input("Vegetarian(Y/N)")
    if is_v=="Y" or is_v=="y":
        is_vegetarian = True       
    calories = int(input("Calories: "))
    food = Food(name,origin,is_vegetarian,calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    line = line.strip()
    data = line.split("|")
    name = data[0]
    origin = int(data[1])
    is_vegetarian = bool(data[2])
    calories = int(data[3])
    food = Food(name,origin,is_vegetarian,calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    line = file_variable.readline()
    foods = []
    while line!='':
        line.strip()
        foods.append(read_food(line))
        line = file_variable.readline()
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for f in foods:
        file_variable.write(f.name)
        file_variable.write("|")
        file_variable.write(str(f.origin))
        file_variable.write("|")
        file_variable.write(str(f.is_vegetarian))
        file_variable.write("|")
        file_variable.write(str(f.calories))
        file_variable.write("\n")

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = []
    for f in foods:
        if f.is_vegetarian==True:
            veggies.append(f)
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = []
    for f in foods:
        if f.origin==origin:
            origins.append(f)
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total = 0
    count = 0
    for f in foods:
        total+=int(f.calories)
        count+=1
    avg = total//count
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    count = 0
    total = 0
    for f in foods:
        if f.origin == origin:
            total+=int(f.calories)
            count+=1
    avg = total//count

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    foods.sort()
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    for f in foods:
        print("{:<36s}{:<13s}{:<11s}{}".format(f.name,Food.ORIGIN[f.origin],str(f.is_vegetarian),str(f.calories)))

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    any_origin = False
    if origin==-1:
        any_origin = True
    any_cals = False
    if max_cals==0:
        any_cals = True
    any_veg = False
    if is_veg==False:
        any_veg = True
        
    for f in foods:
        if not any_origin and f.origin!=origin:
            continue
        if not any_cals and f.calories>max_cals:
            continue
        if  is_veg!=f.is_vegetarian:
            continue
        result.append(f)
    return result

def low_cal(foods, count):
    """
    -------------------------------------------------------
    Returns a list of foods with a calorie count less than count.
    Use: low_cal_foods = low_cal(foods, count)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        count - foods must have calories below count (int)
    Returns:
        returns
        low_cal_foods - a list of Food (list of Food)
    -------------------------------------------------------
    """
    low_cal_foods = []
    
    for food in foods:
        if food.calories<count:
            low_cal_foods.append(food)
    
    
    return low_cal_foods