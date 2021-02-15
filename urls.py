from django.contrib import admin
from django.urls import path
from police_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.HomePage, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('blog', views.blog, name='blog'),
    path('mostwanted', views.mostwanted, name='mostwanted'),
    path('missingperson', views.missingperson, name='missingperson'),
    path('missing', views.missing, name='missing'),
    path('register', views.register, name="register"),
    path('feedback', views.feedback, name="feedback"),
    path('policelogedin', views.policelogedin, name="policelogedin"),
    path('policelogingin', views.policelogingin, name="policelogingin"),
    path('reportcrime', views.reportcrime, name="reportcrime"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
