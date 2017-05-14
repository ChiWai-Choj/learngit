# -*- coding: utf-8 -*-

#导入所需要包
import time
from selenium import webdriver

#定义创建模拟浏览器函数
def driver():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    #隐式等待5秒，可以自己调节
    driver.implicitly_wait(5)
    #设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
    #以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
    driver.set_page_load_timeout(10)
    #设置10秒脚本超时时间
    driver.set_script_timeout(10)
    return driver

#定义登录校园网函数
def page_source(driver):
    driver.get('http://192.168.2.185/pyxx/login.aspx')
    xuehao=raw_input('XueHao:')
    mima=raw_input('MiMa:')
    securityCode=raw_input('YanZhengMa:')
    driver.find_element_by_id('ctl00_txtusername').clear()
    driver.find_element_by_id('ctl00_txtusername').send_keys(xuehao)
    driver.find_element_by_id('ctl00_txtpassword').clear()
    driver.find_element_by_id('ctl00_txtpassword').send_keys(mima)  
    driver.find_element_by_id('ctl00_txtyzm').clear()
    driver.find_element_by_id('ctl00_txtyzm').send_keys(securityCode)
    driver.find_element_by_id('ctl00_ImageButton1').click()
    return driver

#定义刷新、判断是否有学术活动、抢票函数      
def xuanpiao():
    o=0         
    while True:
        start = time.time() 
        driver.switch_to_default_content()
        driver.switch_to_frame('MenuFrame')
        link.click()
        driver.switch_to_default_content()
        driver.switch_to_frame('PageFrame')
        b=driver.find_elements_by_xpath("//table[@id='dgData00']/tbody/tr/td[14]")
        print u'现在有%i个活动'%(len(b)-1)
        #判断是否有学术活动
        if len(b)>1:
            a=driver.find_elements_by_xpath("//table[@id='dgData00']/tbody/tr/td[14]/a")
            aa=len(a)
            for i in list(reversed(range(0,aa))):
                a[i].click()
                driver.switch_to_alert().accept() 
                message=driver.switch_to_alert().text
                print u"第%i个活动：%s"%(i+1,message)
                driver.switch_to_alert().accept()
                if i!=0:
                    a=driver.find_elements_by_xpath("//table[@id='dgData00']/tbody/tr/td[14]/a")                      
            break
	o+=1
        end = time.time()
        print u'您已经刷新%i次,用时%f秒'%(o,end-start)
def xuanpiao0():
    o=0         
    while True:
        start = time.time() 
        driver.switch_to_default_content()
        driver.switch_to_frame('MenuFrame')
        link.click()
        driver.switch_to_default_content()
        driver.switch_to_frame('PageFrame')
        b=driver.find_elements_by_xpath("//table[@id='dgData00']/tbody/tr/td[14]")
        print u'现在有%i个活动'%(len(b)-1)
        #判断是否有学术活动
        if len(b)>1:
            a=driver.find_elements_by_xpath("//table[@id='dgData00']/tbody/tr/td[14]/a")
            aa=len(a)
            for i in list(reversed(range(0,aa))):
                a[i].click()
                driver.switch_to_alert().accept() 
                message=driver.switch_to_alert().text
                print u"第%i个活动：%s"%(i+1,message)
                driver.switch_to_alert().accept()
                if i!=0:
                    a=driver.find_elements_by_xpath("//table[@id='dgData00']/tbody/tr/td[14]/a")                      
	o+=1
        end = time.time()
        print u'您已经刷新%i次,用时%f秒'%(o,end-start)


       
if __name__ == "__main__":
    driver=driver()
    page_source(driver)   
    driver.switch_to_default_content()
    driver.switch_to_frame('MenuFrame')
    link=driver.find_element_by_xpath("//dl[@id='tree']/dd[7]/ul/li/a")
    if driver.find_element_by_xpath("//dl[@id='tree']/dt[7]").get_attribute('class').encode('utf-8')=='close':
        link0=driver.find_element_by_xpath("//dl[@id='tree']/dt[7]")
        link0.click()
    start=raw_input('S(Satrt)/E(Exit):')
    model=raw_input('J(jiankong)/Q(qiangpiao):')
    if start=='S':
        if model=='J':
            xuanpiao0()
        elif model=='Q':
            xuanpiao()
    elif start=='E':
        driver.close()
    

