'''
import re 
pattern = [\s]*href=\"[\w]+\.html\"
x = open("test.txt",'r')
for line in x:
    line = list(line.split())
    for obj in line:
        if 'href' in obj and "/" not in obj:  
            
                href="modelNissanArmada.html"
                href={{ url_for('modelNissanArmada') }}
'''
import os
import re
#print (os.listdir(os.getcwd()))

for f in os.listdir(os.getcwd()):
    if f.endswith(".html"):
        
        input = open(f,'r')        
        output = open("output3.txt","w")

        for line in input:
            output.write(re.sub(r"[\.]*href=\"{0,1}([\w]+)\.html\"{0,1}[\.]*", r"href={{url_for('\1')}}", line))
        
        input.close()
        output.close()
        
        output = open("output2.txt","w")
        input = open("output3.txt","r")

        for line in input:
            output.write(re.sub(r"dist/(\w+)", r"../static/\1", line))

        input.close()
        output.close()
        
        output = open(f,"w")
        input = open("output2.txt","r")

        for line in input:
            output.write(re.sub(r"dist/(\w+)", r"../static/\1", line)) 

        input.close()
        output.close()

input.close()
output.close()
#line = re.sub(r"[\s]*href=\"[\w]+\.html\"", "[\s]*href=\{\{url_for\(\'[\w]+\'\)\}\}")     
