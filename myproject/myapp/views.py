from django.shortcuts import render
from django.http import HttpResponse
#httpresponse is (HttpResponse is a class provided by Django that represents an HTTP response.)
#render is a function provided by Django in the django.shortcuts module.
#render is typically used to render html templates with data

# Create your views here.
#every coders first code 
def hello(request):
    return HttpResponse("Hello Vishnu! 😂😂")

def first(request):
    return HttpResponse("This is your first function");

#second way to display my name 
def second(request):
    name = 'vishnu'
    return HttpResponse (f"My name is {name}");

#concatination using + sign
def secondoffirst(request):
    object = 'cake'
    return HttpResponse("Taste the "  + object);
        
#Including html tags in my function 
def third(request):
    return HttpResponse("<h1 style='color : red'>Hello, World this is Vishnu :) 😂");

#Creating a Dictionary 
def menuitems(request):
    items = {
        'Pizza' : 'Pizza Cost Rs. 100',
        'Coconut' : 'Coconut Cost Rs. 25',
        'Mango' : 'Mango Cost Rs. 30'
    }
    content = '<h1> Menu Items </h1>'
    for item, description in items.items():
        content+=f'<li> {item} : {description} </li>'
    return HttpResponse(content)

#Creating Dynamic URL as up to above it is a static means where user input 
#http://localhost:8000/products (static Url)
#http://localhost:8000/products/123 (Dynamic Url)
#http://localhost:8000/porducts?q=query (Dynamic URl)
#we should pass number of parameters required to ask in the url in function only
def greet(request, name):
    return HttpResponse(f"Hello, {name}! :) welcome to django practice session")


#Dynamic Url's using Parameter
#Creating a dictonary with the help of dynamic url format, passing the parametet dist to get the item information accordingly
def menuitems1(request, dish):
    items = {
        'Pizza' : 'Pizza Cost rs 40',
        'Mango' : 'Mango Cost rs 50',
        'Burger' : 'Burger Cost rs 70',
        'Coconut' : 'Coconut Cost rs 30'
    }
    description = items[dish]
    return HttpResponse(description);

#what if the item was not found (simple use if else logic if the item is there in the dictionary print the description else print not found)

def menuitems2(request, dish1):
    items = {
        'Pizza' : 'Pizza Cost rs 30',
        'Pasta' : 'Pasta Cost rs 40',
        'Maggie' : 'Maggie Cost rs 10',
        'Burger' : 'Buurger Cost rs 45',
        'Frech Fries' : 'Frenchies Cost rs 50'
    }
    if dish1 in items:
        description = items[dish1]
        return HttpResponse(description);
    else:
        return HttpResponse(f"{dish1} Not Found")   
    
#Dynamic URL's using Query
#checking for food item availabe or not
def greet1(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    occupation = request.GET.get('occ')
    return HttpResponse(f"He is {name}. and he is around {age}, he is a {occupation}")
    
def recipe(request):
    food = request.GET.get('food')
    return HttpResponse(f"Recipe is availabe for {food}");
#Addition of two number from the url
def addition(request):
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')
    # result = value1 + value2 don't write like this it will think it as string and it will concatinate
    result = int (value1) + int (value2)
    return HttpResponse(f"Result of two numbers addition is {result}");

#Calculator using Dynamic url query
def calculator(request):
    operation = request.GET.get('op')
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')
   
    try:
        value1 = int(value1)
        value2 = int(value2)
    except ValueError:
        return HttpResponse('Invalid Numbers')
    
    if operation == 'sum':
        result = value1+value2
        return HttpResponse(f"the sum of two numbers is {result}")
    elif operation == 'sub':
        result = value1 - value2
        return HttpResponse(f"The subtraction of two Numbers is {result}")
    elif operation == 'product':
        result = value1*value2
        return HttpResponse(f"The product of two numbers is {result}")
    elif operation == 'Division':
        result = value1 / value2
        return HttpResponse(f"The division of two numbers is {result}")
    else:
        return HttpResponse("Invalid Number");

#Practicing of Calculator Function
def calculate(request):
    operation = request.GET.get('op')
    val1 = request.GET.get('val1')
    val2 = request.GET.get('val2')
    
    try:
        val1 = int(val1)
        val2 = float(val2)
    except ValueError:
        return HttpResponse("Invalid Entry")
    
    if operation == 'sum':
        result = val1 + val2
        # return HttpResponse(result)
    elif operation == 'sub':
        result = val1 - val2
        # return HttpResponse(result)
    elif operation == 'product':
        result = val1 *  val2
        # return HttpResponse(result)
    elif operation == 'division':
        result = val1/val2
        # return HttpResponse(result)
    else:
        return HttpResponse("Invalid Response")
    return HttpResponse(f"Result of {operation} operation is: {result}")

#Regular Expressions: 
def user_profile(request, username):
    return HttpResponse(f"user_Profile: {username}")

#Regex with Numbers
def item_details(request, item_id):
    return HttpResponse(f"item id is: {item_id}")

#Regex with alpha numeric values
def RegNname(request, reg_nam):
    return HttpResponse(f"Student Details is: {reg_nam}")

#Writing Regex for categories and sub categorie
def restro_details(request, category, subcategory):
    return HttpResponse(f"category is {category} and subcategory is {subcategory}")

#same as above with condition that if subcategory or category not provided it will return not provided instead of Error page

from django.http import HttpResponse
#here we also used the error handling method 
def restro_details1(request, category, subcategory):
    if(subcategory==""):
        return HttpResponse(f"Category is {category} and Subcategory <span style='color:red'> Not Provided</span>", status=404)
    return HttpResponse(f"Category is {category} and Subcategory is {subcategory}")

#Django Templates
#basic html 
def firsthtml(request):
    return render(request, 'first.html')

#creating Table using Django templates creating the  data here and fetching in html file
def secondhtmlfetch(request):
    data = {"content" : "Django is a framwork"}
    return render(request, 'second.html', data)

#Tables using Html
def table(request):
    items = {'menu' : [
        {'name' : 'punugulu', 'Cost' : '50rs'},
        {'name' : 'Bonda', 'Cost' : '30rs'},
        {'name' : 'Dosa', 'Cost' : '40rs'},
        {'name' : 'Utthapam', 'Cost' : '50rs'},
        {'name' : 'Idly', 'Cost' : '50rs'}
    ]}
    return render(request, 'menu1.html', items)

#declaring a global varible where we can use many times
items =[
	{'name':'pizza', 'Cost': 500},
	{'name':'fries', 'Cost':'free'},
	{'name':'momos', 'Cost':80},
	{'name':'Chutney', 'Cost':'Free'},
	{'name':'pasta', 'Cost':70}
]

#create an appopriate url that accepts a parameter such that when the user specifies the name of the food item as the parameter, the details of that food item should be rendered on a template named restroo.html

def restro(request, food_name):
    for item in items:
        if item['name'] == food_name:
            context = {'item' : item}
            return render(request, 'restroo.html', context)
    return render(request, 'restroo.html', {'item' : None})# Return a default context if item is not found

#Page Routing using Django templates
#creating a page with navbar 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

list_items = [
    {'name':'Bonda', 'cost':'40', 'Detils':'South Indian most Liked Tiffins'},
    {'name': 'Dosa', 'cost': '50', 'Details': 'vere untadi'},
    {'name': 'Idalyy', 'cost': '50', 'Details': 'with sambar swargam without sambar hevan...'},
    {'name': 'paysam', 'cost': 'Free', 'Details': 'idi tgaithe mootham kadupu nindi pothadi andi...........'}
]

def food(request):
    return render(request, 'food.html', {'items' : list_items})

def food2(request, itemname):
    singleItem = {}
    for food in list_items:
        if(food['name'] == itemname):
            singleItem = food
            break
    return render(request, 'food2.html', {'data' : singleItem})

#Practicing Routing again
def Illu(request):
    return render(request, 'illu.html')

def vivaram(request):
    return render(request, 'vivaram.html')

vastuvulu_anni = [
    {'Peru' : 'Perugu', 'Viluva' : '10rs', 'Vivaram' : 'tinte inka nidravastundi'},
    {'Peru' : 'Palu', 'Viluva' : '20rs', 'Vivaram' : 'tagite balam tagakapothe sunayam'},
    {'Peru' : 'Pandlu', 'Viluva' : '50rs', 'Vivaram': 'Tindam manchidi tinakapothe tagandi'},
    {'Peru' : 'Palmoil', 'Viluva' : '120rs', 'Vivaram' : 'Appalai matarame vadali idi'}
]

def padardam(request):
    return render(request, 'tindi.html', {'items' : vastuvulu_anni})

# def padardam2(request, padardam_name):
#     SingleItem = {}
#     for item in vastuvulu_anni:
#         if(item['name'] == padardam_name):
#             SingleItem = item
#             break
#     return render(request, 'tindi2.html', {'data' : SingleItem})

def padardam2(request, padardam_name):
    SingleItem = {}  # Initialize SingleItem to None
    for item in vastuvulu_anni:
        if item['Peru'] == padardam_name:
            SingleItem = item
            break
    return render(request, 'tindi2.html', {'data': SingleItem})

#Starting With Django forms and CSRF_TOKEN
from django.shortcuts import render
from django.middleware.csrf import get_token

def simpleform(request):
    if request.method == 'POST':
        # Process the form data
        # Example: Saving form data to the database
        form_data = request.POST.get('form_data')
        # Your form processing logic here
        return render(request, 'success.html', {'form_data': form_data})
    else:
        csrf_token = get_token(request)
        return render(request, 'simpleform.html', {'csrf_token': csrf_token})

def sampleform(request):
    if request.method == "POST":
        form_data = request.POST.get('form_data')
        form_data2 = request.POST.get('form_data2')
        return render(request, 'success.html', {'form_data' : form_data, 'form_data2' : form_data2})
    else: 
        csrf_token = get_token(request)
        return render(request, 'simpleform.html', {'csrf_token' : csrf_token})
    

from django.views.decorators.csrf import csrf_exempt 
@csrf_exempt
#FORMS
def siimpleform(request):
    if request.method == 'POST':
        textbox1 = request.POST.get('textbox1')
        textbox2 = request.POST.get('textbox2')
        return HttpResponse(f"The values are {textbox1} and {textbox2}")
    else:
        form_html = """
        <form method = "POST">
        <label for = "textbox1"> Text Box 1: </label><br>
        <input type = "text" id = "textbox1" name = "textbox1"><br>
        <label for = "textbox2"> Text Box 2: </label><br>
        <input type = "text" id = "textbox2" name = "textbox2"><br><br>
        <input type = "Submit" value = "Submit">
        </form>
        """
        return HttpResponse(form_html)

#form validation in django
from django.shortcuts import render
def validation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        name_error = ''
        email_error = ''
        password_error = ''
        
        if not name:
            name_error = "Name cannot be left balnk"
        if not email:
            email_error = "Email cannot be left blank"
        if not password:
             password_error = "Password cannot be left blank"
        if name_error or email_error or password_error:
            return render(request, 'validate.html', {
                'name' : name,
                'email' : email,
                'password' : password,
                'name_error' : name_error,
                'email_error' : email_error,
                'password_error' : password_error
            })
        else:
            return render(request, 'validate.html', {
                'submitted_Values':{
                    'name' : name,
                    'email' : email,
                    'pssword' : password,
                }
            })
    else:
        return render(request, 'validate.html')
    
#creating own classes in forms.py under application level
from .forms import InputForm1
from django.shortcuts import render

def val_django_form(request):
    submitted_details = None
    if request.method == 'POST':
        form = InputForm1(request.POST)
        if form.is_valid():
            submitted_details = form.cleaned_data
        else:
            return render (request, 'val_django_form.html', {'form':form, 'submitted_details' : submitted_details})
    else:
        form = InputForm1()
    return render(request, 'val_django_form.html', {'form' : form, 'submitted_details' : submitted_details})

#creating a signup form and connecting that to database
from django.shortcuts import render, redirect
from .forms import PracticeForm

def signup_view(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success_view')  # Corrected redirect URL name
    else:
        form = PracticeForm()
    return render(request, 'signup.html', {'form' : form})

from django.shortcuts import render

def signup_success_view(request):
    return render(request, 'signup_success.html')

#Creating a blog post from static Image file
#logic for the blogpost to fetch all the data form the database. 
from .models import Blogpost
def blogpost(request):
    post = Blogpost.objects.all()
    return render(request, 'blogpost.html', {'post' : post})

#Temperary form for checking css
#  import re
from django.shortcuts import render, HttpResponse

def tempform(request):
    if request.method == 'GET':
        return render(request, 'forming.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        email_pattern = r'^[\w]+@[\w]+\.[\w]{2,3}$'  # Corrected email pattern

        # Validating form inputs
        if name and password and email and len(name) > 3 and re.match(email_pattern, email):
            return HttpResponse('THANK YOU!')
        else:
            return HttpResponse('PLEASE FILL THE PROPER INFO')

# -----------------
# Cookies:
#GET_COOKIE
def get_cookie(request):
    cookie_value = request.COOKIES.get('name')
    if cookie_value:
        return HttpResponse(f"cookie Values: {cookie_value}")
    #return HttpResponse("cookie Value: "+cookie_value)
    else:
        return HttpResponse("Cookie Not Found!")

#set Cookie
def set_cookie(request, value):
    response = HttpResponse("Cookie set!")
    response.set_cookie('name', value, max_age=15)  # Set cookie with dynamic value and max_age of 15 seconds
    return response

#Delete Cookie
def delete_cookie(request):
    response =HttpResponse("Cookie deleted!")
    response.delete_cookie('name')
    return response
# ----------------------------------------------
# Sessions
def set_session(request, username, email):
    request.session['username'] = username
    request.session['email'] = email
    return render(request, 'set_session.html')

def get_session(request):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'Guest@gmail.com')
    return render(request, 'get_session.html', {'username':username, 'email':email})

def delete_session(request):
    request.session.flush()
    return render(request, 'delete_session.html')