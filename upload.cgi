#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

# shamelessly copied from https://gist.github.com/ohtomi/74c49a4f6b460d9097f7
# ported to python 3 and added length check
    
import cgi, cgitb, os, sys


UPLOAD_DIR = './upload'


def save_uploaded_file():
    print ('Content-Type: text/html; charset=UTF-8')
    print ('')
    print ('''
<html>
<head>
  <title>Upload File</title>
</head>
<body>
''')

    form = cgi.FieldStorage()
    if 'file' not in form:
        print ('<h1>Not found parameter: file</h1>')
        return

    form_file = form['file']
    if not form_file.file:
        print ('<h1>Not found parameter: file</h1>')
        return

    if not form_file.filename:
        print ('<h1>Not found parameter: file</h1>')
        return

    
    uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(form_file.filename))

    #doublecheck to be really in the right path
    if os.path.dirname(uploaded_file_path) != UPLOAD_DIR or len(form_file.filename) > 300:
        print('<h1>Invalid filename</h1>')
        return
        
    with open(uploaded_file_path, 'wb') as fout:
        while True:
            chunk = form_file.file.read(100000)
            if not chunk:
                break
            fout.write (chunk)
    print ('<h1>Completed file upload</h1>')

    print ('''
<hr>
<a href="../upload.html">Back to upload page</a>
</body>
</html>
''')


cgitb.enable()
save_uploaded_file()
