low = int(input("Input the lower bound: "))
high = int(input("Input the higher bound: "))

if low < high :
    for number in range(low, high + 1) :
        print(number)
