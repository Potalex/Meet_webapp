from django.shortcuts import render
from django.utils import timezone
from .models import Activity

# Create your views here.

def post_list(request):
  posts = Activity.objects.filter(activateDate__lte=timezone.now()).order_by('activateDate')
  return render(request,'playmonster/post_list.html',{'posts':posts})