#! /usr/bin/env python3

import cgi

f=cgi.FieldStorage()
name=f.getvalue('name')

print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<body>')
if name is None:
    print('<form method="post">')
    print('Your name: ')
    print('<input type="text" name="name">')
    print('<input type="submit" value="OK">')
    print('</form>')
else:
    print('<p>')
    print('Hello,',name)
    print('</p>')
print('</body>')
print('</html>')