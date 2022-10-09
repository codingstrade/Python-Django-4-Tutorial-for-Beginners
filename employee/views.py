
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee, BlogPosts
from django.db.models import Q

# Create your views here.

def index(request):
    myEmployees = Employee.objects.all().order_by('-name')
    template = loader.get_template('employee/index.html')
    context = {
        'myEmployees': myEmployees
    }
    return HttpResponse(template.render(context, request))
    
def create(request):
      template = loader.get_template('employee/createPage.html')
      return HttpResponse(template.render({},request))

def createData(request):
    data1 = request.POST['name']
    data2 = request.POST['title']
    newEmployee = Employee(name=data1, title= data2)
    newEmployee.save()
    return HttpResponseRedirect(reverse('employee'))

def delete(request,id):
    deleteEmployee = Employee.objects.get(id=id)
    deleteEmployee.delete()
    return HttpResponseRedirect(reverse('employee'))

def update(request,id):
      updatemployee = Employee.objects.get(id=id)
      template = loader.get_template('employee/updatePage.html')
      context = {
        'Employee': updatemployee
      }
      return HttpResponse(template.render(context,request))

def updateData(request, id):
    name = request.POST['name']
    title = request.POST['title']
    updatemployee = Employee.objects.get(id=id)
    updatemployee.name = name
    updatemployee.title = title
    updatemployee.save()
    return HttpResponseRedirect(reverse('employee'))  

def blog(request):
    posts = BlogPosts.objects.all()
    featuredPost = BlogPosts.objects.filter(featured= True)
    template = loader.get_template('employee/blog.html')
    context = {
        'posts': posts,
        'featuredPost':featuredPost
    }
    return HttpResponse(template.render(context, request))

def detailsPage(request,id):
      detailsPost = BlogPosts.objects.get(id=id)
      template = loader.get_template('employee/detailsPage.html')
      context = {
        'posts': detailsPost
      }
      return HttpResponse(template.render(context,request))