from django.shortcuts import render
from django.http import HttpResponse
from json_api import templates
from django.shortcuts import get_object_or_404
from json_api.models import User, ActivityPeriod
from django.conf import settings
import json

#index page
def index(request):
    return render(request, "index.html", context = None)

def populateDatabase(request):
    #Reading data from json file
    with open(str(settings.JSON_PATH)) as file_name:
      user_activity_period_data = json.load(file_name)
    try:
        json.loads(json.dumps(user_activity_period_data))
    except ValueError as err:
        print("Invalid JSON.Exception:{0}".format(str(err)))
        return False

    #Iterating through list of dictionaries
    for data_dict in user_activity_period_data:
        #Getting data from each dictionary
        id = data_dict.get('id')
        real_name = data_dict.get('real_name')
        timezone = data_dict.get('timezone')
        activity_periods = data_dict.get('activity_periods')
        #writing into User table
        try:
            user_object  = User.objects.create(user_id = id, real_name = real_name)
            user_object.save()
            print("User Object created successfully", user_object)
        except Exception as e:
            print(e)
        #writing into ActivityPeriod table
        try:
            activity_period_object  = ActivityPeriod.objects.create(user_id_id = user_object.user_id, time_zone = timezone,\
                                                            activity_period = activity_periods)
            activity_period_object.save()
            print("Activity period Object created successfully", activity_period_object)
            print("Dummy data created")
        except Exception as e:
            print(e)
    return render(request, "databaseCreated.html", context = None)

def deleteDatabase(request):
    ActivityPeriod.objects.all().delete()
    User.objects.all().delete()
    print('Deleted all data successfully')
    return render(request, "databaseDeleted.html", context = None)
