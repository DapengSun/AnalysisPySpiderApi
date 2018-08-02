# coding:utf-8
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from LianJiaSpiderApi.LianJiaSpiderQueue import LianJiaSpiderQueue
from Common.Reponse import json_response
from Common.EnumType import ReponseCode

@csrf_exempt
def index(request):
    return render(request,'index.html')

# 将待爬虫的URL放到任务队列中 进行排队
@require_http_methods(["POST"])
@csrf_exempt
def pushjobqueue(request):
    try:
        requestmodel = json.loads(request.body)
        # 待爬的URL
        _searchSpider = requestmodel.get('searchSpider',None)
        if _searchSpider != None:
            _spiderJob = LianJiaSpiderQueue(_searchSpider)
            _spiderJob.pushjobqueue()
            return json_response(ReponseCode.正常.value, '请求URL加入排队成功','')
        else:
            return json_response(ReponseCode.失败.value, '请求URL加入队列失败','')
    except Exception as ex:
        return json_response(ReponseCode.异常.value, '请求URL加入队列异常',ex.message)


