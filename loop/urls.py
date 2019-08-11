from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url('^$',views.index,name = 'index'),
   url('^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name = 'edit_profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)