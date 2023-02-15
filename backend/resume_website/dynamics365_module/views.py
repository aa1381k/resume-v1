from django.shortcuts import render, HttpResponse
from django.views.generic import View
from user_resume_data.models import basic_info_model
import json

# Create your views here.


class datainfo(View):
    def get(self,request):

        get_contact = "get-contact"
        get_case = "get-case"

        context = {
            "get_contact" : get_contact,
            "get_case" : get_case,
        }

        return render(request, "home.html", context)




def Get_contact(request):
    users = basic_info_model.objects.all()
    users_json = {}
    for i in range(users.count()):
        user_info = f"{users[i].first_name} {users[i].last_name}",f"{users[i].phone}"

        users_json[f"user_{i}"] = user_info

    y = json.dumps(users_json, ensure_ascii=False)


    return HttpResponse(y)