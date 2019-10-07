from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ModelTestDB

# Create your views here.
def main_page(request):
    return HttpResponse("Main page")
@login_required(redirect_field_name='login_page')
def char_page(request, ch1, ch2, int1=0):
    ModelTestDB.objects.create(ch1=ch1, ch2=ch2, int1=int1)
    context ={'db':ModelTestDB.objects.all()}
    return render(request,'char_list.html', context=context)
