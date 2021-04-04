a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and c + b > a:
    print("существует")
else:
    print("не существует")
if a + b > c and a + c > b and c + b > a and a==b and c!=a or a==c and a!=b or c==b and c!=a:
    print("равнобедренный")
if a==b==c:
    print("равносторонний")

