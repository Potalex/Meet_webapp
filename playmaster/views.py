from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Activity

# Create your views here.

def main(request):
  posts = Activity.objects.filter(activateDate__lte=timezone.now()).order_by('activateDate')
  return render(request,'playmonster/main.html',{'posts':posts})
  
def act_detail(request,pk):
  act = get_object_or_404(Activity, pk=pk)
  return render(request,'playmonster/act_detail.html', {'act':act})