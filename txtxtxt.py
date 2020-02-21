fp = open("myfile.txt","r")
line = fp.read()

while line:
    print(line)
    line=fp.read()
    
fp.close()

fp = open("myfile.txt","w")
fp.write("哈哈哈哈哈哈哈哈哈哈哈啊哈哈\a")
fp.close()