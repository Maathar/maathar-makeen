from random import randint
x=True
d=randint(1,100)

while x:
    number=int(input("Guess a number:"))
    if number<1 or number>100:
        print("your guess is outside the range")
        
    elif number==d:
      print("your guess is correct")
      x=False
      break
    elif number>d:
        print("go lower")
    else:
        print("go higher")
      
        