from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView


class blogs_list(View):
    def get(self, request):
        return render(request, 'blogs_page.html')

