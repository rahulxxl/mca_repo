from django import forms

class IssueBlood(forms.Form):
    pass
    # blood_group =forms.BooleanField()
    # num_units
    # person_type
    # name
    # address
    # phone
    # date
    # amount


class ViewDonor(forms.Form):
    pass

class NameForm(forms.Form):
    donor_name = forms.EmailField(label="Donor Name", max_length=50)
    
class TestForm(forms.Form):
    blood_group =forms.BooleanField(required=False)     # For Boolean input
    name = forms.CharField(max_length = 10, min_length=7)   # For string Input


class ViewControls(forms.Form):
    BLOOD_GROUPS = (
        ("A+","a-pos"),
        ("B+","b-pos"),
        ("O+","o-pos"),
    )
    
    username = forms.CharField(required = False)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    address = forms.CharField(widget=forms.Textarea, required = False)
    email = forms.EmailField(required = False)
    password = forms.CharField(widget=forms.PasswordInput, required = False)
    blood_group =forms.ChoiceField(choices=BLOOD_GROUPS,required = False)

    class_form = {"class":"form-control"}
    
    username.widget.attrs.update(class_form)
    first_name.widget.attrs.update(class_form)
    last_name.widget.attrs.update(class_form)
    address.widget.attrs.update(class_form)
    email.widget.attrs.update(class_form)
    password.widget.attrs.update(class_form)
    blood_group.widget.attrs.update(class_form)
