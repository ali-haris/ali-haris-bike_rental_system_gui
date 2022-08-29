from datetime import datetime as dt
from conn_db import *


calcu = dt.strptime(to_search('haris',1)[0][3],'%Y-%m-%d %H:%M:%S.%f')-dt.strptime(to_search('haris',2)[0][3],'%Y-%m-%d %H:%M:%S.%f')
print(dt.now().hour)
print(calcu.seconds/60/60)
# print()
