#!python
print("Content-Type: text/html\n")
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello Web'

print('''<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset=utf-8>
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(title=pageId,
    desc=description,
    listStr=view.getList(),
    update_link=view.updateLink(pageId),
    delete_action=view.deleteAction(pageId)))
