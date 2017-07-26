from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app import models
from django.core.urlresolvers import reverse_lazy
# from django.http import HttpResponse

# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['inject_me']='BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    # template_name= 'basic_app/school_list.html'  #django will autmotically assume the name of template to be the Model plus _list!!!!  django will always use school_list.html if it exists, regardless of this property value!!!!
    #ListView automatically returns a list with the Model name lower-cased (school) plus _list unless context_object_name is created

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    # template_name = 'basic_app/school_detail.html' #django will autmotically assume the name of template to be the Model plus _list!!!!
    #ListView automatically returns a list with the Model name lower-cased (school) unless context_object_name is created

class SchoolCreateView(CreateView): #allows you to quickly create a new school "view"
    fields=('name','principal','location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('basic_app:list')



# def index(request):
#     return render(request, 'index.html',{})




# class CBView(View):
#     def get(self,request):
#         return HttpResponse('Class Based Views are Kool!')
