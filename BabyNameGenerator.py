#This will generate baby names based on first, middle, and last names entered into it
import itertools, pprint
firstNames = []
print("""This program will take the first and middle names that you have picked out for your child
and then combine them so you can see how they look and therefore, help you make the best decision
when deciding on your child's name.""")
print('\nPlease enter the last name of the baby:')
lastName = [input()]
while True:
    print('\nEnter baby first name ' + str(len(firstNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    firstNames = firstNames + [name] # list concatenation
print('\nThe first names are:\n')
for name in firstNames:
    print('  ' + name)

middleNames = []
while True:
    print('\nEnter baby middle names ' + str(len(middleNames) + 1) +
      ' (Or enter nothing to stop.):')
    nameTwo = input()
    if nameTwo == '':
        break
    middleNames = middleNames + [nameTwo] # list concatenation
print('The middle names are:\n')
for nameTwo in middleNames:
    print('  ' + nameTwo)
possibleNames = [(x, y, z) for x in firstNames for y in middleNames for z in lastName]
print('\nPossible baby names are: \n')
pprint.pprint(possibleNames)
