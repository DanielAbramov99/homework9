numbers: list[int] = []
count: list[int] = []
string: str
stop: int = -999
while True:
    number: int = int(input("enter your number:"))
    if number == stop:
        break
    if not 0 < number < 10:
        print("invalid number")
        continue
    numbers.append(number)
    numbers.count(number)
    print("statistics:", end="")
    for i in range(0, 10):
        if i == i:
            print(f"{[number]}:{numbers.count(number)} ", end="")
            print()
            break
        else:
            continue
print()
