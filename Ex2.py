salary1 = int(input("Enter salary for person 1"))
salary2 = int(input("Enter salary for person 2"))
salary3 = int(input("Enter salary for person 3"))

if salary1 >= 0 and salary2 >= 0 and salary3 >= 0:
    avg_salary = (salary1 + salary2 + salary3) // 3
    print ("Your average salary is", avg_salary, "RUB")
else:
    print("Error. Enter correct information")

