from django.conf.urls import url
from django.contrib import admin
from apps.lists.views import home_page


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
]
