from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_button_page(request):
    return render_to_response('login_button_page.html')

@login_required
def main_user_page(request):
    return render_to_response('main_user_page.html', context_instance=RequestContext(request))