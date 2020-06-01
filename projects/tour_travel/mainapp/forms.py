from django import forms

from datetime import date, timedelta


class PlanForm(forms.Form):
    check_in_date = forms.DateTimeField()
    check_out_date = forms.DateTimeField()
    adults = forms.IntegerField(min_value=0)
    children = forms.IntegerField(min_value=0, required=False)
    location = forms.CharField(max_length=100, required= False)
    
    adults.widget.attrs.update({"class":"form-control"})
    children.widget.attrs.update({"class":"form-control"})
    location.widget.attrs.update({"class":"form-control"})

    # Date Calculation
    inDate = date.today()
    outDate = inDate+ timedelta(days=30)
    # For setting min, max date, we need yyyy-mm-dd format
    min_date = inDate.strftime("%Y-%m-%d")
    max_date = outDate.strftime("%Y-%m-%d")
    # For Display as a Plceholder. We need dd-mm-yyyy format
    in_date = inDate.strftime("%d-%m-%Y")
    out_date = outDate.strftime("%d-%m-%Y")
    
    check_in_date.widget.attrs.update({"class":"form-control","min":min_date,"placeholder":in_date,"onfocus":"(this.type='date')",})
    check_out_date.widget.attrs.update({"class":"form-control","max":max_date,"placeholder":out_date,"onfocus":"(this.type='date')",})

