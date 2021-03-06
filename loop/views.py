from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Neighborhood,Profile,Business, Post
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, BusinessForm, PostForm

# Create your views here.
def index(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except:
        return redirect('edit_profile',username = current_user.username)

    try:
        posts = Post.objects.filter(neighborhood = profile.neighborhood)
    except:
        posts = None

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.neighborhood = profile.neighborhood
            post.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request,'index.html',{"posts":posts,"profile":profile,"form":form})  

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

@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user = request.user
    neighborhood = Profile.objects.get(user = current_user).neighborhood
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.neighborhood = neighborhood
            business.save()
        return redirect('businesses')
    else:
        form = BusinessForm()

    try:
        businesses = Business.objects.filter(neighborhood = neighborhood)
    except:
        businesses = None

    return render(request,'businesses.html',{"businesses":businesses,"form":form})

@login_required(login_url='/accounts/login/')
def search(request):
    current_user = request.user
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        businesses = Business.objects.filter(name__icontains=search_term)
        return render(request,'search.html',{'businesses':businesses})
    else:
        message = "You haven't searched for any business"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def post(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post.html',{"post":post})
