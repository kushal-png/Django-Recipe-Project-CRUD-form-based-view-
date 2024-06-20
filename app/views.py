from django.shortcuts import render, redirect
from django.http import HttpResponse
from app import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# reate your views here.

@login_required(login_url="/login")
def recipe(request):
    if request.method == "POST":
        data = request.POST
        rtitle = data.get('ftitle')
        rdescription = data.get('fdescription')
        rimage = request.FILES.get('fimage')

        new_recipe = models.recipeModel(
            title=rtitle,
            description=rdescription,
            image=rimage
        )
        new_recipe.save()

        return redirect('/show/')

    return render(request, 'index.html')


@login_required(login_url="/login")
def show(request):
    recipeList = models.recipeModel.objects.all()
    if request.GET.get("search"):
        recipeList = recipeList.filter(
            title__icontains=request.GET.get("search"))
    context = {"recipes": recipeList}
    return render(request, 'show.html', context)


@login_required(login_url="/login")
def destroy(request, id):
    recipe = models.recipeModel.objects.get(id=id)
    recipe.delete()
    return redirect("/show")


@login_required(login_url="/login")
def update(request, id):
    recipe = models.recipeModel.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        rtitle = data.get('ftitle')
        rdescription = data.get('fdescription')
        rimage = request.FILES.get('fimage')

        recipe.title = rtitle
        recipe.description = rdescription
        if rimage:
            recipe.image = rimage

        recipe.save()
        return redirect("/show")

    context = {'recipes': recipe}
    return render(request, 'update.html', context)


def register_page(request):
    if request.method == "POST":
        data = request.POST
        rFirstName = data.get('firstName')
        rLastName = data.get('lastName')
        rUsername = data.get('username')
        rPassword = data.get('password')
        rPasswordConfirm = data.get('confirmPassword')

        checkUser = User.objects.filter(username=rUsername)
        if checkUser.exists():
            messages.info(request, "User already exists")
            return redirect("/register")

        if rPassword != rPasswordConfirm:
            messages.info(request, "Passwords do not match")
            return redirect("/register")

        user = User.objects.create(
            first_name=rFirstName,
            last_name=rLastName,
            username=rUsername,
        )

        user.set_password(rPassword)
        user.save()
        messages.info(request, "User Registered Successfully")
        return redirect("/login")
    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        data = request.POST
        rUsername = data.get('username')
        rPassword = data.get('password')

        # Check if the user exists
        checkUser = User.objects.filter(username=rUsername)
        if not checkUser.exists():
            messages.info(request, "Kindly register first")
            return redirect("/register")

        # Authenticate user
        checkUser = authenticate(
            request, username=rUsername, password=rPassword)
        if checkUser is None:
            messages.info(request, "Invalid password")
            return redirect("/login")
        else:
            # Log the user in
            login(request, checkUser)
            messages.success(request, "Successfully logged in")
            return redirect("/show")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/login")

def practice(request):
    print(request.user.is_authenticated)
    return HttpResponse(request.user.is_authenticated)