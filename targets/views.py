from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

@login_required
def show_all(request):
    return render_to_response('targets/show_all.html', {}, RequestContext(request))
