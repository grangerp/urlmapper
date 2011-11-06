# -*- coding: utf-8 -*-
'''
Created on 2011-11-06

@author: pgranger
'''
import unittest

from tests.tests import TestUrlMap

def runtests():
    unittest.TestLoader().loadTestsFromTestCase(TestUrlMap)
    unittest.main()

if __name__ == '__main__':
    runtests()
