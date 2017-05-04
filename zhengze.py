# -*- coding:utf8 -*-
import sys

def produce_zhengze(argv):
    if len(argv)==1:
        print "用法：文件个数等于2时（示正则表达式文件、输出文件），执行：将正则表达式转换成句子，且屏幕输出每类句子的一个值"+'\n'+"文件个数等于3时（正则表达式文件、标注文件、输出文件），执行：将正则表达式转换成句子+标注"
        return
    elif len(argv)==3:
        ipath=argv[1]
        opath=argv[2]
        mappath=""
    elif len(argv)==4:
        ipath=argv[1]
        opath=argv[3]
        mappath=argv[2] 
    else:
        print "参数个数错误"      
        return
     
    outputs=zhengze(ipath)        
    file1=open(opath,'w')
    maps=[]
    if mappath=="":
        for output in outputs:
            for out in output:
                file1.write((out).encode('utf8')+'\n')
    else:
        for line in open(mappath):
            line=line.decode('utf8').strip()
            maps.append(line.split('=>')[1])
        i=0
        if len(outputs)<>len(maps):
            print "map length <> ipath length"
            return
        for output in outputs:
            for out in output:
                file1.write((out+' =>'+maps[i]).encode('utf8')+'\n')
            i+=1
    file1.close()
        


def zhengze(ipath):
    fuhao=['(',')','[',']']
    #file1=open(opath,'w')
    outputs=[]
    for line in open(ipath):
        line=line.decode('utf8').strip()
        sentence=[]
        sen=""
       # print line.encode('utf8')
        for c in line:
           # print c
            if c in fuhao:
                if sen<>"":
                    sentence.append(sen)
                    sen=""
                sentence.append(c)
            else:
                sen+=c  
        if sen<>"":
            sentence.append(sen)
       # for c in sentence:
      #      print c,
      #  print ""
        i=0
        output=[]
        while i<len(sentence):
            #print sentence[i]
            if sentence[i]=='(' and i+2<len(sentence) and sentence[i+2]==')':
                #pos=sentence[i+1:].index(')')+i+1
                sen=sentence[i+1].split('|')
                newoutput=[]
                if len(output)==0:
                    for s in sen:
                        output.append(s)
                else:
                    for out in output:
                        for s in sen:
                            #print out,s,'======'
                            newoutput.append(out+s)
                    output=newoutput
                i+=3
                #print '===============1'
            elif sentence[i]=='[' and i+2<len(sentence) and sentence[i+2]==']':
                sen=sentence[i+1].split('|')
                newoutput=output[:]
                if len(output)==0:
                    for s in sen:
                        output.append(s)
                    output.append("")
                else:
                    for out in output:
                        for s in sen:
                            newoutput.append(out+s)
                    output=newoutput
                i+=3
                #print '===============2'
            elif sentence[i] not in fuhao:
                sen=sentence[i].split('|')
                newoutput=[]
                if len(output)==0:
                    for s in sen:
                        output.append(s)
                else:
                    for out in output:
                        for s in sen:
                            newoutput.append(out+s)
                    output=newoutput
                i+=1
                #print '===============3'
            else:
                print 'error'
                #print '===============4'
                break
        print output[0].encode('utf8')
        outputs.append(output)
 #       for out in output:
           # print out
  #          file1.write(out.encode('utf8')+'\n')
 #   file1.close()
    return outputs

    




if __name__=='__main__':
    #produce_zhengze(sys.argv[1],sys.argv[2],sys.argv[3])
    produce_zhengze(sys.argv)
