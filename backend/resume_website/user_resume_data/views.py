from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import basic_info_model, user_socialmedia_model, user_langurage_model, user_skill_model, user_certificate_model,\
    user_education_model, user_job_model, user_projects_model, user_internship_model, user_introduced_model,\
    user_entertainment_model
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.views import View


class create_resume(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            resume = basic_info_model.objects.filter(user_base_info_id=user.id)
            resume_data = basic_info_model.objects.filter(user_base_info_id=user.id, resume_id=0).first()
            count_resume = resume.count()
            user_langurages = user_langurage_model.objects.filter(user_id=user.id).order_by('lang_id')
            user_skills = user_skill_model.objects.filter(user_id=user.id).order_by('skill_id')
            user_socials = user_socialmedia_model.objects.filter(user_id=user.id).order_by('social_id')
            user_certificates = user_certificate_model.objects.filter(user_id=user.id).order_by('certificate_id')
            user_educations = user_education_model.objects.filter(user_id=user.id).order_by('education_id')
            user_jobs = user_job_model.objects.filter(user_id=user.id).order_by('job_id')
            user_projects = user_projects_model.objects.filter(user_id=user.id).order_by('project_id')
            user_internships = user_internship_model.objects.filter(user_id=user.id).order_by('internship_id')
            user_introduced = user_introduced_model.objects.filter(user_id=user.id).order_by('introduced_id')
            user_entertainments = user_entertainment_model.objects.filter(user_id=user.id).order_by('entertainment_id')

            if resume.first() == None or resume.first() == '':

                context = {
                    'resume_id': 0,
                    'user_langurages': user_langurages,
                    'user_skills': user_skills,
                    'resume': resume_data,
                    'user_socialmedias' : user_socials,
                    'user_certificates' : user_certificates,
                    'user_educations' : user_educations,
                    'user_jobs' : user_jobs,
                    'user_projects' : user_projects,
                    'user_internships' : user_internships,
                    'user_introduced' : user_introduced,
                    'user_entertainments' : user_entertainments,
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
                    'user_jobs': user_jobs,
                    'user_projects': user_projects,
                    'user_internships': user_internships,
                    'user_introduced': user_introduced,
                    'user_entertainments': user_entertainments,

                }

            return render(request, 'create_resume.html', context)

        else:
            return redirect('login-page')

    def post(self, request):
        user = request.user
        base_info = basic_info_model.objects.filter(user_base_info_id=user.id).first()

        try:
            upload = request.FILES['avatar']
            fss = FileSystemStorage(location='upload/images/user-profile/', base_url='/medias/')
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)

            file_url = file_url.replace('/medias/','images/user-profile/')


            if base_info != None or base_info != '':
                base_info.avatar = file_url
                base_info.save()

            return redirect('create_resume-page')
        except:
            base_info.avatar.delete()
            base_info.save()
            return redirect('home-page')

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
            resume_id = request.POST.get('resume_id')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            website = request.POST.get('website')
            summary = request.POST.get('summary')
            user = request.user



            if email != '' and first_name != '':
                resume = basic_info_model.objects.filter(user_base_info_id=user.id, resume_id=resume_id).first()

                if resume == None or resume == '':

                    new_info = basic_info_model(first_name=first_name, last_name=last_name, job_title=job_title,
                                          country=country,
                                          state=state, city=city, military=military, married=relationship, sex=sex,
                                          birth_day=day,
                                          birth_month=month, birth_year=year, user_base_info=user,
                                          resume_id=resume_id,phone=phone, email=email, website=website, summary=summary,
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


            if social_media_id is not '':
                social_media = user_socialmedia_model.objects.filter(social_media=social_media_name, user_id=user.id).first()

                if social_media == None:
                    new_user_socialmedia = user_socialmedia_model(social_media=social_media_name, username=social_media_id, user_id=user.id, social_id=social_media_number)
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
            User_langurage = user_langurage_model.objects.filter(lang_id=lang_id, user_id=user.id).first()
            if User_langurage == None:
                new_langurage = user_langurage_model(langurage=lang_name, grade=lang_grade, user_id=user.id, lang_id=lang_id)
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
            skill = user_skill_model.objects.filter(skill_id=skill_id, user_id=user.id).first()
            if skill == None:
                new_user_skill = user_skill_model(skill=skill_name, grade=skill_grade, user_id=user.id, skill_id=skill_id)
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
            certificate = user_certificate_model.objects.filter(certificate_id=certificate_id, user_id=user.id).first()
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
            education = user_education_model.objects.filter(education_id=education_id, user_id=user.id).first()

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

def user_job_ajax(request):
    if request.POST:
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        city = request.POST.get('city')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        text = request.POST.get('text')
        job_id = request.POST.get('job_id')
        user = request.user

        if job_title != '' or job_title != None:
            job = user_job_model.objects.filter(job_id=job_id, user_id=user.id).first()

            if job == None:
                new_job = user_job_model(job_title=job_title, company_name=company_name, city=city,
                                         start_date=start_date, end_date=end_date, text=text,
                                         job_id=job_id, user_id=user.id)

                new_job.save()

            else:
                job.job_title = job_title
                job.company_name = company_name
                job.city = city
                job.start_date = start_date
                job.end_date = end_date
                job.text = text
                job.job_id = job_id
                job.save()

        return HttpResponse('ok')

def user_projects_ajax(request):
    if request.POST:
        title = request.POST.get('project_title')
        employer = request.POST.get('employer')
        link = request.POST.get('link')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        text = request.POST.get('text')
        project_id = request.POST.get('project_id')
        user = request.user

        if title != '' or title != None:
            project = user_projects_model.objects.filter(project_id=project_id, user_id=user.id).first()

            if project == None:
                new_project = user_projects_model(title=title, employer=employer, start_date=start_date,
                                                  end_date=end_date, link=link, text=text, project_id=project_id, user_id=user.id)
                new_project.save()
            else:
                project.title = title
                project.employer = employer
                project.link = link
                project.start_date = start_date
                project.end_date = end_date
                project.text = text
                project.project_id = project_id
                project.save()

    return HttpResponse('ok')

def user_internship_ajax(request):
    if request.POST:
        title = request.POST.get('title')
        employer = request.POST.get('employer')
        city = request.POST.get('city')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        text = request.POST.get('text')
        internship_id = request.POST.get('internship_id')
        user = request.user

        if title != '' or title != None:
            internship = user_internship_model.objects.filter(internship_id=internship_id, user_id=user.id).first()

            if internship == None:
                new_internship = user_internship_model(title=title, employer=employer, city=city, start_date=start_date,
                                                       end_date=end_date, text=text, internship_id=internship_id, user_id=user.id)
                new_internship.save()

            else:
                internship.title = title
                internship.employer = employer
                internship.city = city
                internship.start_date = start_date
                internship.end_date = end_date
                internship.text = text
                internship.internship_id = internship_id
                internship.save()

    return HttpResponse('ok')

def user_introduced_ajax(request):
    if request.POST:
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        introduced_id = request.POST.get('introduced_id')
        user = request.user

        if name != '' or name != None:
            introduced = user_introduced_model.objects.filter(introduced_id=introduced_id, user_id=user.id).first()

            if introduced == None:
                new_introduced = user_introduced_model(name=name, company_name=company_name, phone=phone, email=email,
                                                       introduced_id=introduced_id, user_id=user.id)
                new_introduced.save()

            else:
                introduced.name = name
                introduced.company_name = company_name
                introduced.phone = phone
                introduced.email = email
                introduced.introduced_id = introduced_id
                introduced.save()

    return HttpResponse('ok')

def user_entertainment_ajax(request):
    if request.POST:
        name = request.POST.get('name')
        entertainment_id = request.POST.get('entertainment_id')
        user = request.user

        print('name is: ',name)

        if name != '' or name != None:
            entertainment = user_entertainment_model.objects.filter(entertainment_id=entertainment_id, user_id=user.id).first()

            if entertainment == None:
                new_entartaiment = user_entertainment_model(name=name, entertainment_id=entertainment_id, user_id=user.id)
                new_entartaiment.save()

            else:
                entertainment.name = name
                entertainment.entertainment_id = entertainment_id
                entertainment.save()

    return HttpResponse('ok')

def resume_remove_item(request):
    if request.POST:
        item_name = request.POST.get('item_name')
        item_id = request.POST.get('id')

        if item_name is not '':

            if item_name == 'user-social-media':
                social_media = user_socialmedia_model.objects.filter(social_id__iexact=item_id).first()
                social_media.delete()

        return HttpResponse('ok')
