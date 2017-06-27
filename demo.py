# coding:utf-8

from bs4 import BeautifulSoup
import requests
import csv
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://bj.lianjia.com/zufang/dongcheng/pg{page}/'

page = 0

csv_file = open('fang.csv','wb')
csv_write = csv.writer(csv_file,delimiter=',')

while True:
    page += 1
    print '正在下载网页：',url.format(page=page)
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.content,'lxml')

    house_list = html.find('div',{'class','list-wrap'}).find_all('div',{'class','info-panel'})
    # print len(house_list)
    # break
    if not house_list:
        break
    for house in house_list:
        house_title = house.find('div',{'class',"where"}).get_text()
        # print house_title
        house_url = house.find('div',{'class','where'}).a['href']
        # print house_url
        house_location = house.find('div',{'class','con'}).get_text()
        # print house_location
        house_price = house.find('div',{'class','price'}).get_text()
        # print house_price
        csv_write.writerow([house_title,house_location,house_price,house_url])

csv_file.close()
def csv_to_xls(filename):
    myexcel = xlwt.Workbook(encoding = 'utf-8')
    mysheet = myexcel.add_sheet("sheet1")
    csvfile = open(filename,"rb")
    reader = csv.reader(csvfile)
    l = 0
    for line in reader:
        r = 0
        for i in line:
            mysheet.write(l,r,i)
            r=r+1
        l=l+1
    excel_filename = str(filename.split(".")[0]) + ".xls"
    myexcel.save(excel_filename)
    return excel_filename

csv_to_xls('fang.csv')




