from django.shortcuts import render

import requests as req
import datetime

from .forms import MyValidationForm
# Create your views here.

url = "https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json"
response = req.get(url)
data = response.json()

def tranc_date(request, dt):


	dt = dt
	temp = datetime.datetime.strptime(dt, "%d-%m-%y").date()
	dt_f = temp.strftime("%d %b %y")

	tranc = []

	for i in data:
		if i['Date'] == dt_f:
			tranc.append(i)

	context = {
		"title" : "Transantions Details",
		"tranc" : tranc
	}
	return render(request, "index.html", context)


def balance(request, dt):

	dt = dt
	temp = datetime.datetime.strptime(dt, "%d-%m-%y").date()
	dt_f = temp.strftime("%d %b %y")

	t_balance_list = []
	t_balance = 0

	tmp = {}
	for i in data:
		if i['Date'] == dt_f:
			temp = {
				'account_no' : i['Account No'],
				'date' : i['Date'],
				'withdrawal_amt' : i['Withdrawal AMT'],
				'deposit_amt' : i['Deposit AMT'],
				'balance' : i['Balance AMT'],
			}

			t_balance_list.append(temp)


	context = {
		"title" : "balance",
		"t_balance_list" : t_balance_list,
	}

	return render(request, "balance.html", context)


def details_id(request, id):

	id_list = []

	for i in data:
		if i['Account No'] == id:
			id_list.append(i)


	return render(request, "id.html", context = { 'id_list' : id_list, 'title' : 'ID Details' })


def add_trans(request):
	if request.method == "POST":
		print(request.POST)
		form = MyValidationForm(request.POST, request.FILES)

		if not form.is_valid():
			return render(request, "add.html", {"error message" : "invalid details check again.."})
		else:
			tmp = {}

			tmp['Account No'] = form.cleaned_data['account_no']
			tmp['Date'] = form.cleaned_data['date'].strftime("%d %b %y")
			tmp['Transaction Details'] = form.cleaned_data['transaction_Details']
			tmp['Value Date'] = form.cleaned_data['value_date'].strftime("%d %b %y")
			tmp['Withdrawal AMT'] = form.cleaned_data['withdrawal_amt']
			tmp['Deposit AMT'] = form.cleaned_data['deposit_amt']
			tmp['Balance AMT'] = form.cleaned_data['balance_amt']

			print(tmp)
			data.append(tmp)

			return render(request, "add.html", {"method" : "get", "new_details" : tmp})

	else:
		form = MyValidationForm()
		return render(request, "add.html", {"form" : form, "method" : "post"})