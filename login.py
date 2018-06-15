#__author: Joey
#date:    2018/6/15

from selenium import webdriver
import requests

class ZhiHu_login(object):
    #模拟登陆知乎获取cookie
    def __init__(self,user,pwd):
        self.cookie = {}
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.zhihu.com')
            driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/div/div[2]/button[3]').click()
            driver.find_element_by_xpath('/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[2]/span').click()
            username = driver.find_element_by_xpath('/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
            password = driver.find_element_by_xpath('/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')
            username.send_keys(user)
            password.send_keys(pwd)
            driver.find_element_by_xpath('/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button').click()
            if driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div[1]/div/div/span'):
                print('login succeed')
                cookies = driver.get_cookies()
                for i in cookies:
                    self.cookie[i['name']] = i['value']
                print(self.cookie)
            else:raise Exception
        except Exception as e:
            print('login failed:',e)

    def get_page(self,url):
        page = requests.get(url,cookies=self.cookie,headers=self.headers)
        print(page.text)

if __name__ == '__main__':
    #输入手机/邮箱，密码登陆
    zhihu = ZhiHu_login('*****','*****')
    #返回登陆后的界面
    zhihu.get_page('https://www.zhihu.com')


