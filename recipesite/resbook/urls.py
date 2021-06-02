from django.conf.urls import url
from django.urls import path

from resbook import views
from resbook.views import *

urlpatterns = [
    url(r'^$', RecipesHome.as_view(), name='home'),
    url(r'about/', views.about, name='about'),
    url(r'login/', views.login, name='login'),
    url(r'addpage/', AddPage.as_view(), name='addpage'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', RecipesCategory.as_view(), name='category'),
]
