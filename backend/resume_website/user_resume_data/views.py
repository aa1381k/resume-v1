from django.http import HttpResponse
from django.shortcuts import render
from . models import basic_info, user_socialmedia
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
    if request.POST:
        if request.user.is_authenticated:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            job_title = request.POST.get('job_title')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            military = request.POST.get('military')
            relationship = request.POST.get('relationship')
            sex = request.POST.get('sex')
            day = request.POST.get('day')
            month = request.POST.get('month')
            year = request.POST.get('year')
            avatar = request.POST.get('avatar')
            resume_id = request.POST.get('resume_id')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            website = request.POST.get('website')
            summary = request.POST.get('summary')
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
        if request.user.is_authenticated:
            social_media_name = request.POST.get('social_media_name')
            social_media_id = request.POST.get('social_media_id')
            social_media_number = request.POST.get('social_media_number')

            print(social_media_id, social_media_number, social_media_name)

            if social_media_name != '' and social_media_id != '':
                social_media = user_socialmedia.objects.filter(social_media=social_media_name, username__exact=social_media_id).first()

            if social_media == None or social_media == '':
                new_user_socialmedia = user_socialmedia(social_media=social_media_name, username=social_media_id, social_id=social_media_number)
                new_user_socialmedia.save()

            else:
                social_media.social_media = social_media_name
                social_media.username = social_media_id
                social_media.save()
    return HttpResponse('ok social')