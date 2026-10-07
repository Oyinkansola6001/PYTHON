names = ["Peter", "Mayowa", "Sam", "Mary"]
print(names[0:3])
print(names)
names.append("Favour")
print(names)
names.insert(2, "John")
print(names)
print("Peter" in names)
print(len(names))

for name in names:
    print(name)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

i = 0
while i < len(numbers):
    print(numbers[i])
    i +=1


numbers = range(2, 10, 2)
for number in numbers:
    print(number)

numbers = (1, 2, 3, 4, 5)

