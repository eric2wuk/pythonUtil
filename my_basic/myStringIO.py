from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!!!')
print(f.getvalue())