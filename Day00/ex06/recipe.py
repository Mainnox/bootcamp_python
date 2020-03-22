import pickle
import os.path
import os

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def load_obj_without_input(name ):
    with open('obj/' + name, 'rb') as f:
        return pickle.load(f)

def loop_input_add(string, code = 0):
    while (1):
        check = 0
        if string:
            print(string)
        put = input()
        put = put.lower()
        if not put:
            continue
        if (code == 1):
            for i in put:
                if not i.isdigit():
                    check += 1
        if check > 0:
            continue
        put = put.lower()
        return (put)

def del_recipe():
    recipes = os.listdir("obj")
    while (1):
        print("Which recipe you want to delete ? (You can type quit for leaving)")
        for i in recipes:
            j = 0
            while j < len(i) - 4:
                print(i[j], end = '')
                j += 1
            print()
        put = input()
        put = put.lower()
        os.system('clear')
        if not put:
            continue
        if put == "quit":
            break
        if recipes.count(put + ".pkl") > 0:
            print("Type \"yes\" if you really want to delete " + put + " recipe ?")
            confirm = input()
            put = "obj/" + put + ".pkl"
            if confirm == "yes":
                os.remove(put)
                break
        else:
            print("No recipe got the name " + put)

def add_recipe():
    recipe = {}
    ingredients = []
    repeat = 0
    while (1):
        print("Give me a name for your recipe")
        name = input()
        name = name.lower()
        if not name:
            print("Empty name")
            continue
        if os.path.exists("obj/" + name + ".pkl"):
            print("Recipe already exist")
            continue
        else:
            break
    recipe["name"] = name
    recipe["meal"] = loop_input_add("What is the type of meal your recipe are ?")
    recipe["prep_time"] = loop_input_add("What is the preparation time of your recipe ? (In minutes)", 1)
    while (1):
        if repeat == 0:
            print("Give me those ingredients of your recipe. (One by one :))")
        ingredients.append(loop_input_add(""))
        if (ingredients[-1] == "yes"):
            ingredients.remove("yes")
            break
        repeat += 1
        print("Your ingredients are :" + str(ingredients)[1:-1] + "\nIf it's done type yes")
        continue
    recipe["ingredients"] = ingredients
    save_obj(recipe, recipe["name"])
    os.system('clear')
    print("Yours " + recipe["name"] + "\'s recipe is add to this wonderful cookbook !")

def print_recipe(to_print):
    print("Recipe for " + to_print["name"] + ":")
    print("Ingredients list: " + str(to_print["ingredients"])[1:-1] + ".")
    print("To be eaten for " + to_print["meal"] + ".")
    print("Takes " + str(to_print["prep_time"] + " minutes of cooking."))

def print_a_recipe():
    recipes = os.listdir("obj")
    while (1):
        print("Which recipe you want to print ? (You can type quit for leaving)")
        for i in recipes:
            j = 0
            while j < len(i) - 4:
                print(i[j], end = '')
                j += 1
            print()
        put = input()
        put = put.lower()
        os.system('clear')
        if not put:
            continue
        if put == "quit":
            break
        if recipes.count(put + ".pkl") > 0:
            to_print = load_obj(put)
            print_recipe(to_print)
            break
        else:
            print("No recipe got the name " + put)

def print_all_recipe():
    count = 0
    recipes = os.listdir("obj")
    for i in recipes:
        to_print = load_obj_without_input(i)
        print_recipe(to_print)
        if count < len(recipes):
            print("\nPress enter for the next one")
            input()
            os.system('clear')
        count += 1

count = 0
os.system('clear')
while (1):
    if count == 0:        
        print("\t*************************************************")
        print("\t***    Welcome to the best cookbook ever !    ***")
        print("\t*************************************************\n")
    print("Please choose one of these options !\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print all recipe\n5: Quit")
    choose = input()
    os.system('clear')
    if choose == "1":
        add_recipe()
    elif choose == "2":
        del_recipe()
    elif choose == "3":
        print_a_recipe()
    elif choose == "4":
        print_all_recipe()
    elif choose == "5":
        print("Goodbye have a nice launch !")
        break
    else:
        print("Unknown commands")
    count += 1