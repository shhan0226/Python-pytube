#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

### 1. system()
#os.system('ls -l')

### 2. popen()
#stream = os.popen('ls -l')
#output = stream.read()
#print(output)



import subprocess
### 3. subprocess()
#subprocess.run(["ls", "-l"])

### 4.
#result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
#print(result.stdout)

### 5. 
#command = "ls -l"
#result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True)
#print(result.stdout)

### 6.
#subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL)

### 7.
#subprocess.run(["/data/github/py3-tool/pyserial/test.sh", "arguments"], shell=True)



temp = 0
print(temp)

#result = subprocess.run(["/data/github/py3-tool/pyserial/test.sh", "arguments"], stdout=subprocess.PIPE, text=True)
#print(result.stdout)
stream = os.popen('/data/github/py3-tool/pyserial/test.sh')

temp = stream.read()
print(temp.strip())
