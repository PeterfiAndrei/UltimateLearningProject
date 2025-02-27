num = 10  # int
price = 99.99  # float
name = "Alex"  # String
is_available = True  # boolean


def add(a, b):
    return a + b


print("Suma numerelor este:", add(8, num))

if add(num, 2) < 10:
    print("bigger than 10")
else:
    print("smaller than 10")

for i in range(1, 5, 2):
    print("Printing for", i)

i = 0
while i < 5:
    print("Printing while", i)
    i += 1
