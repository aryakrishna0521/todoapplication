from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from task.models import Todo

from task.forms import SignInForm,SignUpForm,TodoForm
# Create your views here.


class SignUpView(View):
    template_name="register.html"
    form_class=SignUpForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{'form':form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
            print("account created")
            return redirect('signup')
        print("failed")
        return render(request,self.template_name,{'form':form_instance})
class signinView(View):
    template_name="login.html"
    form_class=SignInForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{'form':form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("session started")
                return redirect("index")
            print("invalid credentials")
        return render(request,self.template_name,{"form":form_instance})

class TodoListView(View):
    template_name="index.html"
    form_class=TodoForm
    def get(self,request,*args,**kwargs):
        qs=Todo.objects.filter(owner=request.user)
        form_instance=self.form_class()
        return render(request,self.template_name,{'form':form_instance,'data':qs})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.instance.owner=request.user
            form_instance.save()
            return redirect("index")
        return render(request,self.template_name,{'form':form_instance})

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todo.objects.get(id=id).delete()
        return redirect('index')

class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todo.objects.filter(id=id).update(status=True)
        return redirect('index')
