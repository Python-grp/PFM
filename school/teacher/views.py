from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Teacher
from django.contrib.auth.decorators import login_required
from home_auth.decorators import admin_required
from home_auth.models import CustomUser

# Create your views here.

@login_required
def teacher_list(request):
  teachers = Teacher.objects.all()
  return render(request, "teachers/teachers.html" , {'teacher_list' : teachers})

@admin_required
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
  
        if not CustomUser.objects.filter(username=teacher_id).exists():
            CustomUser.objects.create_user(
                username=teacher_id, 
                email=f"{teacher_id}@teacher.preskool.com", 
                password=teacher_id, 
                is_teacher=True, 
                first_name=first_name, 
                last_name=last_name
            )
        messages.success(request, 'Teacher added Successfully')
        return redirect('teacher_list')  
    else : 
       return render(request , 'teachers/add-teacher.html')
    
@admin_required
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

@login_required
def view_teacher(request, teacher_id):
  teacher = get_object_or_404(Teacher ,pk=teacher_id )
  return render(request, 'teachers/teacher-details.html' , {'teacher' : teacher})

@admin_required
def delete_teacher(request, teacher_id):
  teacher = get_object_or_404(Teacher , pk=teacher_id)
  teacher.delete()
  messages.success(request , 'Teacher deleted successfully')
  return redirect('teacher_list') 
