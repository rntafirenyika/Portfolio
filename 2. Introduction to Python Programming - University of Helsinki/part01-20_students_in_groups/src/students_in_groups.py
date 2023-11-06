#Asks for the number of students on a course and the desired group size. The program then prints out the number of groups formed from the students on the course
num_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
if num_students % group_size == 0:
    num_groups = num_students // group_size
else:
    num_groups = (num_students // group_size) + 1
print(f"Number of groups formed: {num_groups}")