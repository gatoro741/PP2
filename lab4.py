def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield str(i)  

n = int(input("Enter a number: "))
print(", ".join(even_numbers(n))) 