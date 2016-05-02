# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^home/', include('home.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


# urlpatterns = [
# 	url(r'^$', include('home.urls')),
#     url(r'^home/', include('home.urls')),
#     url(r'^admin/', admin.site.urls),
# ]

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', admin.site.urls),)
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)