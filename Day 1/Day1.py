# input data for the task

test_input = 0

if test_input:
    filename = ".\\Day 1\\day1_test.txt"
else:
    filename = ".\\Day 1\\day1_input.txt"

data_file_input = open(filename)
data_input = data_file_input.readlines()
#print(data_input)

# part 1

# separating input into two lists

temp_data = 0
left_list = []
right_list = []

for i in range(len(data_input)):
    temp_data = data_input[i].split()
    left_list.append(int(temp_data[0]))
    right_list.append(int(temp_data[1]))

# sorting the lists
left_list.sort()
right_list.sort()

# calculating distance

distance = 0
for i in range(len(left_list)):
    distance += abs(left_list[i]-right_list[i])

# output

print("Part 1 output: " + str(distance))


# part 2

# we will be using sorted lists from part 1

similarity_score = 0

# first we are doing the first iteration seperately in order to make comparisons with previous value from left list
# this will prevent doing the similarity calculation for the same value (it will copy the value for previous calculation)

similarity_iter = 0
repetitions = 0
while True:
    if right_list[0] < left_list[0]:
        right_list.pop(0)   # since we work on sorted lists, we won't need anything lower than the first value of the left list
    elif right_list[0] == left_list[0]:
        right_list.pop(0)
        repetitions += 1
    else:
        break
similarity_iter = left_list[0] * repetitions
similarity_score += similarity_iter

# now we make similarity calculations for other values in the left list

for i in range(1,len(left_list)):
    if left_list[i] == left_list [i-1]:
        similarity_score += similarity_iter
    else:
        repetitions = 0
        while True:
            if len(right_list) == 0:
                break
            if right_list[0] < left_list[i]:
                right_list.pop(0)   # since we work on sorted lists, we won't need anything lower than the first value of the left list
            elif right_list[0] == left_list[i]:
                right_list.pop(0)
                repetitions += 1
            else:
                similarity_iter = left_list[i] * repetitions
                similarity_score += similarity_iter
                break

print("Part 2 output: " + str(similarity_score))