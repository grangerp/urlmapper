# -*- coding: utf-8 -*-
'''
Created on 2011-11-06

@author: pgranger
'''
import unittest

from urlmapper import UrlMap, UrlNotFound

class TestUrlMap(unittest.TestCase):
    def setUp(self):

        def rettest(*args, **kwargs):
            return args, kwargs

        self.urlmap = UrlMap()
        self.urlmap.add(r'^articles/2003/$', rettest)
        self.urlmap.add(r'^articles/(\d{4})/$', rettest)
        self.urlmap.add(r'^articles/(\d{4})/(\d{2})/$', rettest)
        self.urlmap.add(
            r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
            rettest)

    def test_noargs(self):
        # make sure it map no args
        path = 'articles/2003/'
        self.assertEqual(self.urlmap.map_path(path).call(), ((), {}))

        # should raise an exception for an immutable sequence
        #self.assertRaises(TypeError, random.shuffle, (1, 2, 3))
    def test_oneargs(self):
        path = 'articles/2004/'
        self.assertEqual(self.urlmap.map_path(path).call(), (('2004',), {}))

    def test_kwargss(self):
        path = 'articles/2004/12/01/'
        self.assertEqual(self.urlmap.map_path(path).call(),
            ((), {'day': '01', 'month': '12', 'year': '2004'}))

    def test_urlnotmatch(self):
        path = 'article/2004/12/01/'
        self.assertRaises(UrlNotFound, self.urlmap.map_path, path)
