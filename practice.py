import random

Adice = random.randint(1,6)
Bdice = random.randint(1,6)

print('주사위 던지기')
print('주사위 1:', Adice)
print('주사위 2:', Bdice)
print()

print('실행할 연산의 종류를 입력하세요.')
print('1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 나머지 구하기')
cal = int(input('연산종류:'))

if cal == 1:
    result= (Adice+Bdice)
    print('덧셈 결과:', result)

elif cal == 2:
    result= (Adice-Bdice)
    print('뺄셈 결과:', result)

elif cal == 3:
    result= (Adice*Bdice)
    print('곱셈 결과:', result)

elif cal == 4:
    result= (Adice//Bdice)
    print('나눗셈 결과:', result)

elif cal == 5:
    result= (Adice%Bdice)
    print('나머지 구하기 결과:', result)

print('별찍기')

for i in range(1,(result+1)):
    print('*'*i)
