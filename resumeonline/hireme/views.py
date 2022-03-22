from django.shortcuts import render, redirect

# Create your views here.


def hireme(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        hireme = hireme(name=name, email=email, message=message)
        hireme.save()
        message.success(
            request, "Thank you for your message. I will get back to you soon.")
        return redirect('home')
