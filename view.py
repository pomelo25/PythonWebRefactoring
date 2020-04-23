import os

def getList();
  files = os.listdir('data')
  listStr = ''
  
  for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}>{name}</a></li>'.format(name=item)
  
  return listStr
  
  
def updateLink(pageId):
  if pageId != 'Welcome':
    updateLink = '<a href="update.py?id={}">update</a>'.format(pageId)
  else:
    updateLink = ''
  
  return updateLink
  
  
def deleteAction(pageId):
  if pageId != 'Welcome':
    deleteAction = '''
      <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
      </form>
    '''.format(pageId)
  else:
    deleteAction = ''
    
  return deleteAction
