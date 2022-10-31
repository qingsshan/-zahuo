# coding=utf-8
import exrex
from config import *



def url_passworad(url):
    # 过滤域名
    if "://" in url:
        url = url.split("://")
    url_yu = url[1].replace("/", "")
    # 截取域名
    url_jie = url_yu.split(".")
    print(url_jie)
    # 准备空列表接受过滤后域名
    url_res = []
    # 过滤黑名单
    for key in url_jie:
        if key not in black_name_list:
            url_res.append(key)
    return url_res


url = "https://ssoin.fsyuncai.com/"
url_res = url_passworad(url)
for i in url_res:
    for p in pwd_m_list:
        pattern = i+r"[@#!]{1,2}"+p
        # 生成字典
        temp_pwd_list = list(exrex.generate(pattern))
        with open("./pwdtxt/pwd.txt", "a+") as w:
            for password in temp_pwd_list:
                w.write(password+"\n")

