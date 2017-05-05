from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Activity
from .forms import ActForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
# Create your views here.

def main(request):
  #acts = Activity.objects.filter(activateDate__lte=timezone.now()).order_by('createdDate')
  acts = Activity.objects.all()
  paginator = Paginator(acts,5)
  page = request.GET.get('page')
  try:
    acts = paginator.page(page)
  except PageNotAnInteger:
    acts = paginator.page(1)
  except EmptyPage:
    acts = paginator.paginator(paginator.num_pages)
  return render(request,'playmonster/main.html',{'acts':acts})
  
def act_detail(request,pk):
  act = get_object_or_404(Activity, pk=pk)
  return render(request,'playmonster/act_detail.html', {'act':act})
  
def act_new(request):
  if request.method == "POST":
    form = ActForm(request.POST)
    if form.is_valid():
      act = form.save(commit=False)
      act.author = request.user
      act.activateDate = timezone.now()
      act.save()
      return redirect('act_detail', pk=act.pk)
  else:
    form = ActForm()
  return render(request, 'playmonster/act_edit.html', {'form': form})
  
def act_edit(request,pk):
  act = get_object_or_404(Activity, pk=pk)
  if request.method == "POST":
    form = ActForm(request.POST,instance=act)
    if form.is_valid():
      act = form.save(commit=False)
      act.author = request.user
      act.activateDate = timezone.now()
      act.save()
      return redirect('act_detail',pk=act.pk)
  else:
    form = ActForm(instance=act)
  return render(request, 'playmonster/act_edit.html', {'form':form})