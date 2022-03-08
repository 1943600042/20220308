from django.http import HttpResponse
from django.template import Template,Context
from django.http import HttpResponseRedirect




# 首页
def index(request):
    return HttpResponse("hello world")


def about(requset):
    return HttpResponse("aaaaaa")


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


    return HttpResponse(result)


from django.template.loader import get_template


def get_index(request):

    parm = {'name': 'wang', 'age': 213}

    template_obj = get_template("index.html")

    result = template_obj.render(parm)

    return HttpResponse(result)


from django.shortcuts import render_to_response


def oneindex(request):
    parm = {'name': 'xian', 'age': 343}
    return render_to_response('index.html',parm)
    pass

