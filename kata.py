def fizz_buzz():
    results = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results

# Run and print the results
for result in fizz_buzz():
    print(result)
