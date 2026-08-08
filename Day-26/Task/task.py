with open("DAY-26/task/file1.txt") as f:
    lines = f.readlines()
    numbers1 = [int(num.strip()) for num in lines]

with open("DAY-26/task/file2.txt") as f:
    lines = f.readlines()
    numbers2 = [int(num.strip()) for num in lines]

result = [num for num in numbers1 if num in numbers2]
print(result)
