# Coding 2.1

# task 1
print('# Task 1: Pi')

pi = 3.14           
print(f'3.14 type is: {type(pi)}')
str_pi = (str(pi))
print(f'String pi = {str_pi}')       

# Task 2: AGE
print('# Task 2: Age')

age = 21            
print(type(age)) 
text2 = '21'

print(f'age + text2 = {age +(int(text2))}')

# # Use of Mathematic Operators :- 2.5 Coding unit 
#   Task 3: -Calculate your BMI = Weight () by Height(m)2

print('#Task 3: -Calculate your BMI = Weight () by Height(m)2')
weight = 80
height = 180
bmi = (weight / (height**2))
print(f'Your BMI is {bmi}')
print(f'BMI type is: {type(bmi)}')

# Task 4:- Megan coffee shop

print('# Task 4: Coffee shop')
employees = ['Tom', 'John', 'Harry', 'Joe', 'Dan', 'Reuben']
rate = 8.59
hours = []

for x in employees:
    answer = float(input(f'How many hours did {x} work? '))
    hours.append(answer)
    print(f'{x} worked {answer} hours, earning £{rate * hours[-1]}')


# Task 5. Interesting Facts 

print('# Task 5. Interesting Facts ')
facts = {'Ian':'Likes Marmite on toast',
        'Iain':'Hates pizza',
        'Joe': 'Loves pasta',
        'Reuben':'Loves stilton'}
facts["Iain"] = 'Loves blueberries'
facts.update({'Dan': 'Likes sandwiches'})
print(f'Here is the list of facts: {facts}')



# Task 6. Airports

print('# Task 6. Airports')

uk_airports = [
    ("London Heathrow Airport", "LHR"),
    ("London Gatwick Airport", "LGW"),
    ("Manchester Airport", "MAN"),
    ("London Stansted Airport", "STN"),
    ("London Luton Airport", "LTN"),
    ("Birmingham Airport", "BHX"),
    ("Edinburgh Airport", "EDI"),
    ("Glasgow Airport", "GLA"),
    ("Bristol Airport", "BRS"),
    ("Newcastle Airport", "NCL")
]

for airport, code in uk_airports:
    print(f'{airport} has the airport code {code}')





