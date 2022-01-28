from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView,DetailView, CreateView


class HomeNews(ListView):
    model = News
    # template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# Create your views here.
# def index(request):
#     news = News.objects.all()
#     return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})
class NewsByCategory(ListView):
    model = News
    # template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # category = Category.objects.get(pk=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     return render(request, 'news/category.html',
#                   {'news': news, 'title': 'Список новостей', 'category': category})

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'


#
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html',
#                   {'news_item': news_item})
class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             new = form.save()
#             return redirect(new)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
