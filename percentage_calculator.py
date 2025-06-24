print("📊 Percentage Calculator")
num = float(input("Enter the number: "))
percent = float(input("Enter the percentage you want to find: "))

result = (percent / 100) * num
print(f"{percent}% of {num} is {result}")
