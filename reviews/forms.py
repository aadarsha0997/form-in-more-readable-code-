from django import forms
from .models import Review
####### form extend from form class ##############


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(required=True, label="Your Name",max_length=100,error_messages={
#         "required": "Your name must not be empty",
#         "max_length":"Please enter a shorter name!"
#     })
#     review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)


######## Form extended from modelform class #######
class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        #### field=['user_name','review_text' ]####  select which field of model to include in form one by one
        fields='__all__' ### all field of model should be include 
        #### exclude=['use_name'] #### which field of modle should be excluded in form
        labels={
            'user_name':'Your Name',
            'review_text':'Your Feedback',
            'rating':'Your rating',
        } #### if we didn't assinge label it use model fields as label by defult
        error_messages={
            'user_name':{
                'required':'must not be empty',
                'max_length':'name must be short',
            }
        }

