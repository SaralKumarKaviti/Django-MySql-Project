from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *
import csv

# Create your views here.

def hello_index(request):
	return HttpResponse('Hello World!!')

def dashboard(request):
	return render(request,'tasks/dashboard.html')

def addTask(request):
	data = RegisterForm()
	if request.method=='POST':
		data=RegisterForm(request.POST,request.FILES)
		if data.is_valid():
			data.save()
		return redirect('/view')
	else:
		# context={'data':data}
		return render(request,'tasks/add.html',{'data':data})

def viewTask(request):
	data = Register.objects.all()
	context={'data':data}
	return render(request,'tasks/view.html',context)

def editTask(request,pk):
	query=Register.objects.get(id=pk)
	data=RegisterForm(instance=query)
	if request.method=='POST':
		data=RegisterForm(request.POST,request.FILES,instance=query)
		if data.is_valid():
			data.save()
		return redirect('/view')
	else:
		return render(request,'tasks/edit.html',{'query':query})

def deleteTask(request,pk):
	item=Register.objects.get(id=pk)
	if request.method=='POST':
		item.delete()
		return redirect('/view')
	else:
		context={'item':item}
		return render(request,'tasks/delete.html',context)

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="employee.csv"'
    employees=Register.objects.all()
    write=csv.writer(response)
    for employee in employees:
        write.writerow([employee.firstName,employee.lastName,employee.email,employee.phoneNumber,employee.createdOn])
    return response

# def index(request):
# 	tasks=Task.objects.all()
# 	form = TaskForm()

# 	if request.method=='POST':
# 		form=TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/')

# 	context={'tasks':tasks, 'form':form}
# 	return render(request,'tasks/list.html',context)

# def updateTask(request,pk):
# 	task=Task.objects.get(id=pk)
# 	form = TaskForm(instance=task)
# 	if request.method=='POST':
# 		form = TaskForm(request.POST,instance=task)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context ={'form':form}
# 	return render(request,'tasks/update.html',context)

# def deleteTask(request,pk):
# 	item=Task.objects.get(id=pk)
# 	if request.method=='POST':
# 		item.delete()
# 		return redirect('/')


# 	context={'item':item}
# 	return render(request,'tasks/delete.html',context)


