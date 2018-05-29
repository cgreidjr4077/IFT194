def pay(category, hours):
    hourlyRate = 15
    overtimeRate = 20
    salaryRate = 500
    if category == "salary":
        print (salaryRate)
    else:
        if category == "hourly":
            if hours > 40:
                overtimeHours = hours - 40
                print ((40 * hourlyRate) + (overtimeHours * overtimeRate))
            else:
                print (hours * hourlyRate)

print (pay("salary", 30))
print (pay("hourly", 44))

        
