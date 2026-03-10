#import module
import random
#list of students
first_student = input("First Student: ")
second_student = input("Second Student: ")
third_student = input("Third Student: ")
fourth_student = input("Fourth Student: ")
#list
list_of_students = [first_student, second_student, third_student, fourth_student]
#module randint
random.shuffle(list_of_students)
#show print
print("Follow the order of the presentation: \n{}.".format(', '.join(list_of_students)))
