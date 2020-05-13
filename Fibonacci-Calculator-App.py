print("Welcome to the Fibonacci Calculator App")
n = int(input("How many no of fibonacci sequence would you like to compute : "))
print("The First " + str(n) + " of fibonacci sequence are : ")
fibo = [1, 1]
for i in range(n-2):
    fibo.append(fibo[i] + fibo[i+1])
for i in range(n):
    print(fibo[i])
print("The corresponding golden ratio value are : ")
for i in range(n-1):
    print(fibo[i + 1] / fibo[i])
print("The Ratio of consecutive fibonacci terms approaches Phi : " + str(fibo[-1] / fibo[-2]))
