from Scripts.bottle import post
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.crypto import get_random_string
from django.views import View
from .forms import Register_form, Login_form, Forgotpassword_form, Resetpassword_form
from .models import User_model
from utils.send_email import send_email
from user_resume_data.models import basic_info_model, user_skill_model, user_job_model, user_education_model,\
user_projects_model
from django.core.files.storage import FileSystemStorage
from account_module.models import user_work_samples, work_samples_image



class profile_view(View):
    def get(self, request):
        if request.user.is_authenticated:

            user = request.user
            user_account = basic_info_model.objects.filter(user_base_info_id=user.id).first()
            user_full_name = user_account.first_name + " " + user_account.last_name
            user_skills = user_skill_model.objects.filter(user_id=user.id)
            user_jobs = user_job_model.objects.filter(user_id=user.id)
            user_education = user_education_model.objects.filter(user_id=user.id)
            user_project = user_projects_model.objects.filter(user_id=user.id)
            # theme_color = User_model.objects.filter(basic_info_model__resume_id=user.id).first()
            # print(theme_color)


            context = {
                'user': user_account,
                'user_full_name': user_full_name,
                'user_skills': user_skills,
                'user_jobs': user_jobs,
                'user_education': user_education,
                'user_projects': user_project,
            }
            return render(request, 'profile.html', context)
        return redirect('home-page')

class add_work_samples(View):
    def post(self, request):
        user = request.user
        post_title = request.POST.get('post_title')
        post_id = request.POST.get('post_id')
        post_description = request.POST.get('post_description')
        post_link = request.POST.get('post_link')

        work_samples = user_work_samples.objects.filter(post_id=post_id, user_id=user.id).first()
        user_work_samples_lenght = len(user_work_samples.objects.filter(user_id=user.id))

        if work_samples == None:
            if user_work_samples_lenght == 0:
                user_work_samples_lenght = 0
            else:
                user_work_samples_lenght += 1
            new_work_samples_post = user_work_samples(user_id=user.id, post_id=user_work_samples_lenght,
                                                      post_title=post_title, post_description=post_description,
                                                      post_link=post_link)
            new_work_samples_post.save()

            uploads = request.FILES.getlist('post_image')

            for upload in uploads:
                fss = FileSystemStorage(location='upload/images/work-samples/', base_url='/medias/')
                file = fss.save(upload.name, upload)
                file_url = fss.url(file)

                file_url = file_url.replace('/medias/', 'images/work-samples/')

                new_work_samples_post_image = work_samples_image(user_id=user.id, post_id=user_work_samples_lenght,
                                                                 post_image=file_url)
                new_work_samples_post_image.save()


            return redirect("profile-page")






class register_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home-page')
        else:
            register_form = Register_form()
            context = {
                'forms': register_form
            }
            return render(request, 'register.html', context)

    def post(self, request):
        register_form = Register_form(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            user = User_model.objects.filter(email__iexact=email)

            if user:
                register_form.add_error('email','این ایمیل قبلا ثبت نام شده است.')

            else:
                new_user = User_model(email=email,
                                      email_active_code=get_random_string(72),
                                      is_active=False,
                                      username=email
                                      )
                new_user.set_password(password)
                new_user.save()
                send_email('ثبت نام در رزومه ساز علی', email,{'user':new_user},'emails/active_email_template.html')

                return redirect('home-page')

        context = {
            'forms': register_form
        }
        return render(request, 'register.html', context)



class Login(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = Login_form()
            context = {
                'forms' : form
            }
            return render(request, 'login.html', context)
        return redirect('home-page')

    def post(self, request):
        form = Login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User_model.objects.filter(email__iexact=email).first()
            if user is not None:
                if not user.is_active:
                    form.add_error('email', 'این حساب کاربری غیر فعال است')
                else:
                    is_password_correct = user.check_password(password)
                    if is_password_correct:
                        login(request, user)
                        return redirect('home-page')
                    else:
                        form.add_error('password', 'کلمه عبور اشتباه است')
                        # return redirect('login-page')
            else:
                form.add_error('email', 'کاربری با این مشخصات یافت نشد')
        context = {
            'forms' : form
        }
        return render(request, 'login.html', context)


class Loguot(View):
    def get(self, request):
        logout(request)
        return redirect('home-page')


class activate_account(View):
    def get(self, request, active_code):
        user = User_model.objects.filter(email_active_code__iexact=active_code).first()
        try:
            if user is not None:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect('home-page')
        except:
            pass


class Forgotpassword(View):
    def get(self, request):
        form = Forgotpassword_form()
        context = {
            'forms' : form
        }
        return render(request, 'forgotpass.html', context)

    def post(self, request):
        form = Forgotpassword_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User_model.objects.filter(email__iexact=email).first()
            if user:
                send_email('بازیابی کلمه عبور', email, {'user':user},'emails/resetpass_email_template.html')
                return redirect('home-page')
            else:
                form.add_error('email','ایمیل یافت نشد.')
        context = {
            'forms' : form
        }
        return render(request, 'forgotpass.html', context)


class Resetpassword(View):
    def get(self, request, active_code):
        form = Resetpassword_form()

        user = User_model.objects.filter(email_active_code__iexact=active_code).first()
        if user:
            context = {
                'forms' : form,
                'user' : user,
            }
            return render(request, 'resetpass.html', context)
        else:
            form.add_error('password', 'کاربری با این مشخصات یافت نشد')

    def post(self, request, active_code):
        form = Resetpassword_form(request.POST)
        if form.is_valid():
            user = User_model.objects.filter(email_active_code__iexact=active_code).first()
            if user:
                new_password = form.cleaned_data.get('password')
                user.set_password(new_password)
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect('login-page')
            else:
                form.add_error('password', 'کاربری با این مشخصات یافت نشد')
        context = {
            'forms': form,
        }
        return render(request, 'resetpass.html', context)