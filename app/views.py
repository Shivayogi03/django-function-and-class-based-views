from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View
from django.views.generic import TemplateView,FormView
# Create your views here.


def insert_by_fbv(request):
    ESMFO=SchoolMF()
    d={'ESMFO':ESMFO}

    if request.method=='POST':
        SMFO=SchoolMF(request.POST)
        if SMFO.is_valid():
            SMFO.save()
            return HttpResponse('data inserted...')
        
        else:
            return HttpResponse('invalid')
    return render(request,'insert_by_fbv.html',d)



class insert_by_cbv(View):
    def get(self,request):
         ESMFO=SchoolMF()
         d={'ESMFO':ESMFO}
         return render(request,'insert_by_cbv.html',d)
    
    def post(self,request):
         SMFO=SchoolMF(request.POST)
         if SMFO.is_valid():
            SMFO.save()
            return HttpResponse('data inserted...')
        
         else:
            return HttpResponse('invalid')



class RenderHTMLbyTV(TemplateView):
    template_name='RenderHTMLbyTV.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['NAME']='ROHITH'
        ECDO['AGE']=23
        return ECDO
    

class insert_by_TV(TemplateView):
    template_name='insert_by_TV.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['ESMFO']=SchoolMF
        return ECDO
    
    def post(self,request):
        SMFO=SchoolMF(request.POST)
        if SMFO.is_valid():
            SMFO.save()
            return HttpResponse('DATA INSERTED...')
        
        else:
            return HttpResponse('INVALID')
            

class Insertbyfv(FormView):
    template_name='Insertbyfv.html'
    form_class=SchoolMF

    def form_valid(self, form):
        form.save()
        return HttpResponse('Inserted')
    