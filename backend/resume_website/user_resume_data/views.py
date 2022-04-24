from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import basic_info, user_socialmedia, user_langurage, user_skill
# Create your views here.
from django.views import View


class create_resume(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            resume = basic_info.objects.filter(user_base_info_id=user.id)
            count_resume = resume.count()
            user_langurages = user_langurage.objects.filter(user_id=user.id).order_by('lang_id')
            user_skills = user_skill.objects.filter(user_id=user.id).order_by('skill_id')
            if resume.first() == None or resume.first() == '':

                context = {
                    'resume_id': 0,
                    'user_langurages': user_langurages,
                    'user_skills': user_skills,
                }

            else:

                context = {
                    'resume_id': count_resume + 1,
                    'user_langurages': user_langurages,

                }

            return render(request, 'create_resume.html', context)

        else:
            return redirect('login-page')


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

def user_langurages_ajax(request):
    if request.POST:
        lang_name = request.POST.get('lang_name')
        lang_grade = request.POST.get('lang_grade')
        lang_id = request.POST.get('lang_id')
        user = request.user
        if lang_name != '' or lang_name != None:
            User_langurage = user_langurage.objects.filter(langurage=lang_name, user_id=user.id).first()
            if User_langurage == None:
                new_langurage = user_langurage(langurage=lang_name, grade=lang_grade, user_id=user.id, lang_id=lang_id)
                new_langurage.save()
            else:
                User_langurage.langurage = lang_name
                User_langurage.grade = lang_grade
                User_langurage.lang_id = lang_id
                User_langurage.save()

    return HttpResponse('langurage saved')

def user_skills_ajax(request):
    if request.POST:
        skill_name = request.POST.get('skill_name')
        skill_grade = request.POST.get('skill_grade')
        skill_id = request.POST.get('skill_id')
        user = request.user

        if skill_name !='' or skill_name != None:
            skill = user_skill.objects.filter(skill=skill_name, user_id=user.id).first()

            if skill == None:
                new_user_skill = user_skill(skill=skill_name, grade=skill_grade, user_id=user.id, skill_id=skill_id)
                new_user_skill.save()

            else:
                skill.skill = skill_name
                skill.grade = skill_grade
                skill.skill_id = skill_id
                skill.save()

        return HttpResponse('skill saved')