from django.shortcuts import render, redirect
from app import models

# Create your views here.


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


def show(request):
    recipeList = models.recipeModel.objects.all()
    if request.GET.get("search"):
        recipeList = recipeList.filter(
            title__icontains=request.GET.get("search"))
    context = {"recipes": recipeList}
    return render(request, 'show.html', context)


def destroy(request, id):
    recipe = models.recipeModel.objects.get(id=id)
    recipe.delete()
    return redirect("/show")


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
