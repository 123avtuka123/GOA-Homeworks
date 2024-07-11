user_input=input("enter your savings: ")

saving=float (user_input)

percent=0.05

saving=saving * (1 + percent)

ballance=str (saving)

message="amount of 1 year: " + ballance

print(message)