from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from donate import views as donate_views
from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [

    url(r'^$', donate_views.index, name='index'),  # this is for the homepage
    url(r'^admin/', admin.site.urls),

    url(r'^books_list/$', donate_views.books_list, name='books_list'),

    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),

    url(r'^donate_book/$', donate_views.donate_book, name='donate_book'), # name="" kaam lagne ahref bata redirect garna ho
    url(r'^book_detail/(?P<id>\d+)/$', donate_views.book_detail, name = "book_detail"),
    url(r'^book_detail/(?P<id>\d+)/update/$', donate_views.donate_book_update, name = "update"),
    # url(r'^book_detail/(?P<id>\d+)/delete/$', donate_views.delete, name="delete"),

    url(r'^search_list/$', donate_views.search_list, name='search_list'),
    url(r'^contact_us/$', donate_views.contact_us, name='contact_us'),

    url(r'^profile/$', donate_views.profile, name='profile'),
    url(r'^success/$', donate_views.success, name='success'),

    url(r'^test/$', donate_views.test, name='test'),
    url(r'^contributer_board/$', donate_views.contributer_board, name='contributer_board'),

]


#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)