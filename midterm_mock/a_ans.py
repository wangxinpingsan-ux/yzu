s = input("input s ")
c = input("input c ")

index = ""
count = 0
removed = ""

for i, value in enumerate(s):
    if value == c:
        index += str(i) + " "
        count += 1
    else:
        removed += value

print(f"index: {index}")
print(f"count: {count}")
print(f"removed: {removed}")
