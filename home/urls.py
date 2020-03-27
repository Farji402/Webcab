from django.urls import path
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static



app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('profile/', views.profile, name='profile'),
    path('setting/', views.setting, name='setting'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('edit/general/', views.edit_general, name='edit_general'),
    path('edit/security/', views.edit_security, name='edit_security'),
    path('profilephoto/', views.upload_dp, name='upload_dp')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
