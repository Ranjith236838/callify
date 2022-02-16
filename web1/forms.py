from django import forms


class MyValidationForm(forms.Form):
	account_no = forms.IntegerField()
	date = forms.DateField()
	transaction_Details = forms.CharField()
	value_date = forms.DateField()
	withdrawal_amt = forms.FloatField()
	deposit_amt = forms.FloatField()
	balance_amt = forms.FloatField()