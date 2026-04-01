
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Departement

def departement_list(request):
    depts = Departement.objects.all()
    return render(request, 'departement/departments.html', {'depts': depts})


def add_departement(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept_id = request.POST.get('department_id')
        head = request.POST.get('head_of_department')
        started_year = request.POST.get('started_year') 

        Departement.objects.create(
            name=name, 
            department_id=dept_id, 
            head_of_department=head
        )
        messages.success(request, 'Department added successfully')
        return redirect('departement_list')
    return render(request, 'departement/add_departement.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import Departement

def edit_department(request, pk):
    departement = get_object_or_404(Departement, pk=pk)

    if request.method == "POST":
        departement.name = request.POST.get("name")
        departement.department_id = request.POST.get("department_id")
        departement.head_of_department = request.POST.get("head_of_department")
        departement.save()
        return redirect('departement_list')

    return render(request, 'departement/edit_department.html', {
        'departement': departement
    })

def delete_departement(request, pk):
    dept = get_object_or_404(Departement, pk=pk)
    dept.delete()
    messages.success(request, 'Department deleted successfully')
    return redirect('departement_list')