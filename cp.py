import re
from datetime import datetime 

with open("README.md") as f:
    lines = f.readlines()
print(type(lines))
head = None

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

for line in lines:
    if re.search(r"^## \*\*Stage", line):
        head = line
    elif re.search(r"^\- \[ \]", line):
        if head != None:
            break
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"====== {timestamp} ==========")
print("You are in: ")
print(head)
print("Your current task is")
print(line)
print("================")

# data = dir(re)
# stoper = 1
# for i in data:
#     print(i)
#     if stoper % 5 == 0:
#         run = input()
#         if run == "q":
#             break
#     stoper += 1

# test = re.match(r"$## Stage \d: .*", "## **Stage 1: Fundamentals**")
# print(test)

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")