
userInput = 0

while True:
    try:
        userInput = int(input("Nhập vào một số n (Điều kiện: -100 <= n <= 100): "))
    except ValueError:
        print("Giá trị nhập vào không phải là số. Vui lòng nhập lại!")
        continue

    if -100 <= userInput <= 100:
        break


print(userInput)
