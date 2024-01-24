from django.shortcuts import render, redirect
from .models import Member, Message, Solution, Client, Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


# get messages from users

def contact(request):
    if request.method == "POST":
        Message.objects.create(
            fullname = request.POST['fullname'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            message = request.POST['message']
        )
        return redirect('index')
    return render(request, "contact.html")


def service(request):
    solutions = Solution.objects.all()
    clients = Client.objects.all()
    context = {
        'solutions': solutions,
        'clients': clients,
    }
    
    return render(request, 'service.html', context)


def blog(request):
    members = Member.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'blog.html', context)


def about(request):
    return render(request, 'about.html')
