from selenium import webdriver
import csv
import re
from itertools import islice
from urllib import parse



str1=r'openapp.jdmobile://virtual?params='
str6=r'{"category":"jump","des":"m","url":"'
str2=r'","m_param":{"jdv":"'
str3=r'"},"kepler_param":{"source":"kepler-open","channel":"'
str4=r'"},"keplerFrom":"1","keplerID":"'
str5=r'"}'
# chromedriver =r'C:\Users\wangyang50\AppData\Local\Google\Chrome\Application\chromedriver.exe'


csv_data = csv.reader(open("sourceurl.csv"))

result = []

errorFile = open("result.csv", 'w',newline ='')
writeCSV = csv.writer(errorFile)

driver = webdriver.Chrome()

for row in islice(csv_data, 1, None):
    tstr=row[1]
    print(tstr)
    # ttttttt=parse.quote_plus(str(tstr))
    print(tstr)
    tstr2=row[2]
    print(tstr2)
    driver.get(tstr2)# 获得cookie信息
    cookie=driver.get_cookies()#将获得cookie的信息打印
    for cookie in driver.get_cookies():
        if cookie['name']=='__jdv':
            if re.findall(r"^.*at_\d*", cookie['value']):
                tstr1=re.findall(r"^.*at_\d*", cookie['value'])
            else:
                tstr1=re.findall(r"^.*0_\w*", cookie['value'])
            print(tstr1[0])
            par=parse.quote_plus(str6+ tstr + str2 + tstr1[0] + str3 + row[5]+str4 + row[4]+str5)
            a=str1 +par
            row[3]=tstr1[0]
            row[6]=a
            writeCSV.writerow(row)

