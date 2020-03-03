import pyinputplus as pyip

print('It\'s time to make a sandwich. Please select your options')

#Creation of prompts that are used when asking for input using pyip
breadSelect = ('Select your bread.\n1.Wheat, 2.White, or 3.Sourdough\n')
proteinSelect = ('Select your protein.\n1.Chicken, 2.Turkey, 3.Ham, or 4.Tofu\n')
cheeseSelect = ('Do you want cheese?  Additional $0.50\n')
typeOfCheese = ('Select your cheese\n1.Cheddar, 2.Swiss, or 3.Mozarella\n')
condimentSelect = ('Do you want any condiments?  $0.25 each\n')
mayoSelect = ('Do you want mayo?\n')
mustardSelect =('Do you want mustard?\n')
lettuceSelect = ('Do you want lettuce?\n')
tomatoSelect = ('Do you want tomato?\n')

#String that will eventually display all ingredients of the sandwich
sandwichToppings = 'Your sandwich has '

#Float value that will be the total cost of the sandwich and be used to display the final price
sandwichCost = 4.00

#List created to store condiment strings
condiments = []

#Asks for input of bread type
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt = breadSelect, numbered = True)
sandwichToppings += bread + ' bread'

#Asks for input of protein type
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt = proteinSelect, numbered = True)
sandwichToppings += ', ' + protein + ' protein'

#Asks if user wants cheese. If yes, asks for input of cheese type
#Also, the price of cheese is added to the total cost
cheese = pyip.inputYesNo('Do you want cheese?\n')

if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'], prompt = typeOfCheese, numbered = True)
    sandwichToppings += ', ' + cheeseType + ' cheese'
    sandwichCost += 0.50

#Asks if user wants any condiments. If yes, it adds each condiment to condiment list
#Also, the price of each condiment is added to the total cost
addOns = pyip.inputYesNo('Do you want mayo, mustard, lettuce, or tomato?\n')

if addOns == 'yes':
    mayo = pyip.inputYesNo(mayoSelect)
    sandwichToppings += ', '

    if mayo == 'yes':
        condiments.append('mayo')
        sandwichCost += 0.25

    mustard = pyip.inputYesNo(mustardSelect)
    if mustard == 'yes':
        condiments.append('mustard')
        sandwichCost += 0.25

    lettuce = pyip.inputYesNo(lettuceSelect)
    if lettuce == 'yes':
        condiments.append('lettuce')
        sandwichCost += 0.25

    tomato = pyip.inputYesNo(tomatoSelect)
    if tomato == 'yes':
        condiments.append('tomato')
        sandwichCost += 0.25

    #Adds 'and' before the last condiment item
    listLength = len(condiments)
    condiments.insert(listLength-1, 'and ' + condiments[listLength-1])
    del condiments[listLength]
    sandwichToppings += ', '.join(condiments)

#Prints the sandwich ingredients and cost of the sandwich
print(sandwichToppings)
print('Your sandwich costs $' + str(sandwichCost))

