# 구구단 3단을 출력
# 출력할 때, 3 X 3 = 9 와 같이 어떤 값을 곱하였는지도 함께 출력
i = 3
count = 0
while count < 9:
    count = count + 1
    result = i * count
    print("3 X", count, "=", result)

    for index in range(1, 10):
        number = 3*index
        print("3 X", index, "=", number)

for i in range(1, 10):
    for k in range(11, 20):
        print(i, k)

m = [[1,2,3],[4,5,6],[7,8,9]]
for i in m:
    for k in i:
        print(i)

# for 반복문을 두 번 사용해서
# 2차원 리스트의 요소를 모두 출력
num_list = [[10, 50],[20, 40],[30, 60],[40, 70]]
for i in num_list:
    for k in i:
        print(k)

# 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 구하여라
my_list = [[100,200],[400,800],[1000,1400]]
for i in my_list:
    sum = 0
    for num in i:
        sum = sum + num
    average = sum / len(i)
    print("평균값:", int(average))

my_list = [[100,200],[400,800],[1000,1400]]
for i in my_list:
    var = 0
    for j in i:
        var = var + j
    print(var/len(i))

# '10번 찍어 안 넘어가는 나무 없다' 속담을 while문을 사용하여 구현
number = 0
while number < 10 :
    number = number + 1
    print("나무를", str(number)+"번 찍었습니다.")
else:
    print("나무가 넘어갑니다.")

string = "매개변수를 입력하면, 입력한 매개변수가 화면에 출력됩니다."
print(len(string))

def 안녕하세요():
    print("안녕하세요. 만나서 반갑습니다.")

안녕하세요()

# 두 수를 더하는 함수
def add_numbers(number_1, number_2):
    result = number_1 + number_2
    print(result)
    return result

add_numbers(3, 5)
add_numbers(50, 30)

# 네 개의 덧셈 함수, 곱셈 함수 코드를 작성
def add_numbers(number_3, number_4, number_5, number_6):
    result_1 = number_3 + number_4 + number_5 + number_6
    print(result_1)
add_numbers(4,6,1,8)

def mul_numbers(number_3, number_4, number_5, number_6):
    result_2 = number_3 * number_4 * number_5 * number_6
    print(result_2)
mul_numbers(4,6,1,8)

# 별 피라미드 찍기
# 출력 결과가 아래와 같이 나오도록 코드를 작성
i = 0
while i < 10:
    i = i + 1
    print("*" * i)

# 1부터 100까지의 수를
# 2의 배수, 3의 배수, 5의 배수로
# 분류
numbers_1 = []
numbers_2 = []
numbers_3 = []
num = 0
while num < 100:
    num = num + 1
# 2의 배수는 numbers_1의 리스트에,
    if num%2 == 0:
        numbers_1.append(num)
# 3의 배수는 numbers_2의 리스트에,
    if num%3 == 0:
        numbers_2.append(num)
# 5의 배수는 numbers_3의 리스트에 저장하는 코드를 작성
    if num%5 == 0:
        numbers_3.append(num)
print(numbers_1)
print(numbers_2)
print(numbers_3)