print("Think of a two numbers...")
input("Press Enter After You Thought of Your Number...")
print("\nMultiply the first number by 2...\nExample: if your number is 2 3 then 2x2")
input("Press Enter After You Done Multiplication...")
print("\nAdd 5 to your Answer...")
input("Press Enter After Addition...")
print("\nMultiply Your Answer by 5...")
input("Press Enter After Multiplication...")
print("\nAdd Second Number You Thought of before to the Final Answer...")

while True:
    number = input("\nType Your Final Answer: ")
    if number.isnumeric():
        magic = int(number) - 25
        answer = str(magic)
        if 25 <= int(number) < 35:
            print(f"Your First Number: '0' Your Second Number: '{answer[0]}'")
            break
        else:
            print(f"Your First Number: '{answer[0]}' Your Second Number: '{answer[1]}'")
            break
    else:
        print("Answer Must Be a Number")
