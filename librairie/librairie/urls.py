
from django.contrib import admin
from django.urls import path
from livres.views import home,formulaire
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('forms', formulaire),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, 
    document_root = settings.MEDIA_ROOT)
