import ast
from django.http import HttpResponse


def post_test(request):
    if request.method == 'POST':
        print("->receive post<-")
        # print(request.GET.urlencode()) #get the data caried by url
        # body部分是一个字节串，需要先转换为string再转换为dict
        request_str = request.body.decode("utf-8")
        request_dict = ast.literal_eval(request_str)
        response_str = request_dict['RoomID']
        return HttpResponse('receive post request: ' + 'hello, room ' + response_str)
    print("->receive post failed<-")
    return HttpResponse("post analyse failed")
