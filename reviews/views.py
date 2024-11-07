from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.

######### Defult way to make views without forms.py ######
# def review(request):
#     if request.method == 'POST':
#         entered_data=request.POST['username'] ### post is dictionary and username is name to form field we assigne so we can save mail in diffferent veriable and username in deifferent veriable
#         print(entered_data)
#         return HttpResponseRedirect("thank-you")

#     return render(request,"reviews/review.html")

########## Way to make validation using form.py extending from form class

# def review(request):
#     if request.method=='POST':

#         form = ReviewForm(request.POST) #assining veriable , not pointing like class base view & POST is collected data from user in dictionary
#         if form.is_valid(): ### is_valid is built_in function in form class 
#             review=Review(user_name=form.cleaned_data['user_name'],
#                           review_text=form.cleaned_data['review_text'],
#                           rating=form.cleaned_data['rating']) ## cleaned_data is also function in from class to print all data
#             review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form=ReviewForm()
#     return render(request, "reviews/review.html",{
#         "form":form,
#     })

########## Way to make validation using form.py extending from ModelForm class

def review(request):
     if request.method=='POST':
         ### existing_data=Review.objects.get(pk=1) to update data of database by user
         form = ReviewForm(request.POST) #form=ReviewForm(request.POST,instance=existing_model) ### save data but as not new data but update data
         if form.is_valid():
             form.save()
             return HttpResponseRedirect("/thank-you")
     else:
         form=ReviewForm()
     return render(request, "reviews/review.html",{
         "form":form,
    })


######### manual veladition on form to not be empty and longer then 100 character. ######

# def review(request):
#     if request.method == 'POST':
#         entered_data=request.POST['username'] ### post is dictionary and username is name to form field we assigne so we can save mail in diffferent veriable and username in deifferent veriable
#         print(entered_data)
#         return HttpResponseRedirect("thank-you")

#     return render(request,"reviews/review.html")


def thank_you(request):
    
    return render(request,"reviews/thank_you.html")