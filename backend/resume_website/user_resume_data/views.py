from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import basic_info, user_socialmedia, user_langurage, user_skill, user_certificate_model, user_education_model
# Create your views here.
from django.views import View


class create_resume(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            resume = basic_info.objects.filter(user_base_info_id=user.id)
            resume_data = basic_info.objects.filter(user_base_info_id=user.id, resume_id=0).first()
            count_resume = resume.count()
            user_langurages = user_langurage.objects.filter(user_id=user.id).order_by('lang_id')
            user_skills = user_skill.objects.filter(user_id=user.id).order_by('skill_id')
            user_socials = user_socialmedia.objects.filter(user_id=user.id).order_by('social_id')
            user_certificates = user_certificate_model.objects.filter(user_id=user.id).order_by('certificate_id')
            user_educations = user_education_model.objects.filter(user_id=user.id).order_by('education_id')
            if resume.first() == None or resume.first() == '':

                context = {
                    'resume_id': 0,
                    'user_langurages': user_langurages,
                    'user_skills': user_skills,
                    'resume': resume_data,
                    'user_socialmedias' : user_socials,
                    'user_certificates' : user_certificates,
                    'user_educations' : user_educations,
                }

            else:

                context = {
                    'resume_id': 0,
                    'user_langurages': user_langurages,
                    'user_skills': user_skills,
                    'resume': resume_data,
                    'user_socialmedias': user_socials,
                    'user_certificates': user_certificates,
                    'user_educations': user_educations,

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

                if resume == None or resume == '':

                    new_info = basic_info(first_name=first_name, last_name=last_name, job_title=job_title,
                                          country=country,
                                          state=state, city=city, military=military, married=relationship, sex=sex,
                                          birth_day=day,
                                          birth_month=month, birth_year=year, user_base_info=user, avatar=avatar,
                                          resume_id=resume_id,
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

            else:
                return HttpResponse('error')

        return HttpResponse('datasaved')

def user_socialmedia_ajax(request):
    if request.POST:
        if request.user.is_authenticated:
            user = request.user
            social_media_name = request.POST.get('social_media_name')
            social_media_id = request.POST.get('social_media_id')
            social_media_number = request.POST.get('social_media_number')
            print(social_media_number)

            if social_media_name != '' and social_media_id != '':
                social_media = user_socialmedia.objects.filter(social_media=social_media_name, user_id=user.id).first()

                if social_media == None or social_media == '':
                    new_user_socialmedia = user_socialmedia(social_media=social_media_name, username=social_media_id, user_id=user.id, social_id=social_media_number)
                    new_user_socialmedia.save()

                else:
                    social_media.social_media = social_media_name
                    social_media.username = social_media_id
                    social_media.social_id = social_media_number
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

        if skill_name != '' or skill_name != None:
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

def user_certificate(request):
    if request.POST:
        certificate_title = request.POST.get('certificate_title')
        organization_title = request.POST.get('organization_title')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        certificate_id = request.POST.get('certificate_id')
        user = request.user

        if certificate_title != '' or certificate_title != None:
            certificate = user_certificate_model.objects.filter(certificate_title=certificate_title, user_id=user.id).first()
            if certificate == None:
                new_certificate = user_certificate_model(certificate_title=certificate_title,
                                                   organization_title=organization_title, start_date=start_date,
                                                   end_date=end_date, certificate_id=certificate_id, user_id=user.id)
                new_certificate.save()
            else:
                certificate.certificate_title = certificate_title
                certificate.organization_title = organization_title
                certificate.start_date = start_date
                certificate.end_date = end_date
                certificate.certificate_id = certificate_id
                certificate.save()


        return HttpResponse('ok certificate')

def user_education_ajax(request):
    if request.POST:
        education_title = request.POST.get('education_title')
        education_grade = request.POST.get('education_grade')
        university_name = request.POST.get('university_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        text = request.POST.get('text')
        education_id = request.POST.get('education_id')
        user = request.user

        if education_title != '' or education_title != None:
            education = user_education_model.objects.filter(education_title=education_title, user_id=user.id).first()

            if education == None:
                new_education = user_education_model(education_title=education_title, education_grade=education_grade,
                                                      university_name=university_name, start_date=start_date,
                                                     end_date=end_date, text=text, education_id=education_id,
                                                     user_id=user.id)
                new_education.save()

            else:
                education.education_title = education_title
                education.education_grade = education_grade
                education.university_name = university_name
                education.start_date = start_date
                education.end_date = end_date
                education.text = text
                education.education_id = education_id
                education.save()

        return HttpResponse('ok education')
