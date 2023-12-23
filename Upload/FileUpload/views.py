from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import EzForm, SignUpForm
from .models import Ez
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class Home(TemplateView):
    template_name='base.html'
    
def upload(request):
    if request.method=='POST':
        uploadedFile=request.FILES['document']
        fls=FileSystemStorage()
        print(uploadedFile.content_type)
        fls.save(uploadedFile.name, uploadedFile)

    return render(request, 'upload.html')

def ez_FileList(request):
    ez=Ez.objects.all()
    context={'ez':ez}
    return render(request, 'ez_fileList.html',context)

def ez_File_upload(request):
    if request.method=="POST":
        form=EzForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ezFile')
    else:
        form=EzForm()
    context={'form':form}
    return render(request, 'ez_file_upload.html',context)

def login_user(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('ezFile')
            
        else:
            messages.success(request,'Error Logging In. Try Again...')
            return redirect('login')
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,'Logged Out Successfully...')
    return redirect('login')

def signup(request):
    if (request.method=='POST'):
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,'Signed Up Successfully...')
            return redirect('ezFile')
    else:
        form=SignUpForm()
    return render(request, 'signup.html',{'form':form})