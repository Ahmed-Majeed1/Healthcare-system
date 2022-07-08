from django.contrib import admin
from django.urls import path
from users import views as users_views
from blog import views as blog_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('doctors/', blog_views.doctors, name='doctors'),
    # path('contact/', blog_views.contact, name='contact'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'blog/home.html'), name='logout'),
    path('face_reg/', users_views.face_register, name='face_reg'),
    path('log/', users_views.login, name='log'),
    path('prelogin/', users_views.prelogin, name='prelogin'),
    path('contact/', users_views.send, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
