from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .utils import *


# Create your views here.


class RecipesHome(DataMixin, ListView):
    model = Recipes
    template_name = 'resbook/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Recipes")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Recipes.objects.filter(is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Page Not Found</h1>')


def about(request):
    return render(request, 'resbook/about.html', {'title': 'About Us'})


def login(request):
    return HttpResponse('Authorization')


class RecipesCategory(DataMixin, ListView):
    model = Recipes
    template_name = 'resbook/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Recipes.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Category-" + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Recipes
    template_name = 'resbook/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(titile=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'resbook/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    rise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Recipe")
        return dict(list(context.items()) + list(c_def.items()))
