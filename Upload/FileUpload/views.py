from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import EzForm
from .models import Ez

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