

from django.views.generic import ListView, DetailView
from .models import Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Article
    template_name = "index.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "details.html"
    context_object_name = "batman"


class CreateArticleView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = '__all__'


class CreateUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'text']


class CreateDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('home')
    context_object_name = 'batman'



