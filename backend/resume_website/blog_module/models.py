from django.db import models
from account_module.models import User_model
# Create your models here.

class blog_category_model(models.Model):
    title = models.CharField(max_length=100)
    parrent = models.ForeignKey('blog_category_model',on_delete=models.CASCADE, null=True, blank=True)
    url_title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'



class blog_model(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/blogs', blank=True)
    author = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, allow_unicode=True)
    category = models.ManyToManyField('blog_category_model')
    tags = models.ManyToManyField('blog_tags', blank=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return self.title

    def get_jalali_created_date(self):
        return self.create_date.strftime("%H:%M")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['title']



class blog_tags(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Tag'
        verbose_name_plural = 'Blog Tags'
        ordering = ['title']


class blog_comments(models.Model):
    author = models.ForeignKey(User_model, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(blog_model, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('blog_comments', on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.author.get_full_name()

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'
        ordering = ['create_date']