import json
import ast
from django.http import HttpResponse
from .models import RoomInfo


def post_test(request):
    if request.method == 'POST':
        print("->receive post<-")
        # print(request.GET.urlencode()) #get the data caried by url
        request_str = request.body.decode("utf-8")
        request_dict = ast.literal_eval(request_str)
        response_str = request_dict['RoomID']
        return HttpResponse('receive post request: ' + 'hello, room ' + response_str)
    print("->receive post failed<-")
    query_set = RoomInfo.objects.values()
    room_list = list(query_set)
    return HttpResponse(json.dumps(room_list), content_type="application/json")
