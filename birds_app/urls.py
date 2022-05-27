"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from birds_app.views import MainPage, AddBird, BirdList, BirdDetails, AddCommentsView, AddBirdToWishlist, \
    EditBirdDetails, QuizView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', MainPage.as_view(), name='main'),
    path('add-bird/', AddBird.as_view(), name='add-bird'),
    path('bird-list/', BirdList.as_view(), name='bird-list'),
    path('bird/<int:id>/', BirdDetails.as_view(), name='bird-details'),
    path('bird/<int:id>/comment/', AddCommentsView.as_view(), name='add-comment'),
    path('wishlist/', AddBirdToWishlist.as_view(), name='wish-list'),
    path('bird/<int:id>/edit/', EditBirdDetails.as_view(), name='edit-bird'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz-results/', QuizView.as_view(), name='quiz-results'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)