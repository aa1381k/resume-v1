from django.shortcuts import render

# Create your views here.
from django.views import View


class register_page(View):
    def get(self, request):
        return render(request, 'register_page.html')