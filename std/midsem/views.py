from django.shortcuts import render,HttpResponse,Http404

from midsem.models import Student

##Shows tha home page with all enroll list
def index(request):
    
    li  = Student.objects.all()
    
    context = {'std_list': li}

    return render(request, 'midtemp\index.html', context)


##show the details of the enroll selected 
def detail(request, e_id):
    st = get_object_or_404(Student,enroll=e_id)
    return render(request, 'midtemp/detail.html', {'s_info': st})


##show the page to upload result csv files
def hod(request):

    

    
    
