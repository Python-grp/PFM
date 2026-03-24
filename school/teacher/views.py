from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Teacher

# Create your views here.

def teacher_list(request):
  teachers = Teacher.objects.all()
  return render(request, "teachers/teachers.html" , {'teacher_list' : teachers})

def add_teacher(request):
    if request.method == 'POST':
   
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        teacher_image = request.FILES.get('teacher_image')

        Teacher.objects.create(   
            first_name=first_name,
            last_name=last_name,
            teacher_id=teacher_id,
            gender=gender,
            date_of_birth=date_of_birth,
            joining_date=joining_date,
            mobile_number=mobile_number,
            teacher_image=teacher_image
        )  
  
        messages.success(request, 'Teacher added Successfully')
        return redirect('teacher_list')  
    else : 
       return render(request , 'teachers/add-teacher.html')
    
def edit_teacher(request , teacher_id) : 
  teacher = get_object_or_404(Teacher , pk=teacher_id)

  if request.method == 'POST':
   
    teacher.first_name = request.POST.get('first_name')
    teacher.last_name = request.POST.get('last_name')
    teacher.teacher_id = request.POST.get('teacher_id')
    teacher.gender = request.POST.get('gender')
    teacher.date_of_birth = request.POST.get('date_of_birth')
    teacher.joining_date = request.POST.get('joining_date')
    teacher.mobile_number = request.POST.get('mobile_number')

    if request.FILES.get('teacher_image') : 
         teacher.teacher_image = request.FILES.get('teacher_image') 

    teacher.save()

    messages.success(request , 'Teacher updated successfully')
    return redirect('teacher_list')  
  
  return render(request , 'teachers/edit-teacher.html' , {'teacher' : teacher})    

def view_teacher(request, teacher_id):
  teacher = get_object_or_404(Teacher ,pk=teacher_id )
  return render(request, 'teachers/teacher-details.html' , {'teacher' : teacher})

def delete_teacher(request, teacher_id):
  teacher = get_object_or_404(Teacher , pk=teacher_id)
  teacher.delete()
  messages.success(request , 'Teacher deleted successfully')
  return redirect('teacher_list') 
