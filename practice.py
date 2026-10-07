def avg(a, b):
    print((a + b) / 2)

def average(a, b):
    return (a + b) / 2

    average(10, 20)
avg(20, 30)
final_score = (average(20, 90) *2) - average(10, 20) + average(10, 50)
print(final_score)


convocation_list = ["Davido", "Burna boy", "Wizkid", "Rema"]

def greet(alias):
    print("Congratulations to you, my dear " + alias)

for name in convocation_list:
    greet(name)
    greet(name)
    greet(name)



time = 10

if time >= 12:
    print("I will eat eba")
else:
    print("I will eat bread")



name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the program.")


birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"You are {age} years old.")




