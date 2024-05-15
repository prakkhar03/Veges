from django.contrib import admin
from django.urls import path
from vege.views import *
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('frontpage/', frontpage, name='front'),
    path('recipe/', receipies, name='receipes'), 
    path('uploaded/', upload, name='uploaded'),
    path('delete/<id>/', delete, name='delete'),
    path('update/<id>/', update, name='update'),
    path('manage/', manage, name='manage'),
    path('', loginpage, name='login'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
