import requests
import datetime
import json
from datetime import timedelta

mydate = datetime.datetime.now()
day = mydate.strftime("%Y%m%d")    
print (day)

dayofmonth = int(mydate.strftime("%d")) 

if dayofmonth == 1:
	flag = True
else:
	flag = False
	
def api(day):
	server_url = "http://api.goseek.cn/Tools/holiday?date="
	try:
		response = requests.get(server_url + day)
	except UnicodeDecodeError:
		print('please check network!')	
	else:
		timedata = json.loads(response.text)  
		daytype = int(timedata["data"]) 
	return daytype

daytype = api(day)

def typeday(daytype):
	if daytype == 0 or daytype == 2:
		message = "workday"
	else:
		message = "holiday"	
	return message
	
print(typeday(api(day)))

if daytype == 0 or daytype == 2:
	i = 0
	flag1 = False
	beforeday = [0 for i in range(dayofmonth-1)]
	testdaytype = [0 for i in range(dayofmonth-1)]
	while(i < dayofmonth-1):
		if flag:
			print ("Today is first workday of this month")
			break                           
		beforeday[i] = (mydate - datetime.timedelta(days =i+1)).strftime("%Y%m%d")
		testdaytype[i] = api(beforeday[i])
		print (beforeday[i])
		print (typeday(testdaytype[i]))
		if testdaytype[i] == 0 or testdaytype[i] == 2:  
			flag1 = True
			break
		i = i + 1
	if flag1:
		print ("Today is not first workday of this month")
	else:
		print ("Today is first workday of this month")
else:
	print ("Today is not first workday of this month")
