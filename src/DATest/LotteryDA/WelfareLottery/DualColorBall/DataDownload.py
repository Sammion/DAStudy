# -*- coding: utf-8 -*-
"""
Created on 8/11/2018

@author: Samuel
@Desc: 
@dependence:
pip install selenium
pip install phantomjs
"""
import requests
from bs4 import BeautifulSoup as bs
import re
from selenium import webdriver
import os
import urllib3
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import time, datetime


def get_days(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def get_wk_dt(date_list):
    with open("date_list.txt", mode="a", encoding="utf-8") as fw:
        for dt in date_list:
            print(dt)
            wk_num = datetime.datetime.strptime(dt, "%Y-%m-%d").weekday()
            if wk_num in [1, 3, 6]:
                fw.write(dt)
                fw.write('\n')
            else:
                continue


def gen_url():
    dt = datetime.datetime.now()
    dt_list = get_days('2018-08-01', '2018-08-10')
    get_wk_dt(dt_list)

    dt.weekday()

    open_date = ''
    id = ''
    src_url = "http://www.cwl.gov.cn//c/%{od}/%{id}.shtml".format(od=open_date, id=id)
    return src_url


def get_data(dt_id={428324: "2017-12-21"}):
    """

    :param dt_id:
    :return:
    """
    url_format = "http://www.cwl.gov.cn//c/{dt}/{id}.shtml"
    driver_path = "..\driver\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver_path)
    df = pd.DataFrame()
    for i in dt_id.keys():
        url = url_format.format(dt=dt_id[i], id=i)
        try:
            browser.get(url=url)
            qiuH1 = browser.find_element_by_class_name("qiuH1").text
            qiuH2 = browser.find_element_by_class_name("qiuH2").text
            qiuH3 = browser.find_element_by_class_name("qiuH3").text
            qiuH4 = browser.find_element_by_class_name("qiuH4").text
            qiuH5 = browser.find_element_by_class_name("qiuH5").text
            qiuH6 = browser.find_element_by_class_name("qiuH6").text
            qiuL = browser.find_element_by_class_name("qiuL").text
            luck_nums = [qiuH1, qiuH1, qiuH2, qiuH3, qiuH4, qiuH5, qiuH6, qiuL]
            print("{dt} 开奖号码为： {num}".format(dt=dt_id[i], num=luck_nums))

            print(df)
            # ps = browser.page_source
            # soup=bs(ps,'lxml')
        except:
            print("Sth wrong happend!")
    df.to_csv("ALL_DATA.csv", mode='w', encoding="utf-8")
    browser.close()
    return df


def down_load_data():
    driver_path = "..\driver\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver_path)
    url = "http://www.cwl.gov.cn/kjxx/ssq/kjgg/"
    browser.get(url)
    ps = browser.page_source
    with open("all_list1.html", mode="w", encoding="utf-8") as fw:
        fw.write(ps)
    browser.find_element_by_class_name("dqzt").click()
    browser.find_element_by_xpath('//strong[3]').click()
    # begin_date=browser.find_element_by_xpath("//input[@class=='inpQa']")
    browser.find_element_by_class_name("inpRa").clear()
    browser.find_element_by_class_name("inpRa").send_keys("2013-01-01")
    browser.find_element_by_class_name("inpRz").clear()
    browser.find_element_by_class_name("inpRz").send_keys("2018-08-30")
    browser.find_element_by_class_name("aRzR").click()
    ps = browser.page_source
    data_parse(ps)
    for i in range(15):
        try:
            browser.find_element_by_class_name("xye").click()
            ps = browser.page_source
            # print("Begin to data parse: " + i)
            data_parse(ps)
        except:
            print("=" * 50 + '\n' + " Maybe all data have been parsed! \n" + "=" * 50)
            break
        finally:
            print("=" * 50 + '\n' + " All data have been parsed! \n" + "=" * 50)
    # data_parse(ps)
    browser.close()


def data_parse(ps):
    soup = bs(ps, 'lxml')
    tbody = soup.find("tbody")
    all_info = list()
    for tr in tbody.find_all("tr"):
        td = tr.find_all("td")
        id = td[0].text
        dt = td[1].text
        nums = list()
        for i in td[2].find_all("span"):
            nums.append(i.text)
        nums.append(td[3].text)
        all_sales = td[4].text
        first_prize_sales = td[5].text
        first_prize = td[6].text
        second_prize_sales = td[7].text
        second_prize = td[8].text
        third_prize_sales = td[9].text
        third_prize = td[10].text
        bonus_remain = td[11].text
        detail_link = td[12].find("a")
        per_info = [id, dt, nums, all_sales, first_prize_sales, first_prize, second_prize_sales, second_prize,
                    third_prize_sales, third_prize, bonus_remain, detail_link]
        all_info.append(per_info)
    head = ['id', 'dt', 'nums', 'all_sales', 'first_prize_sales', 'first_prize', 'second_prize_sales', 'second_prize',
            'third_prize_sales', 'third_prize', 'bonus_remain', 'detail_link']
    df = pd.DataFrame(all_info, columns=head)
    df.to_csv("AllData.csv", mode="a", header=False)


if __name__ == '__main__':
    # get_data()
    # gen_url()
    down_load_data()
