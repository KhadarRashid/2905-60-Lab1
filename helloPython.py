name = input('Hello there, what is your name? ')
bday = input(f'When were you born {name}? ')

print(f"btw your name has {len(name)} letters")

if bday.lower() == 'january':
    print(f'What are the chances, its your birthday month! Happy birthday, belated or early! Whichever is the case {name}')
else: 
    print(f"{bday} is a great month to be born in")