import json

# Open the JSON file and load it into a Python list
with open('students.json', 'r') as file:
    class_list = json.load(file)

#Output notification to the user
print("Original Student List:")

#Call print function
print(class_list)

#Add fictional student
new_student = {
    "last_name": "Kuenning",
    "First_name": "Kuenning",
    "id": "A76018711",
    "email": "Kuenning.Kristopher@bellevue.edu"
}

#Append new student to class list
class_list.append(new_student)

#Notify and print updated list
print("\nUpdated Student List (after adding new student):")

#Call print function
print(class_list)

#Use the JSON dump() function to append the new data to the .json file
with open('students.json', 'w') as file:
    json.dump(class_list, file, indent=4)

#output notification to the user that the .json file was updated
print("\nThe new student has been added to the 'students.json' file.")