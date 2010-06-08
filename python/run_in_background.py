# -*- encoding: utf-8 -*-
import subprocess

command = ['./wait_and_hello.sh']

sp = subprocess.Popen(command, 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)

while sp.poll() is None:
    print sp.stdout.readline()

status = sp.wait()

print "Terminan los dos procesos"
print "El proceso hijo termina con estatus=%d" %(status)
