fileInput = open("employeeData.txt","r")
fileOutput = open("updatedEmployeeData.txt","w")
name = ""
address = ""
delimiter = ","
newline = "\n"
payRate = 0.0
RAISE = 2.00

#Read records inside fileInput
for record in fileInput:
    #print(record)
    #print(record.strip())
    newlineNoReturn = record.strip()
    newRecord = newlineNoReturn.split(',')
    name = newRecord[0]
    address = newRecord[1]
    payRate = float(newRecord[2])
    payRate += RAISE
    print(name, " Pay Rate Updated To: ", payRate)
    recordOut = name + delimiter + address + delimiter + str(payRate) + newline
    fileOutput.write(recordOut)

fileInput.close()