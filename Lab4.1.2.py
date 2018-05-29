import math
print ("Determine how many reams of paper you need:")
print ("Enter number of pages in report:")
reportPages = int(input ())
print ("Enter number of attendees:")
attendees = int(input ())
print ("Enter number of extra reports:")
extraReports = int(input ())
print ("Enter ream size:")
reamSize = int(input ())

totalPages = reportPages * (attendees + extraReports)
totalReams = math.ceil(totalPages / reamSize)

print("You need " + str(totalReams) + " reams of paper.")
