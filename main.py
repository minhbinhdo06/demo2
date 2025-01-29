total = 0
number = []

print("Nhập tổng số phần từ mà bạn mong muốn: ")
n = int(input())    

for i in range(10):
    num = int(input(f"Nhập số thứ {i + 1}: "))
    total += num
    number.append(num)

print("----------------------------------")
print(f"Tổng số phần tử bạn đã nhập: {total}")
print(f"Các phần tử bạn đã nhập:{number}")  
print("T là số 1")
