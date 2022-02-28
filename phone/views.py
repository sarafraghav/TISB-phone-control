from django.shortcuts import render
from django.http import HttpResponse
from .forms import handler
from django.contrib import messages
from .models import signin
from datetime import datetime



# Create your views here.
def home(request):
    if request.method == 'POST':
        form = handler(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
          print(form.cleaned_data['cid'])
          signedin = signin.objects.filter(cid= form.cleaned_data['cid'],signedin=True)
          if(signedin):
              y = signedin[0]
              y.signedin = False
              y.signout = datetime.now()
              y.save()
              messages.success(request, "User Succesfully Logged Out")
          else:
            x = form.save(commit=False)
            x.signedin = True
            x.save()
            messages.success(request, "User Succesfully Logged In")
          
            
    else:
        form = handler()

    return render(request, 'index.html', {'form': form})