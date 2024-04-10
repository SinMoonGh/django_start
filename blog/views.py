from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import FormView
from django.views.generic.dates import BaseDayArchiveView, TodayArchiveView
from blog.models import Post
from django.conf import settings
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.order_by('-id')


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
    #     context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
    #     context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
    #     context['disqus_title'] = f"{self.object.slug}"
    #     return context
    

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'


# class TagCloudTV(TemplateView):
#     template_name = 'taggit/taggit_cloud.html'


# class TaggedObjectLV(ListView):
#     template_name = 'taggit/taggit_post_list.html'
#     model = Post

#     def get_queryset(self) -> QuerySet[Any]:
#         return Post.objects.filter(tags__name = self.kwargs.get('tag'))
    
#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['tagname'] = self.kwargs['tag']
#         return context
    


    

"""
1. 검색어 확인
2. q를 통해 검색하고
3. 결과를 담아
4. 페이지에 전달.
"""
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        search_word = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains=search_word) | Q(description__icontains=search_word) |
            Q(content__icontains=search_word)
        ).distinct()
        context = {'form' : form,'post_list': post_list, 'search_word': search_word}
        return self.render_to_response(context)
