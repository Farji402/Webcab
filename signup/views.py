from django.shortcuts import render, redirect
from .forms import JantaForm
from home import templates



def signup_page(request):
    if request.session.has_key('outlook_id'):
        return render(request, 'home/home_page.html')
    else:
        my_response = "Please fill the all the details correctly!"
        if request.method == 'POST':
            form = JantaForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'home/home_page.html')
            else:
                form = JantaForm()
                return render(request, 'signup/signup_page_final.html', {'my_response': my_response, 'form': form})

        else:
            form = JantaForm()
            return render(request, 'signup/signup_page_final.html', {'form': form})
