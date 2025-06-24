print("📊 Mean and Median Calculator")
data = input("Enter numbers separated by commas: ")
numbers = [float(x.strip()) for x in data.split(",")]

# Mean
mean = sum(numbers) / len(numbers)

# Median
numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

print(f"Mean: {mean}")
print(f"Median: {median}")
