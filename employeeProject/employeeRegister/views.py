from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employeeRegister/employee_list.html', context)


def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        context = {'form': form}
        return redirect(request, 'employeeRegister/employee_form.html', context)
    
    else:
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()

        return redirect('list')


def employee_delete(request):
    return

