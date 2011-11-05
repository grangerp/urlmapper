'''
Created on 2011-11-05

@author: pgranger
'''
import re

class UrlMap(object):
    
    def __init__(self):
        self.urlmap=[]
    
    def add(self,regexp,funct):
        self.urlmap.append((re.compile(regexp),funct))
            
    def map_path(self,path):
        for regexp,func in self.urlmap:
            match=regexp.search(path)
            if match:
                kwargs = match.groupdict()
                if kwargs:
                    args = ()
                else:
                    args = match.groups()
                return func(*args,**kwargs)
        return None    

def a():
    return 'a'
def b():
    return 'b'
def c(year,month,day):
    return year,month,day
def d(year=None,month=None,day=None):
    
    return year,month,day

if __name__ == '__main__':
    urlmap=UrlMap()
    urlmap.add(r'^articles/2003/$', a)
    urlmap.add(r'^articles/(\d{4})/$', b)
    urlmap.add(r'^articles/(\d{4})/(\d{2})/$', c)
    urlmap.add(r'^articles/(\d{4})/(\d{2})/(\d+)/$', c)
    urlmap.add(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', d)
    
    path='articles/2004/12/21/'
    print urlmap.map_path(path)
    