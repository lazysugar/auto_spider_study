import requests
from lxml import etree
import time
import sys
import base64


search_data='search_data'#输入搜索的数据
headers={
    'Cookie':'your_cookie', #你的cookie
    'Upgrade-Insecure-Requests': '1',
    'Referer':'https://fofa.so/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

}
for yeshu in range(1,355):
    print('正在提取第'+str(yeshu)+'页\n')
    url='https://fofa.so/result?'+'page='+str(yeshu)+'&page_size=10'+'&qbase64='
    search_data_bs=str(base64.b64encode(search_data.encode("utf-8")), "utf-8")
    urls=url+search_data_bs
    print(urls)
    try:
        result=requests.get(urls,headers=headers).content
        #print(result.decode('utf-8'))
        soup =etree.HTML(result)
        ip_data = soup.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')
        ip_data='\n'.join(ip_data)
        print(ip_data)
        with open(r'ip.txt','a+') as f:
            f.write(ip_data+'\n')
            f.close()
    except Exception as f:
        print(f)
        time.sleep(0.5)
