from rest_framework.views import APIView
from django.http.response import JsonResponse
from json_api.models import User, ActivityPeriod

class UserActivityPeriod(APIView):
    def get(request, format=None):
        print("GET method")
        user_object = User.objects.all()
        activity_period_object = ActivityPeriod.objects.all()
        members = list()
        for user in user_object:
            id = user.user_id
            real_name = user.real_name
            for activity_period in activity_period_object:
                if id == activity_period.user_id_id:
                    user_activity_dict = {
                                            "id" : id,
                                            "real_name" : real_name,
                                            "tz" : activity_period.time_zone,
                                            "activity_periods" : activity_period.activity_period
                                        }
                    members.append(user_activity_dict)


        return JsonResponse({
                            'ok' : True,
                            'members' : members
                            })
