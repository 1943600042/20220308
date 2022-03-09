from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import render_to_response


# 首页
def index(request):
    return render_to_response('index.html')


def about(requset):
    return render_to_response('about.html')


def re_send(request):
    return HttpResponse('bbbbbb')


def test(request,id,type):
    dend = '我在那{}，你在哪{}'.format(id,type)
    print(dend)
    return HttpResponse(dend)


def indexhtml(request,id):
    html = """
    <html>
        <head></head>
        <body>
            <h1>name</h1>
        </body>
        姓名：{{name}}
        年龄：{{age}}
    </html>
    """
    template_obj = Template(html)
    parmas = {'name': 'wang', 'age': id}
    content_obj = Context(parmas)
    result = template_obj.render(content_obj)
    print(result)
    return HttpResponse(result)


# def get_index(request):
#
#     parm = {'name': 'wang', 'age': 213}
#
#     template_obj = get_template("index.html")
#
#     result = template_obj.render(parm)
#     print(result)
#     return HttpResponse(result)
#
#
# def oneindex(request):
#     parm = {'name': 'xian', 'age': 343}
#     return render_to_response('index.html',parm)
#     pass
#
#
# def twoindex(request):
#     parm = {'name': 'spend', 'age': 343}
#     return render(request, 'index.html', parm)
#
#
# def temptest(request):
#     name = {'st': '12', 'pe': '33'}
#     age = [12, 22]
#     ap = 20
#     lst = [3,1,34,21]
#     # return render_to_response('index.html',{'name':name,'age':age})
#     return render_to_response('index.html', locals())


def statictest(request):
    age = 20
    return render_to_response('statichtml.html',locals())


def listpic(request):
    return render_to_response('listpic.html')


def newlistpic(request):
    return render_to_response('newlistpic.html')


def statichtml(request):
    age = 20
    return render_to_response('statichtml.html',locals())


