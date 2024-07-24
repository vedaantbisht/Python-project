import random

print("==============")

print("Stone Paper Scissors lizard and spock")

print("==============")

print("1) ✊")

print("2) 🖐")

print("3) ✌")

print("4) 🦎")

print("5) 🖖")

player = int(input("pick up number(1 , 2 , 3 , 4 , 5):"))

while player not in [1 , 2 , 3 , 4 , 5]:

    player = int(input("Invalid number . pick up number(1 , 2 , 3 , 4 , 5):"))



cpu = random.randint(1,5)

choices = {1: "✊", 2: "🖐", 3: "✌" , 4: "🦎" , 5: "🖖"}

print(f"player : {choices[player]}")

print(f"cpu : {choices[cpu]}")

if player == cpu:

    print("its a tie")

elif player ==1 and cpu ==3:

    print("player won")

elif player ==3 and cpu ==2:

    print("player won")

elif player ==2 and cpu ==1:

    print("player won")

elif player ==1 and cpu ==4:

    print("player won")

elif player ==4 and cpu ==3:

    print("player won")

elif player ==5 and cpu ==3:

    print("player won")

elif player ==3 and cpu ==4:

    print("player won")

elif player ==4 and cpu ==2:

    print("player won")

elif player ==2 and cpu ==5:

    print("player won")    

elif player ==5 and cpu ==1:

    print("player won")    

else:

    print("cpu win")