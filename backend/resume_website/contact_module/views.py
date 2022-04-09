from django.shortcuts import render

# Create your views here.
from django.views import View


class contact_page(View):
    def get(self, request):
        return render(request, 'contact_page.html')