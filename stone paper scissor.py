from random import randint

print('[1] Stone')
print('[2] Paper')
print('[3] Scissor')

rounds = 1
for a in range(5):
    com = randint(1,3)
    print ('Round: ', rounds)
    rounds = rounds + 1
    user = eval(input('User: '))
    print ('Computer:', com)

    if user == 1 and com == 1:
        print ('Winner: Draw')
    elif user == 2 and com ==2:
        print ('Winner: Draw')
    elif user == 3 and com == 3:
        print ('Winner: Draw')
    elif user == 1 and com == 2:
        print ('Winner: Computer')
    elif user == 1 and com == 3:
        print ('Winner: User')
    elif user == 2 and com == 1:
        print ('Winner: User')
    elif user == 2 and com == 3:
        print ('Winner: Computer')
    elif user == 3 and com == 1:
        print ('Winner: Computer')
    elif user == 3 and com == 2:
        print ('Winner: Computer')
        
    else:
        print('Invalid')

    print('\n')
    
from random import randint
  
player = input('rock (r), paper (p) or scissors (s)?')

if player == 'r':
  print('O', end=' ')
  
elif player == 'p':
  print('___', end=' ')
  
elif player == 's':
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if chosen == 1 :
  computer = 'r'
  print('O')
  
elif chosen == 2 :
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if player == computer:
  print('DRAW!')
  
elif player == 'r' and computer == 's':
  print('Player wins!')
  
elif player == 'r' and computer == 'p':
  print('Computer wins!')
  
elif player == 'p' and computer == 'r':
  print('Player wins!')
  
elif player == 'p' and computer == 's':
  print('Computer wins!')

elif player == 's' and computer == 'p':
  print('Player wins!')
  
elif player == "s" and computer == 'r':
  print('Computer wins!')

else:
  print('Huh?')
  
  
