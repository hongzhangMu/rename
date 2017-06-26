# encoding: utf-8  
import os  
import os.path  
rootdir = r'/media/tx-eva-08/data/workspace/dataset/'    # 指明被遍历的文件夹  
  
#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字  
for parent, dirnames, filenames in os.walk(rootdir):      
    for filename in filenames:  #输出文件信息  
        print "parent is: " + parent
        newfile=parent[40:]
        print newfile  
        print "filename is: " + filename
        filename1=filename[4:]
        print filename1
        newfilename='_'+newfile+'_'+filename1
        print newfilename  
        os.rename(os.path.join(parent, filename), os.path.join(parent, newfilename))  
 