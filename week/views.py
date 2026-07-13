from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

_dict={
  "1":"saturday",
  "2":"sunday",
  "3":"monday",
  "4":"tuesday",
  "5":"wendensday",
  "6":"thursday",
  "7":"friday"
}
# Create your views here.
def weekly(request,week_id):

    if week_id in _dict:
        return HttpResponse(_dict[week_id])
    else :
        return HttpResponseNotFound("the day isn't in week")