from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from .models import Article
from .forms import ArticleForm
# Create your views here.


# class ListArticle(ListView):
#     template_name = "article/article_list_abc.html"
#     queryset = Article.objects.all()
#     context_object_name = "articles"


# class DetailArticle(DetailView):
#     template_name = "article/article_detail.html"
#     context_object_name = "article"
#     queryset = Article.objects.all()

#     def get_object(self):
#         _id = self.kwargs.get("id")
#         return get_object_or_404(Article, id=_id)


# class CreateArticle(CreateView):
#     template_name = "article/article_create.html"
#     form_class = ArticleForm


# class UpdateArticle(UpdateView):
#     template_name = "article/article_update.html"
#     form_class = ArticleForm

#     def get_object(self):
#         id = self.kwargs.get("id")
#         return get_object_or_404(Article, id=id)


# function base view to class base view
class ArticleObjectMixin(object):
    model = Article
    lookup = "id"

    def get_object(self):
        lookup = self.kwargs.get(self.lookup)
        obj = None
        if lookup is not None:
            obj = get_object_or_404(self.model, id=lookup)
        return obj


class ListArticle(View):
    queryset = Article.objects.all()
    template_name = "article/article_list_abc.html"
    context_object_name = "articles"

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            "articles": self.get_queryset()
        }
        return render(request, self.template_name, context)


class DetailArticle(ArticleObjectMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        context["article"] = obj
        return render(request, "article/article_detail.html", context)


class CreateArticle(View):
    template_name = "article/article_create.html"

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArticleForm()
        context = {
            "form": form
        }
        return render(request, "article/article_create.html", context)


class UpdateArticle(ArticleObjectMixin, View):
    template_name = "article/article_update.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = ArticleForm(instance=obj)
            context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArticleForm()

        context = {
            "form": form
        }

        return render(request, self.template_name, context)
