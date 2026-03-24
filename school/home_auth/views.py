from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import CustomUser , PasswordResetRequest
from django.utils import timezone

# Create your views here.



def signup_view(request):

 if request.method == 'POST':
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     email = request.POST['email']
     password = request.POST['password']
     role = request.POST.get('role') 

# Créer l'utilisateur
     user = CustomUser.objects.create_user(
     username=email,
     email=email,
     first_name=first_name,
     last_name=last_name,
     password=password, 
  )
# Assigner le rôle
     role = request.POST.get('role' , '').lower() 
     if role == 'student':
        user.is_student = True
     elif role == 'teacher':
        user.is_teacher = True
     elif role == 'admin':
        user.is_admin = True
     else : 
        messages.error(request, "Please select a valid role.") 
        return render(request , 'authentication/register.html') 

     user.save()
     login(request, user)
     messages.success(request, 'Signup successful!')
     return redirect('index')
 return render(request, 'authentication/register.html')

def login_view(request):
 
 if request.method == 'POST':
      email = request.POST['email']
      password = request.POST['password']
      user = authenticate(request, username=email,
      password=password)

      if user is not None:
         login(request, user)
         messages.success(request, 'Login successful!')

# Redirection selon le rôle
         if user.is_admin:
            return redirect('admin_dashboard')
         elif user.is_teacher:
            return redirect('teacher_dashboard')
         elif user.is_student:
            return redirect('student_dashboard')
         else:
            messages.error(request, 'Invalid user role')
            return redirect('index')
      else:
         messages.error(request, 'Invalid credentials')
         return render(request, 'authentication/login.html')
 return render(request, 'authentication/login.html')  

def logout_view(request):
 
 logout(request)
 messages.success(request, 'You have been logged out.')
 return redirect('index')

def forgot_password(request) : 
 
  if request.method == 'POST' : 
     email = request.POST.get('email')
     if email : 
        try : 
             user = CustomUser.objects.get(email=email)
             reset_request = PasswordResetRequest.objects.create(user=user , email=email)
             reset_request.send_reset_email()
             messages.success(request , 'Password reset link sent to your email.')
        except CustomUser.DoesNotExist : 
             messages.error(request , 'No user found with this email.')

     else :
       messages.error(request , 'Please enter your email.')
  return render(request, 'authentication/forgot-password.html') 

def reset_password(request , token = None):
  if not token : 
        messages.error(request , "Invalid password reset link.")    
        return redirect('login')
  
  reset_request = get_object_or_404(PasswordResetRequest , token = token)
  
  if not reset_request.is_valid():
         messages.error(request , "This passord reset link has expired.")
         return redirect('forgot-password')
  
  if request.method == 'POST' : 
         new_password = request.POST.get('new_password')
         confirm_password = request.POST.get('confirm_password')

         if not new_password or not confirm_password : 
              messages.error(request , "Please fill out all fields.")
         elif  new_password != confirm_password : 
              messages.error(request , "Passwords do not match.")
         else : 
            user = reset_request.user
            user.password = make_password(new_password)  
            user.save()

            reset_request.delete()

            messages.success(request , "Your password has been reset. You can now log in .")
            return redirect('login')
  return render(request , 'authentication/reset_password.html')           

                   