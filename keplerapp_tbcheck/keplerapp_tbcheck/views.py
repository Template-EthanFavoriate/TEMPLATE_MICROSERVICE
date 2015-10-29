from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context

'''
 _    _  _____  _      _____  _____ ___  ___ _____ 
| |  | ||  ___|| |    /  __ \|  _  ||  \/  ||  ___|
| |  | || |__  | |    | /  \/| | | || .  . || |__  
| |/\| ||  __| | |    | |    | | | || |\/| ||  __| 
\  /\  /| |___ | |____| \__/\\ \_/ /| |  | || |___ 
 \/  \/ \____/ \_____/ \____/ \___/ \_|  |_/\____/ 
                                                   
VERSION:  Code Initial Release    2015-10-27 
VIEW KEPLERAPP_TBCHECK

check table. a example app
''' 

from keplerapp_tbmodel.models import Employee

def service_check(request):
    emp = Employee()
    emp.truncate()
    emp.prepare_data()
    
    sec_orglist = map(lambda x:x.EmpName,emp.get_Name_by_OrgID(2))
    
    context={}
    context['sec_orglist']=sec_orglist
    context['dictionary_key_A']='value of dictionary key A: 10230'
    return render_to_response('keplerapp_tbcheck/intro_index.html', context)

def service_default(request):
    #return HttpResponse("defalt page 404")
    return render_to_response('keplerapp_tbcheck/intro_index.html', {})