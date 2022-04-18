from django.http import HttpResponse
from django.shortcuts import render
from . models import basic_info
# Create your views here.
from django.views import View


class create_resume(View):
    def get(self, request):
        user = request.user
        resume = basic_info.objects.filter(user_base_info_id=user.id)
        count_resume = resume.count()
        if resume.first() == None or resume.first() == '':

            context = {
                'resume_id': 0
            }

        else:

            context = {
                'resume_id': count_resume+1
            }

        return render(request, 'create_resume.html', context)


def user_base_info_ajax(request):
    if request.GET:
        if request.user.is_authenticated:
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
            resume_id = request.GET.get('resume_id')
            phone = request.GET.get('phone')
            email = request.GET.get('email')
            website = request.GET.get('website')
            summary = request.GET.get('summary')
            user = request.user


            if email != '' and first_name != '':
                resume = basic_info.objects.filter(user_base_info_id=user.id, resume_id=resume_id).first()
            else:
                return HttpResponse('error')


            if resume == None:

                new_info = basic_info(first_name=first_name, last_name=last_name, job_title=job_title, country=country,
                           state=state, city=city, military=military, married=relationship, sex=sex, birth_day=day,
                           birth_month=month, birth_year=year, user_base_info=user, avatar=avatar, resume_id=resume_id,
                           phone=phone, email=email, website=website, summary=summary,
                           )
                new_info.save()

            else:

                resume.first_name = first_name
                resume.last_name = last_name
                resume.job_title = job_title
                resume.country = country
                resume.state = state
                resume.city = city
                resume.military = military
                resume.married = relationship
                resume.sex = sex
                resume.birth_day = day
                resume.birth_month = month
                resume.birth_year = year
                resume.avatar = avatar
                resume.summary = summary
                resume.website = website
                resume.phone = phone
                resume.email = email
                resume.save()

        return HttpResponse('datasaved')

def user_socialmedia_ajax(request):
    if request.POST:
        print('ok')
    return HttpResponse('ok social')