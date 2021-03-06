from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required


from upload.models import Upload
from upload.forms import UploadForm
# Create your views here.

def index(request):
    	user=request.user
    	if user.is_anonymous:
		a=0
	if request.user.is_active and request.user.is_authenticated:
		a=1

	return render_to_response(
        	'upload/index.html',
        	{'a':a},
        	context_instance=RequestContext(request)
        )
	   	
@login_required   	
def list_file(request):
    # file upload view
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = Upload(upload_file = request.FILES['upload_file'],username=request.user.username)
            newfile.save()

            # Redirect to the file list after POST
            return HttpResponseRedirect('')
    else:
        form = UploadForm() # A empty, unbound form

    # Load documents for the list page
    files = Upload.objects.all().filter(username = request.user.username)

    # Render list page with the documents and the form
    return render_to_response(
        'upload/list_file.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



