f1=open("abc.txt","w")
f1.write("wawawawaaaaaaaaaawwwwwwwwwww\n\n")
f1.write("hahahahahahaha\n\n")
f1.write("all are welcome\n")
f1=open("abc.txt",'r')
str=f1.read()
print("read strings:",str)
f1.close()
print(f1.name,"is closed")
