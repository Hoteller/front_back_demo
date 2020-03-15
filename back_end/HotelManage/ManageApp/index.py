import json
from django.http import HttpResponse
from .models import RoomInfo


def index(request):
    query_set = RoomInfo.objects.values()
    room_list = list(query_set)
    return HttpResponse(json.dumps(room_list), content_type="application/json")
