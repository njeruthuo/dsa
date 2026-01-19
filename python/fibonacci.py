import time


def fibonacci(number):
    if number <= 1:
        return number

    prev, curr = 0, 1
    for _ in range(2, number+1):
        prev, curr = curr, prev+curr

    return curr


def fibon(number):
    if number <= 1:
        return number

    return (fibon(number-1)+fibon(number-2))


# Test iterative
start = time.time()
result1 = fibonacci(12)
end = time.time()

difference_iterative = end - start
print(f"fibonacci(12) = {result1}, Time: {difference_iterative:.6f} seconds")

# Test recursive
start = time.time()
result2 = fibon(12)
end = time.time()
difference_recursive = end - start
print(f"fibon(12) = {result2}, Time: {difference_recursive:.6f} seconds")


if difference_iterative > difference_recursive:
    print("Iterative is computationally expensive than recursive")
else:
    print("Recursive is computationally expensive than iterative")
