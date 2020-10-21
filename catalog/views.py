from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils import timezone
from .models import Post
#from django.shortcuts import render, get_object_or_404

def news(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'catalog/news.html', {'posts': posts})

def administration(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/administration.html')      

def Future(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/Future.html')

def fees(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/fees.html')

def facilities(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/facilities.html')

def Gallaries(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/Gallaries.html')

def holiday(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/holiday.html')

def honors(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/honors.html')

def home(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/home.html')

def Rules(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/Rules.html')

def school(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/school.html')

def contact(request):
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'catalog/contact.html')

	
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['mnagulama@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "catalog/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')