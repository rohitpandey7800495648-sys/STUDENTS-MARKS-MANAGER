# project number 2
students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}

# adding a student
while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists.")
            continue

        marks = []
        while len(marks) < 3:
            mark = int(input("Enter mark: "))

            if mark < 0 or mark > 100:
                print("Invalid mark, try again.")
            else:
                marks.append(mark)

        students[name] = marks
        print("Student added successfully.")

# stage 1 ; Averages
    elif option == 2:
        
        for name in students:
            total = 0

            for mark in students[name]:
                total += mark

            average = total / len(students[name])
            
# stage 2 ; Grades
            if average >= 85:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"

            print(f"Name : {name}, Average : {average:.2f} , Grade : {grade}")

# stage 3 ; Topper
    elif option == 3:
        topper = ""
        highest_average = 0

        for name in students:
            total = 0

            for mark in students[name]:
                total += mark

            average = total / len(students[name])

            if average > highest_average:
                highest_average = average
                topper = name

        print("Topper:", topper)

# stage 4 ; Exit
    elif option == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
