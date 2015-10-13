import os
import datetime as dt
import shutil

for root,dirs,files in os.walk('/Users/Sylvia/Desktop/EdittedFolder'):

    for item in files:
        now = dt.datetime.now()
        yesterday = now - dt.timedelta(days=1)
        path = os.path.join(root,item)
        st = os.stat(path)

    mod_time = dt.datetime.fromtimestamp(st.st_ctime)
    if mod_time < yesterday:
        shutil.move(os.path.join(root,item), '/Users/Sylvia/Desktop/HomeOffice')
        print('File created or modified yesterday has been transferred')
    else:
        print('%s last modified %s'%(path,mod_time))
