import json
from django.http import HttpResponse
from .models import RoomInfo


def get_test(request):
    if request.method == 'GET':
        print("->receive get request<-")
        # print(request.GET.urlencode())
        query_set = RoomInfo.objects.values()
        room_list = list(query_set)
        return HttpResponse(json.dumps(room_list), content_type="application/json")
    print("->receive get failed<-")
    return HttpResponse("get test failed")
