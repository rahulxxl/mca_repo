from datetime import date, timedelta

from django import forms

from . import models

class CustDateInput(forms.DateInput):
    input_type = "date"


class CreateJam(forms.Form):
    jam_title = forms.CharField(max_length=50)
    start_date = forms.DateField()
    end_date = forms.DateField()
    #team_size = forms.IntegerField(min_value=1, max_value=5)
    prize = forms.IntegerField(min_value=1)

    jam_title.widget.attrs.update({"class":"form-control"})
    #team_size.widget.attrs.update({"class":"form-control"})
    prize.widget.attrs.update({"class":"form-control"})
    
    # Date Calculation
    startDay = date.today()
    endDay = startDay+ timedelta(days=14)
    # For setting min, max date, we need yyyy-mm-dd format
    min_date = startDay.strftime("%Y-%m-%d")
    max_date = endDay.strftime("%Y-%m-%d")
    # For Display as a Plceholder. We need dd-mm-yyyy format
    st_date = startDay.strftime("%d-%m-%Y")
    ed_date = endDay.strftime("%d-%m-%Y")
    
    start_date.widget.attrs.update({"class":"form-control","min":min_date,"placeholder":st_date,"onfocus":"(this.type='date')",})
    end_date.widget.attrs.update({"class":"form-control","max":max_date,"placeholder":ed_date,"onfocus":"(this.type='date')",})



class ApplyJam(forms.Form):
    pass


class LoginFormDeveloper(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    username.widget.attrs.update({"class":"form-control", "placeholder":"username"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})


class LoginFormStudio(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    username.widget.attrs.update({"class":"form-control", "placeholder":"studio username"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})


class RegisterDeveloper(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    name.widget.attrs.update({"class":"form-control", "placeholder":"full name"})
    username.widget.attrs.update({"class":"form-control", "placeholder":"username"})
    email.widget.attrs.update({"class":"form-control", "placeholder":"email"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})
    password_confirm.widget.attrs.update({"class":"form-control", "placeholder":"confirm password"})


class RegisterStudio(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    name.widget.attrs.update({"class":"form-control", "placeholder":"full name of studio"})
    username.widget.attrs.update({"class":"form-control", "placeholder":"studio username"})
    email.widget.attrs.update({"class":"form-control", "placeholder":"email"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})
    password_confirm.widget.attrs.update({"class":"form-control", "placeholder":"confirm password"})

