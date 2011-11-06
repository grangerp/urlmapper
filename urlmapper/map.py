'''
Created on 2011-11-05

@author: pgranger
'''
import re

class UrlNotFound(Exception):
    pass

class UrlNotMatch(Exception):
    pass

class RegexUrlMatch(object):
    """ class containing a match and all necessary info to call the function """
    def __init__(self, func, args, kwargs, name=None):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.name = name

    def call(self):
        """ call function and return result """
        return self.func(*self.args, **self.kwargs)


class RegexUrlPattern(object):

    def __init__(self, regexp, func, kwargs=None, name=None):
        self.regexp = regexp
        self.func = func
        if kwargs is None:
            kwargs = {}
        self.kwargs = kwargs
        self.name = name

    def resolve(self, path):
        match = self.regexp.search(path)
        if match:
            kw = match.groupdict()
            if kw:
                args = ()
            else:
                args = match.groups()
            kw.update(self.kwargs)
            return RegexUrlMatch(self.func, args, kw, self.name)
        raise UrlNotMatch(path)

class UrlMap(object):

    def __init__(self):
        self.urlmap = []

    def add(self, regexp, func, kwargs=None, name=None):
        self.urlmap.append(RegexUrlPattern(re.compile(regexp), func, kwargs, name))

    def map_path(self, path):
        for rp in self.urlmap:
            try:
                return rp.resolve(path)
            except UrlNotMatch:
                pass
        raise UrlNotFound()


if __name__ == '__main__':
    def a():
        return 'a'
    def b():
        return 'b'
    def c(year, month, day):
        return year, month, day
    def d(year=None, month=None, day=None, param=None):
        return year, month, day, param

    urlmap = UrlMap()
    urlmap.add(r'^articles/2003/$', a)
    urlmap.add(r'^articles/(\d{4})/$', b)
    urlmap.add(r'^articles/(\d{4})/(\d{2})/$', c)
    #urlmap.add(r'^articles/(\d{4})/(\d{2})/(\d+)/$', c)
    urlmap.add(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', d)

    path = 'articles/2004/12/21/'
    print urlmap.map_path(path).call()
