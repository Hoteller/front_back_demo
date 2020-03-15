import json
from django.http import HttpResponse
from .models import RoomInfo


def get_test(request):
    if request.method == 'GET':
        print("->receive get request<-")
        # print(request.GET.urlencode())    #如果GET请求带参数，需要使用此行的函数读取
        query_set = RoomInfo.objects.values()  # 查询数据库，返回所有内容
        room_list = list(query_set)  # 将QuerySet类转换为list
        # 封装json，回复一个json类型的HttpResponse
        return HttpResponse(json.dumps(room_list), content_type="application/json")
    print("->receive get failed<-")
    return HttpResponse("get test failed")
