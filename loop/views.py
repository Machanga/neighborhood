from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Neighborhood,Profile,Business, Post
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=current_user)
            form = ProfileForm(request.POST,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
        except:
            form = ProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
    else:
        if Profile.objects.filter(user=current_user):
            profile = Profile.objects.get(user=current_user)
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
    return render(request,'edit.html',{"form":form})

