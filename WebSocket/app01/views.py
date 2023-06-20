import  queue
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.

USER_QUEUR={
}
def index(request):
    qq_group_num=request.GET.get('num')
    return  render(request,'index.html',{"qq_group_num":qq_group_num})
#
# def home(request):
#     uid=request.GET.get('uid')
#     USER_QUEUR[uid]=queue.Queue()
#     return render(request,"home.html",{"uid":uid})
#     pass
# def sendmsg(request):
#     text=request.GET.get('text')
#     for uid,q in USER_QUEUR.items():
#         q.put(text)
#     return  HttpResponse('OK')
# def getmsg(request):
#     #各自去各自队列获取数九，需要明白自己的uid
#     uid=request.GET.get('uid')
#     q=USER_QUEUR[uid]#根据自己的uid，获取自己的队列
#     result={'status':True,'data':None}
#     try:
#         data=q.get(timeout=10)
#         result["data"]=data
#     except queue.Empty as e:
#         result["status"] = False
#     print(result)
#     return JsonResponse(result)
#
