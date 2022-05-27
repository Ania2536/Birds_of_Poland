from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)