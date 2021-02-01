


def FIND(string):
    #定义两个变量：分别表示开始的字符串，结束的字符串
    start1 = '<a href="'
    end1 = '/" class'
    #使用find找到开始和结束截取的位置
    s3=string
    s = string.find(start1)
    e = string.find(end1)
    #找到第一个
    sub_str = string[s:e + len(end1)]
    s1=sub_str.replace(start1,'')
    s1=s1.replace(end1,'')
    s1=s1.replace('</p>','')
    print(s1)
    if s1 !=None:
        f=open('vul.txt','a')
        f.write(s1)
        f.write('\n')
    count = string.count(start1)
    for x in range(0,count):
        s = string.find(start1,e)
        e = string.find(end1,s)
        sub_str = string[s:e + len(end1)]
        s2=sub_str.replace(start1,'')
        s2=s2.replace(end1,'')
        s2=s2.replace('</p>','')
        return s2

file = open("123.txt",'rb')
for url in file.readlines():
    print(FIND(str(url, encoding = "utf-8")))
