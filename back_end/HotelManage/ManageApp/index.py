import json
from django.http import HttpResponse
from .models import RoomInfo

# 直接进入127.0.0.1:8000可以看到一个json回复
def index(request):
    query_set = RoomInfo.objects.values()
    room_list = list(query_set)
    return HttpResponse(json.dumps(room_list), content_type="application/json")
