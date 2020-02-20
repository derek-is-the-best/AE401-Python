import os
print(os.getcwd())
fo = open('myfile.txt','w')
fo.write('hahaha')
fo = open('myfile.txt','r')
print(fo.read())
fo = open('myfile.txt','a')
fo.write('and hohoho')
fo.close

