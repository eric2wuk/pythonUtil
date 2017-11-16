from io import BytesIO
fff = BytesIO()
fff.write('中文ss'.encode('utf-8'))
print(fff.getvalue())