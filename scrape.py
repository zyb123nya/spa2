#!/usr/bin/env python
# coding: utf-8

# In[42]:


import requests
import time
t1=time.time()
import hashlib
import base64
a="ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb"
for b in range(1,101):
    c=f"{a}{b}" #解码后的base64编码和后者1-100的拼接
    url_id=base64.b64encode(c.encode('utf-8'))#base64转utf-8
    url_id=url_id.decode()
    #1：时间戳取整    
    t=int(time.time())#获取时间戳数据
    #2：SHA1加密 
    s1 = f"/api/movie/{url_id},0,{t}"
    o = hashlib.sha1(s1.encode("utf-8")).hexdigest()    
    s2=f'{o},{t}'
    s3=s2.encode('utf-8')
    #3：Base64加密
    token=base64.b64encode(s3)
    #4:bytes转str
    token=token.decode()
    url=f"https://spa2.scrape.center/api/movie/{url_id}/?token={token}"
    html=getHTMLText(url)
    print(html['id'],html['drama'])
print(time.time()-t1)#约一分钟


# In[ ]:





# In[ ]:





# In[ ]:




