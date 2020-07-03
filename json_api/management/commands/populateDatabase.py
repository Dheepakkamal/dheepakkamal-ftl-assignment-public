from django.core.management.base import BaseCommand
from django.conf import settings
from json_api.models import User, ActivityPeriod
import json

class Command(BaseCommand):
    help = 'Populates dummy data to DB'

    def handle(self, *args, **kwargs):
        #Dummy data creation in DB

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
