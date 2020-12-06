import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from datetime import datetime
import sys
import os
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=400)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(400, 140, window=entry1)
entry2 = tk.Entry(root)
canvas1.create_window(400, 100, window=entry2)
entry3 = tk.Entry(root)
canvas1.create_window(400, 60, window=entry3)
label5 = tk.Label(root, text='note: version 0.0.2 doesnt have any checks for wrong erp or passowrd. Please enter total courses as a single digit (e.g. 5)  ')
label5.config(font=('helvetica', 10))
canvas1.create_window(400, 10, window=label5)
label4 = tk.Label(root, text='total courses you have')
label4.config(font=('helvetica', 10))
canvas1.create_window(400, 40, window=label4)
label2 = tk.Label(root, text='ERP')
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 80, window=label2)
label3 = tk.Label(root, text='LMS Password')
label3.config(font=('helvetica', 10))
canvas1.create_window(400, 120, window=label3)
def getSquareRoot():
    ERP = entry2.get()
    password = entry1.get()
    t_course=entry3.get()
    int_t_course=int(t_course)+1

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    driver = webdriver.Chrome(executable_path=resource_path(r'/chromedriver_win32/chromedriver.exe'))

    driver.get('https://lms.iba.edu.pk/portal')

    # logging_in
    login = driver.find_element_by_xpath(r'//*[@id="eid"]').send_keys(ERP)
    password = driver.find_element_by_xpath(r'//*[@id="pw"]').send_keys(password)
    submit = driver.find_element_by_xpath(r'//*[@id="submit"]').click()
    driver.maximize_window()
    count = 0
    printable=[1,2,3,4,5,6]
    # Selecting Different Courses

    for j in range(1, int_t_course):
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, r'//*[@id="mastLogin"]/div[2]/a/i'))
            )
        finally:
            site = driver.find_element_by_xpath(r'//*[@id="mastLogin"]/div[2]/a/i').click()

        particular_course_xpath = r'//*[@id="otherSitesCategorWrap"]/div[4]/div[2]/ul/li[' + str(j) + r']/div/a/span'
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, particular_course_xpath))
            )
        finally:
            particular_course = driver.find_element_by_xpath(particular_course_xpath).click()
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, r'//*[@id="toolMenu"]/ul/li[5]/a/span[2]'))
            )
        finally:
            assignment_box = driver.find_element_by_xpath(r'//*[@id="toolMenu"]/ul/li[5]/a/span[2]').click()
        for i in range(2, 3):
            duedate = r'//*[@id="col1"]/div/div/form/div/table/tbody/tr[' + str(i) + ']/td[5]/span'
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, duedate))
                )
            finally:
                # duedate=r'//*[@id="col1"]/div/div/form/div/table/tbody/tr[2]/td[5]/span'
                t = driver.find_element_by_xpath(duedate).text
            if (len(t) == 21):
                r = t[:6] + t[7:]
                c = r[:17] + r[18:]
                format = '%b %d %Y %I:%M%p'
                datetime_str = datetime.strptime(c, format)
                now = datetime.now()
                timestamp = datetime.timestamp(now)
                timestamp2 = datetime.timestamp(datetime_str)

                if (timestamp2 > timestamp):
                    diff = int(timestamp2 - timestamp)
                    hour = diff / 3600
                    hour2 = int(hour)
                    h1 = hour - round(hour)
                    if (h1 < 0):
                        h1 = h1 * (-1)
                        minutes = int(h1 * 60)
                    else:
                        minutes = int(h1 * 60)
                    z = r'//*[@id="col1"]/div/div/form/div/table/tbody/tr[' + str(i) + r']/td[2]/strong/a'
                    assignment_title = driver.find_element_by_xpath(z).text
                    printable[count] = 'You have ' + assignment_title + ' due at ' + t + ' which is in ' +str(
                        hour2) + ' hours ' + ' and ' + str(minutes) + ' minutes.'
                    count = count + 1
            elif (len(t) == 20):
                r = t[:6] + t[7:]
                c = r[:16] + r[17:]
                format = '%b %d %Y %I:%M%p'
                datetime_str = datetime.strptime(c, format)
                now = datetime.now()
                timestamp = datetime.timestamp(now)
                timestamp2 = datetime.timestamp(datetime_str)
                # print('now :'+str(timestamp))
                # print('expiry :'+str(timestamp2))

                if (timestamp2 > timestamp):
                    diff = int(timestamp2 - timestamp)
                    hour = diff / 3600
                    hour2 = int(hour)
                    h1 = hour - round(hour)
                    if (h1 < 0):
                        h1 = h1 * (-1)
                        minutes = int(h1 * 60)
                    else:
                        minutes = int(h1 * 60)
                    z = r'//*[@id="col1"]/div/div/form/div/table/tbody/tr[' + str(i) + r']/td[2]/strong/a'
                    assignment_title = driver.find_element_by_xpath(z).text
                    printable[count] = 'You have ' + assignment_title + ' due at ' + t + ' which is in ' + str(
                        hour2) + ' hours ' + ' and ' + str(minutes) + ' minutes.'
                    count = count + 1

    for i in range (count):
        label1 = tk.Label(root, text=printable[i],font=('helvetica', 10))
        canvas1.create_window(400, (250+(i*20)), window=label1)


button1 = tk.Button(text='login', command=getSquareRoot)
canvas1.create_window(400, 180, window=button1)

root.mainloop()


