option=int(input("Enter option number 1-4: "))
a=int(input("Enter value for a: "))
b=int(input("enter value for b: "))
if option== 1:
	print(a+b)
elif option==2:
	print(a-b)
elif option==3:
	print(a*b)
elif option==4:
	print(a/b)
else:
	print("Invalid input, please enter a number from 1-4")
