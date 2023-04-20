from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from polls.models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import logout , authenticate, login

# Create your views here.

@login_required
def homePage(request):
    questionsList = Question.objects.all()
    context = {
        "questionsListHTML" : questionsList
    }
    return render(request, 'home.html', context)

@login_required
def questionDetails(request, questionId):
    try:
        question = get_object_or_404(Question, pk = questionId)
        choice = question.choice_set.all()
    except Question.DoesNotExist:
        raise Http404("This Question doesn't exist")

    context = {
        "questionIdHTML" : question,
        "choicesHTML" : choice,
    }
    return render(request, 'question_details.html', context)

def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login()
        return redirect('home')
    else:
        form = UserCreationForm
    
    return render(request, 'register.html',{'form':form})

def logoutPage(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "Post":
        form = AuthenticationForm(request,data=request.Post)
        if form.is_valid():
            username = form.cleaned_data.get(username)
            password = form.cleaned_data.get(password)

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None,'Incorrect credentials')


    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})    