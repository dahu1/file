#!/usr/bin/python
#coding=utf-8
#__author__='dahu'
#给定一个pat需求,据此生成句子,方括号包含空,括号之间不能包含
import re
import itertools
ss='[现在|今天|明天|后天][北京]有[霾|雾霾|空气污染]吗'
# ss1='[现在|今天|明天|后天](会不会)(下雨|降温)'
fanglist=['\[.*?\]','\]',1] #非贪心匹配
yuanlist=['\(.*?\)','\)',0]
dd={
    r'[':fanglist,
    r'(':yuanlist,
}
cho=ss
with open('pat_in','r') as f:
    cho=f.read()
product=[]
en=[]   #记录尾部
sort_d={}   #排序转接作用

'''匹配到所有括号'''
for i in dd:
    # print i,i in cho
    if i in cho:
        # print cho.index(i)
        for k in re.compile(dd[i][0]).finditer(cho):
            # print k.group()
            # sta=k.start()
            # print cho[k.start():k.end()]
            fenci_list=k.group()[1:-1].split('|')
            en.append((k.start(),k.end()))
            # sta.append(k.start())
            if dd[i][-1]:
                fenci_list.append('')   #方括号考虑没有的情况
            sort_d[k.start()]=fenci_list    #每个位置装入字典,最后排序,就跟原来句子顺序一致.
            # product.append(fenci_list)
            # for fenci in fenci_list:
            #     print fenci,
            # print

'''括号内和括号外的都需要'''
f=open('pat_out','w')
product=[sort_d[i] for i in sorted(sort_d.keys())]
#头部尾部添加
en.insert(0,(0,0))          #en是用来存放每个括号的序号
en.append((len(cho),len(cho)))
en.sort()
print en,len(cho)
# print en.
print sort_d.keys()
qiyui=0
for i in range(len(en)-1):
    if en[i+1][0]-en[i][1] !=0:
        qiyu= cho[en[i][1]:en[i+1][0]]
        product.insert(i+qiyui,[qiyu])  #很丑的方法,都看不下去了
        qiyui += 1
        # print i,
cunt=0
for m in itertools.product(*product):  # 未知个数封装,叼叼叼
    a=''.join(m).strip()
    if a.startswith('的'):
        continue
    print a
    cunt+=1
    f.write(a + '\n')
f.close()
print cunt
# print dd.items()
# for i in dd:
#     ss[i ]