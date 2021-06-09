from django.conf.urls import url
from django.urls import path

from resbook import views
from resbook.views import *

urlpatterns = [
    path('', RecipesHome.as_view(), name='home'),
    path(r'about/', views.about, name='about'),
    path(r'login/', LoginUser.as_view(), name='login'),
    path(r'signin/', RegisterUser.as_view(), name='signin'),
    path(r'addpage/', AddPage.as_view(), name='addpage'),
    path(r'sigout/', views.logout_user, name='signout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', RecipesCategory.as_view(), name='category'),
]
