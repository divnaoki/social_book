from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile
# error message output module
from django.contrib import messages 
from django.http import HttpResponse
# Create your views here.
def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == "POST":
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    # パスワードが一致しているかチェック
    if password == password2:
      # Userモデルに同じメールアドレスがいるかチェック
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Taken')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username Token')
        return redirect('singup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # Log User in and redirect to settings page

        # create a Profile object for the new user
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('signup')
    else:
      messages.info(request, 'Password Not Matching')
      return redirect('signup')
  else:
    return render(request, 'signup.html')
    
