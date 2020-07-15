def add_time(start, duration):
   return new_time

    # print("5.add_time")
    #print(add_time("11:06 PM", "2:02"))
    print("new_time")
    print("Enter Q to Exit")
    
new_time = input("Enter choice new time:")
 

num1 = int(input("Enter current time: "))
num2 = int(input("Enter the continuous time: "))

if new_time == '1':
 new_time = (num1 + num2)
 # print("\nNumber 1 + Number 2 =", answer)
 print(num1, "+", num2, "=", add_time(num1,num2))
else:
  print("Invalid number")