a = input()

sample = set()

for i in range(len(a)):
    for j in range(i, len(a)):
        sample.add(a[i:j+1])

print(len(sample))