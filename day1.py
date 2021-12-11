input_file = open("day1_input.txt", "r")
file_content = input_file.read()
content_list = file_content.split("\n")
input_file.close()

count = 0
for prev, cur in zip(content_list, content_list[1:]):
  if int(prev) < int(cur):
    count += 1
    
print(f"day 1 quiz 1: how many bigger step? {count}")

# quiz 2
three_list = []
for one, two, three in zip(content_list, content_list[1:], content_list[2:]):
  three_list.append(int(one) + int(two) + int(three))
  
three_count = 0
for prev, cur in zip(three_list, three_list[1:]):
  if int(prev) < int(cur):
    three_count += 1
    
print(f"day 1 quiz 2: how many bigger step? {three_count}")