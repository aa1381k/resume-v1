from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from .models import blog_model, blog_category_model, blog_comments
from user_resume_data.models import basic_info_model

class blogs_list(ListView):
    model = blog_model
    template_name = 'blogs_page.html'
    paginate_by = 6

    def get_queryset(self):
        query = super(blogs_list, self).get_queryset()
        Filter = self.request.GET.get('filter')
        if Filter:
            query = query.filter(category__url_title=Filter, is_active=True)
        else:
            query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(blogs_list, self).get_context_data(**kwargs)
        context['categories'] = blog_category_model.objects.filter(is_active=True)
        context['slider_blogs'] = blog_model.objects.filter(is_active=True).order_by('-create_date')[:3]
        context['random_blogs'] = blog_model.objects.order_by('?')[:3]
        context['filter'] = self.request.GET.get('filter')
        return context



class blog_detail(DetailView):
    model = blog_model
    template_name = 'blog_detail.html'

    def get_queryset(self):
        query = super(blog_detail, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        query = super(blog_detail, self).get_context_data()
        blog : blog_model = kwargs.get('object')
        #blog author info
        author = blog.author.id
        author = basic_info_model.objects.filter(user_base_info_id=author).first()
        query['author'] = author
        #similar blogs
        blog_category = blog.category.first()
        similar_blogs = blog_model.objects.filter(category=blog_category).exclude(id=blog.id).order_by('?')[:3]
        query['similar_blogs'] = similar_blogs
        query['comments'] = blog_comments.objects.filter(blog_id=blog.id, parent_id=None, is_active=True).order_by('-create_date').prefetch_related('blog_comments_set')
        query['all_comments'] = blog_comments.objects.filter(blog_id=blog.id, is_active=True)

        return query


class blog_comment(View):
    def post(self, request, *args, **kwargs):
        blog_id = request.POST.get('blog_id')
        parent_id = request.POST.get('parent_id')
        comment = request.POST.get('text')
        new_blog = blog_comments(blog_id=blog_id, parent_id=parent_id, text=comment, author_id=request.user.id)
        new_blog.save()

        context = {
            'comments': blog_comments.objects.filter(blog_id=blog_id, parent_id=None, is_active=True).order_by('-create_date').prefetch_related('blog_comments_set'),
            'all_comments': blog_comments.objects.filter(blog_id=blog_id, is_active=True)
        }

        return render(request, 'includes/comment_partial.html', context)


