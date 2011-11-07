==========
Url Mapper
==========

Example
=======

Create map::

   from urlmapper import UrlMap
   
   urlmap = UrlMap()
   urlmap.add(r'^articles/2003/$', view1)
   urlmap.add(r'^articles/(\d{4})/$', view2, 
      {'extra_param_pass_to_the_view1': 'john','extra_param_pass_to_the_view1': 'doe'})
   urlmap.add(r'^articles/(\d{4})/(\d{2})/$', view3, name='read_article')
   urlmap.add(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',view4)
   
Use map to resolve::
   
   try:
      match = urlmap.map_path(path)
   except UrlNotFound:
      # doe something
      pass
      
   view_result = match.call()
   
TODOs
=====

Reverse resolve by name::
   
   urlmap = UrlMap()
   urlmap.add(r'^articles/2003/$', view1, name='article1')
   urlmap.add(r'^articles/(\d{4})/$', view2, name='article2')
   urlmap.add(r'^articles/(?P\d{4})/$', view3, name='article3')
   
   urlmap.reverse('article1') # return article/2003/
   urlmap.reverse('article2','2004') # return article/2004/
   urlmap.reverse('article2', year='2005') # return article/2005/
    