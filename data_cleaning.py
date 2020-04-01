#David Samuel

#cleaning the data
import datetime #yyyy,mm,dd,h,m,s,ms
import math

# opening file and initial reading
filename = "dnc_complaint_numbers_2019-12-16.csv"

file_in = open(filename, "r")

data = [line for line in file_in]
cleaned = []
new = data[0].strip()+", Area_Code, Prefix, Day_of_Week, Time\n"
print(data[1])

# cleaning up entries without city and splitting the phone number into area code and prefix
for i in range(1,len(data)):
	line = data[i].split(",")
	if (len(line[0])==10 and line[4]=="Virginia" ): 
		number = line[0]
		area = number[0:3]
		prefix = number[3:6]
		line[-1] = line[-1].strip()
		line.append(str(area))
		line.append(str(prefix))
		cleaned.append(line)
# a = (cleaned[1][1])
# print(type(a))

# splitting up the timestamp into time and day of the week
for i in range(0,len(cleaned)):
	stamp = cleaned[i][2]
	if len(stamp) == 0: 
		print(i)
		break
	date, time = stamp.split(" ")
	#print(date, time)
	try:
		y,m,d = date.split("/")
	except ValueError:
		y,m,d = date.split("-")
	h,mi,s = time.split(":")

	try:
		day = datetime.datetime(int(y),int(m),int(d)).weekday()
	except ValueError:
		print(date)
		print(m,d,y)
		break
	newTime = format(int(h)+(int(mi)/60), ".2f")
	newTime = newTime + "\n"
	cleaned[i].append(str(day))
	cleaned[i].append(str(newTime))

# for i in range(5):
# 	print(cleaned[i])
# 	foo = (",".join(cleaned[i]))
# 	print((foo))
# 	print((data[i+1]))

# print(type(cleaned[3][7]))
# print(len(cleaned[3][7]))
# print((cleaned[3][7]) == float('nan'))

# combining the cleaned data and rewriting as csv
final = []
for i in range(0,len(cleaned)):
	if type(cleaned[i][7]) is str and len(cleaned[i][7]) != 0:
		final.append(cleaned[i])
file_out = open("cleaned.csv", "w")
file_out.write(new)
for d in final:
	foo = (",".join(d))
	file_out.write(str(foo))
print("Created cleaned data with ",len(final), "rows.")
file_out.close()	

file_in.close()
