import subprocess

print('$ nslookup')
ppp = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = ppp.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', ppp.returncode)