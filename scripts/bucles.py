print("NÚMEROS DEL 1 AL 10")
for i in range(1,11):
    print(i)

print("NÚMEROS PARES DEL 1 AL 20")
for i in range(1,21):
    if not(i%2==0):
        continue
    print(i)