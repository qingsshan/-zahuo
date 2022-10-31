# coding=utf-8
import requests
from lxml import html
from fake_useragent import UserAgent


class Ten_phone(object):
    def __init__(self, url):
        self._url = url
        self._ua = UserAgent()
        self._etree = html.etree

    def init(self):
        hearder = {
            "User_Agent": self._ua.random,
            "Referer": url
        }
        res = requests.get(self._url, headers=hearder)
        res.encoding = res.apparent_encoding
        if res.status_code != 200:
            print("网页目前不可用")
        html = self._etree.HTML(res.text)
        res_url = html.xpath("/html/body/div[1]/div[1]/div[1]/div/h1/div[1]/div/h2")
        for i in res_url:
            print("电话：" + i.text)
        code = int(input("输入1刷新页面获取验证码："))
        if code == 1:
            while True:
                self._new_url()
                ret = int(input("是否输入1再次刷新？若否则随便输入："))
                if ret == 1:
                    self._new_url()
                if ret != 1:
                    break

    def _new_url(self):
        hearders = {
            "User_Agent": self._ua.random,
            "Referer": url
        }
        res2 = requests.get(self._url, headers=hearders)
        res2.encoding = res2.apparent_encoding
        if res2.status_code != 200:
            print("网页目前不可用")
        html = self._etree.HTML(res2.text)
        res_txt = html.xpath("/html/body/div[1]/div[1]/div[3]/div[1]/div//div/p/text()")
        for b in res_txt:
            print(b)


# 爬取中国地区电话网址
url = "https://www.zusms.com/messages/600fb6ccd5f46474bb8b4d14"
Ten_phone(url).init()
