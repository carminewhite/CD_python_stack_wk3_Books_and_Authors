from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^books/(?P<my_id>\d+)$', views.books),
    url(r'^view_author/(?P<my_id>\d+)$', views.view_author),
    url(r'^authors/(?P<my_id>\d+)$', views.add_authors),
    url(r'^add_book_to_author$', views.add_book_to_author),
    url(r'^add_author_to_book$', views.add_author_to_book),
    url(r'^add_book$', views.add_book),
    url(r'^add_authors$', views.add_authors),
    url(r'^del_book$', views.del_book),
]