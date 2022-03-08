from django.http import HttpResponse


# 首页
def index(request):
    return HttpResponse("hello world")


def about(requset):
    return HttpResponse("aaaaaa")


def re_send(request):
    return HttpResponse('bbbbbb')

def test(request,id,type):
    dend = '我在那{}，你在哪{}'.format(id,type)
    return HttpResponse(dend)



