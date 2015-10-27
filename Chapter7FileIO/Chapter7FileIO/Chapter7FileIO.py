fileInput = open("employeeData.txt","r")
name = ""
address = ""
payRate = 0.0
RAISE = 0.5

#Read records inside fileInput
for record in fileInput:
    print(record)