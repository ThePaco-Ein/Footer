def daysInMonth(year, month):
    if month==1 or month==4 or month==6 or month==9 or month==11 :
        print(30)
    if month==2:
     if year % 4 == 0  and  (year% 100 != 0  or  year % 400 == 0):
         print(29)
     else:
         print(28)
    if month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print(31)


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]	
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)