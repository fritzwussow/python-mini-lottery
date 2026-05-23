
print('Willkommen in der Lotterie!')
number1 = int(input('Bitte gebe eine Zahl zwischen 1-49 ein: '))
number2 = int(input('Bitte gebe eine Zahl zwischen 1-49 ein: '))
number3 = int(input('Bitte gebe eine Zahl zwischen 1-49 ein: '))

#number1 = 5
#number2 = 9
#number3 = 42

if number1 == 5 and number2 == 9 and number3 == 42:
    print('Herzlichen Glückwunsch, du hast gewonnen!')
elif number1 == 999 and number2 == 999 and number3 == 999:
    print('Du hast die Geheimkombination entdeckt, dein Gewinn wird mit der Geheimzahl multipliziert!')
else:
    print('Du hast leider verloren ...')