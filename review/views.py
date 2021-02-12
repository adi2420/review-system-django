from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import ReviewForm,ExpertProfileForm
from .models import Review,ExpertProfile,GenerateCode
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
import random 

def home(request):
    #reviews=Review.objects.filter(author=request.user,expire__isnull=True)
    reviews=Review.objects.all().order_by('?')[:6]
    profiles=ExpertProfile.objects.all().order_by('?')[:3]
    # user=User()
    return render(request, 'review/home/index.html',{'reviews':reviews,'profiles':profiles})



    
def signupuser(request):
    
    if request.method=='GET':
        return render(request, 'review/signup/signupuser.html')
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                profile=ExpertProfile()
                profile.name=request.POST['name']
                profile.number=request.POST['number']
                profile.category=request.POST['category']
                profile.photo=request.POST['photo']
                profile.email=request.POST['email']
                profile.facebook=request.POST['facebook']
                profile.description=request.POST['description']
                profile.user=request.user

                
                profile.save()
                return redirect('userpanel')
            except IntegrityError:
                return render(request, 'review/signup/signupuser.html', {'error':'That username has already been taken. Please choose a new one.'})
        else:
            return render(request, 'review/signup/signupuser.html', {'error':'Passwords did not match'})
            #Tell the users that password did not match

    
@login_required
def userpanel(request):
    profile=get_object_or_404(ExpertProfile,user=request.user)
    return render(request, 'review/userpanel/dashboard.html',{'profile':profile})

@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method=='GET':
        return render(request, 'review/login/login.html')
    else:
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'review/login/login.html', {'error':'Username or Password is invalid.'})
        else:
            login(request, user)
            return redirect('userpanel')


@login_required
def createreview(request):
    if request.method=='GET':
        return render(request,'review/createreview/index.html')
    else:
        try:
            data=Review()
            profile=get_object_or_404(ExpertProfile,user=request.user)

            if profile.Credits<=0:
                return render(request,'review/createreview/index.html',{'error':'You do not have enough credits to post a review. Kindly recharge.'})
            else:
                data.title=request.POST['title']
                data.description=request.POST['review']
                data.photo=request.POST['photo']
                data.author=request.user
                data.save()
                profile.Credits-=1
                profile.save()
                return redirect('userpanel')




            

            


            
        except ValueError:
            return render(request,'review/createreview/index.html',{'error':'Title too long'})


def review(request,review_pk):
    review=get_object_or_404(Review,pk=review_pk)
    posts=Review.objects.order_by('-date')[:6]
    return render(request, "review/view/review.html",{'review':review,'posts':posts})

@login_required
def expertreviews(request):
    
    profile=get_object_or_404(ExpertProfile,user=request.user)
    reviews=Review.objects.filter(author=request.user)
    return render(request,"review/userpanel/reviews.html",{'profile':profile,'reviews':reviews})

@login_required
def updateprofilephoto(request):
    if request.method=='POST':
        profile=ExpertProfile()
        profile.photo=request.POST['newphoto']
        # profile.user=request.user
        profile.save(['photo'])
        return redirect('userpanel')


def allexperts(request):
    reviews=Review.objects.all().order_by('?')
    profiles=ExpertProfile.objects.all().order_by('?')
    return render(request, 'review/all/experts.html',{'reviews':reviews,'profiles':profiles})
    

def allreviews(request):
    reviews=Review.objects.all().order_by('?')
    profiles=ExpertProfile.objects.all().order_by('?')
    return render(request, 'review/all/reviews.html',{'reviews':reviews,'profiles':profiles})
    
def profile(request, profile_pk):
    profile=get_object_or_404(ExpertProfile,pk=profile_pk)
    return render(request, "review/view/profile.html",{'profile':profile})

@login_required
def generatecode(request):
    profile=get_object_or_404(ExpertProfile,user=request.user)
    if request.method=='POST':
        characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789')
        thepassword = ''
        for x in range(15):
            thepassword += random.choice(characters)

        credit=GenerateCode()
        credit.code=thepassword
        credit.value=request.POST['credit']
        credit.save()
        
        return render(request,'review/userpanel/dashboard.html',{'profile':profile,'code':thepassword})
    else:
        return render(request,'review/userpanel/dashboard.html',{'profile':profile,'code':'Generate Code'})
        

def redeemcode(request):
    profile=get_object_or_404(ExpertProfile,user=request.user)
    
    if request.method=='POST':
        credits=get_object_or_404(GenerateCode,code=request.POST['code'])
        if credits:
            profile.Credits += credits.value
            profile.save()
            credits.delete()
            return redirect('userpanel')
