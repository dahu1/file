#!/usr/bin/python
#coding=utf-8
#version_1 
#made by dahu
"""1.考虑两组数据事件不一样的情况
   2.按照要求格式输出"""
import re,sys,string
import collections #扩展功能，记住字典的顺序
if len(sys.argv)<=3:
	print ( ("使用方法：python + %s + input_file1 + input_file2 + output_file")%sys.argv[0])
	exit()
"""数据读取"""
f1=open(sys.argv[1],'r')
data1=f1.read()
#print len(data1)
f1.close()
#print data1
p=re.compile(r'(\n{2})')
s=p.finditer(data1)
k=0

f2=open(sys.argv[2],'r')
data2=f2.read()
f2.close()
p=re.compile(r'(\n{2})')
s2=p.finditer(data2)

"""
数据大切分，
匹配双换行，上一个匹配点的行末到下一个匹配点的行首
"""
k=0
group_data1=[]
for i in s:
	t=0 if k==0 else en
	group_data1.append(data1[t:i.start()].decode('utf-8'))
	#print '>>>>>>'
	en=i.end() 	
	k+=1
#print group_data1[0],len(group_data1)  #列表数据存入到group_data1中

group_data2=[]
k=0
for i in s2:
	t=0 if k==0 else en
	group_data2.append(data2[t:i.start()].decode('utf-8'))
	en=i.end() 	
	k+=1
#print group_data2[0],len(group_data2)
n1=len(group_data1)
n2=len(group_data2)
n=n1

#考虑两边数据会不一样，把每组事件存入字典
a1=[group_data1[i].split('\n')[0].strip() for i in range(n1)]
dict_data1=collections.OrderedDict(zip(a1,group_data1))
a2=[group_data2[i].split('\n')[0].strip() for i in range(n2)]
dict_data2=collections.OrderedDict(zip(a2,group_data2))
"""
#验证生成的字典
k=0
for i in dict_data2:
	if k<=5:
		print i,'>>>>>>>>',dict_data2[i]
		k+=1
"""
#两组数据进行循环对比，找相同项进行处理

if len(group_data1) != len(group_data2):	#防止两组数据个数不一样，防错
	raise  Exception ( "Error! Two file has different counts!")

#print string.split(group_data1[0],'\n')[0]
p1=re.compile(r'logprob=.-?(\d+).(\d*)')
res=[]
k=0
dif_list=[]
for i in dict_data1:
	try:
		match2=p1.search(dict_data2[i])
		r2=float(match2.group(0).split('=')[1])
		match1=p1.search(dict_data1[i])
		r1=float(match1.group(0).split('=')[1])
		res.extend([[i,r1,r2,r1-r2]])
	except:
		print i,' --> 两边数据不一样'
		dif_list.append(i)
#输出结果
f=open(sys.argv[3],'w')
ss='%s有%s组数据\n'

f.write((ss+ss)%(sys.argv[1],n1,sys.argv[2],n2))
if len(dif_list)>0:
	f.write('两边不一样的数据有%s组 如下:\n'%len(dif_list))
	for i in range(len(dif_list)):
		f.write('--> %s\n'%(dif_list[i].encode('utf-8')))
f.write('\n详细情况:\n')
for i in range(len(res)):
	if res[i][3]>=-1111111110.3:
		f.write("%s\nv1:%s  v2:%s delta:%s\n"%(res[i][0].encode('utf-8'),res[i][1],res[i][2],res[i][3]))
f.close()
