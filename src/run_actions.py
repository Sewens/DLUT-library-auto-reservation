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
import os
from selenium import webdriver

# 通过github secret 获取学号密码以及其他敏感信息
StuID = os.environ['STUID']    # 学号
PW = os.environ['PW']    # 密码

# github actions chromedriver运行路径
# 在.github/workflow中指定了相关文件的copy
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
# 此处为chromedriver文件地址
chrome_options.binary_location = CHROMEDRIVER_PATH

# 运行在非沙盒模式下 需要最先进行这个配置
chrome_options.add_argument('--no-sandbox')
# 设置窗体大小
chrome_options.add_argument('--window-size=1420,1080')
# 运行在headless模式
chrome_options.add_argument('--headless')
# 不使用gpu渲染
chrome_options.add_argument('--disable-gpu')
# 将驱动和options关联
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
browser.maximize_window()

# 用户名密码配置信息, 可选多人
user_id = StuID
password = PW
email = 'xxxx@163.com'
user_id_n = 'xxxx'
password_n = '****'
email_n = 'xxxx@163.com'

# 输入需要的图书馆和座位候选座位
wanted_seats = [233, 239, 235] # 请输入完整的3位座位号（如不足请用0补足）
library_name = '令希' # 请输入伯川或令希
reading_room = 401 # 请预先在系统上确定要指定的阅览室

user1 = Reserve(user_id_n, password_n, wanted_seats, email_n, library_name, reading_room)
# user2 = Reserve(user_id, password, wanted_seats, email, library_name, reading_room)

user1.reserve(browser)
# user2.reserve(browser)

browser.close()
