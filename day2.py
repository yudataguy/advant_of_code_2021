input_file = open("day2_input.txt", "r")
file_content = input_file.read()
content_list = file_content.split("\n")
input_file.close()

horizontal = 0
vertical = 0
for step in content_list:
  direction, number = step.split(" ")
  if direction == "up":
    vertical -= int(number)
  if direction == "down":
    vertical += int(number)
  if direction == "forward":
    horizontal += int(number)
    
print(f"day 2 quiz 1: how many area covered? {horizontal * vertical}")

# quiz 2 

new_horizontal = 0
new_vertical = 0
aim = 0

for step in content_list:
  direction, number = step.split(" ")
  if direction == "up":
    # new_vertical -= int(number)
    aim -= int(number)
  if direction == "down":
    # new_vertical += int(number)
    aim += int(number)
  if direction == "forward":
    new_horizontal += int(number)
    new_vertical += aim * int(number)
  
print(f"day 2 quiz 2: how many area covered? {new_horizontal * new_vertical}")