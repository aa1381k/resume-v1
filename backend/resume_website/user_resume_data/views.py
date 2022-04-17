from django.http import HttpResponse
from django.shortcuts import render
from . models import basic_info
# Create your views here.
from django.views import View


class create_resume(View):
    def get(self, request):
        return render(request, 'create_resume.html')


def user_base_info_ajax(request):
    if request.GET:
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        job_title = request.GET.get('job_title')
        country = request.GET.get('country')
        state = request.GET.get('state')
        city = request.GET.get('city')
        military = request.GET.get('military')
        relationship = request.GET.get('relationship')
        sex = request.GET.get('sex')
        day = request.GET.get('day')
        month = request.GET.get('month')
        year = request.GET.get('year')
        avatar = request.GET.get('avatar')
        user = request.user
        new_info = basic_info(first_name=first_name, last_name=last_name, job_title=job_title, country=country,
                   state=state, city=city, military=military, married=relationship, sex=sex, birth_day=day,
                   birth_month=month, birth_year=year, user_base_info=user
                   )
        new_info.save()
        print(basic_info.objects.filter(user_base_info_id=user.id))
    return HttpResponse('saved')