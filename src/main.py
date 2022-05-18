#  coding=utf-8
'''
main
@author: Shuaichi Li
@email: shuaichi@mail.dlut.edu.cn
@date: 2020/12/01 15:46
'''

#  import
import time
import datetime
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
import traceback
from utils.reserve import Reserve


if __name__ == '__main__':

    browser = webdriver.Chrome(executable_path='./driver/win/chromedriver.exe')
    browser.maximize_window()

    # 用户名密码配置信息, 可选多人
    user_id = '11809048'
    password = 'dutir412341435'
    email = 'xxxx@163.com'
    user_id_n = 'xxxx'
    password_n = '****'
    email_n = 'xxxx@163.com'

    # 输入需要的图书馆和座位候选座位
    wanted_seats = [63] # 请输入完整的3位座位号（如不足请用0补足）
    library_name = '令希' # 请输入伯川或令希
    reading_room = 302 # 请预先在系统上确定要指定的阅览室

    user1 = Reserve(user_id, password, wanted_seats, email_n, library_name, reading_room)
    # user2 = Reserve(user_id, password, wanted_seats, email, library_name, reading_room)

    user1.reserve(browser)
    # user2.reserve(browser)

    browser.close()
