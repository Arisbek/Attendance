from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,"home.html")

def contacts(request):
    return HttpResponse("Наши контакты!")

def about_us(request):
    return HttpResponse("Информация о нас!")

def coach_info(request, id):
    coach = Coach.objects.get(id=id)
    return render(request,"coach.html",{'coach':coach})

def coaches(request):
    coaches = Coach.objects.all()
    return render(request,"coaches.html",{'coaches':coaches})

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request,"product.html",{'product':product})

def products(request):
    products = Product.objects.all()
    return render(request,"products.html",{'products':products})

def utility(request, id):
    utility = Utility.objects.get(id=id)
    return render(request,"utility.html",{'utility':utility})

def utilities(request):
    utilities = Utility.objects.all()
    return render(request,"utilities.html",{'utilities':utilities})

def abonement(request, id):
    abonement = Abonement.objects.get(id=id)
    return render(request,"abonement.html",{'abonement':abonement})

def abonements(request):
    abonements = Abonement.objects.all()
    return render(request,"abonements.html",{'abonements':abonements})

# def shorts(request):
#     shorts = Short.objects.all()
#     return render(request,"shorts.html",{'shorts':shorts})

# def short_info(request,id):
#     short = Short.objects.get(id=id)
#     return render(request,"short.html",{'short':short})

# def Categories(request):
#     categories=Category.objects.all()
#     return render(request,"categories.html",{'categories':categories})

# def Category_info(request,id):
#     category=Category.objects.get(id=id)
#     return render(request,"category.html",{'category':category})

# def posts(request):
#     posts_list = Post.objects.all()
#     return render(request,"posts.html",{'posts':posts_list})

# def post_info(request,id):
#     post = Post.objects.get(id=id)
#     return render(request,"post.html", {'post':post})

# def savedposts(request):
#     posts=SavedPosts.objects.filter(saved_posts=request.user)
#     return render(request,"savedposts.html",{'posts':posts})

# def savedposts(request):
#     posts = SavedPosts.objects.filter(saved_posts=request.user)
#     return render(request, "savedposts.html", {'posts': posts})

# @login_required  # Decorate the view with login_required to ensure the user is logged in
# def savedposts(request):
#     posts = SavedPosts.objects.filter(user=request.user)
#     return render(request, "savedposts.html", {'posts': posts})


# def comment(request):
#     comment=Comment.objects.all()
#     return render(request,"comment.html",{'comment':comment})

def profile(request, id):
    user = User.objects.get(id=id)
    abonements = Abonement.objects.filter(creator=user)
    return render(request, 'profile.html', {'user':user, 'abonements':abonements})