from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from studentauth.models import Record
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, " Logged In!")
			return redirect('/')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('/')
	else:
		return render(request, 'home.html', {'records':records})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('/')

@csrf_exempt
def add_record(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = (request.POST['phone'])
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode =(request.POST['pincode'])
        new_record = Record(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, pincode=pincode, date=datetime.now())
        new_record.save()
        return HttpResponse('Record added Successfully')
	
    elif request.method == 'GET':
        return render(request, 'add_record.html')
    else:
        messages.alert(request, "An Exception Occurred! Student Has Not Been Added")

def student_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		student_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'student_record':student_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('/')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('/')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('/')
	
@csrf_exempt
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        if request.method == "POST":
            # Update the record
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            current_record.first_name = first_name
            current_record.last_name = last_name
            current_record.email = email
            current_record.phone = phone
            current_record.address = address
            current_record.city = city
            current_record.state = state
            current_record.pincode = pincode
            current_record.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('/')
        else:
            return render(request, 'update_record.html', {'current_record': current_record})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('/')


