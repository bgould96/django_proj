from django.shortcuts import render

from .models import *

import datetime, GroupMeFunctions, string

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

required_ids = [""]

@csrf_exempt
def index(request):

        return HttpResponse("Group Me.")

def update_db(request):

        #Update Groups

        meta, groups = GroupMeFunctions.gm_get("/groups")

        for group in groups:
                id = group["id"]
                name = group["name"]
                group_obj, created = Group.objects.get_or_create(
                        group_id = id
                )

                if not created:
                        group_obj.group_name = name
                        group_obj.save()

        #Update Users

        for group in Group.objects.all():
            if group.tracked:
                users = GroupMeFunctions.get_group_members(group.group_id)

                camp = Camp.objects.get(camp_name="None")

                if group.group_id == "19550834":
                    camp = Camp.objects.get(camp_name="Bishop")

                for user in users:

                    id = user["user_id"]
                    name = user["nickname"]

                    user_obj, updated = User.objects.update_or_create(
                        user_id = id,
                        defaults = {
                            "camp" : camp,
                            "user_name" : name,
                        }
                    )



        return HttpResponse("Database Updated.")

@csrf_exempt
def functions(request):
    data = request.POST



    GroupMeFunctions.send_bot_message_to_group("f6c64113661287ad36f855469a", request.method)



    return HttpResponse("")

@csrf_exempt
def hilg_attack(request):
    group_id = "22719166"

    GroupMeFunctions.gm_post(
        "/groups/join",
        {'group_id' : group_id}
    )

    resp = GroupMeFunctions.send_user_message_to_group(group_id, "This was sent by the server.")

    return HttpResponse(resp);