from django.urls import path, re_path
from . import views
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),#name using variable method(fstrind)
    path('third/', views.third, name='third'),
    path('secondoffirst/', views.secondoffirst, name='secondoffirst'),#concatination
    path('dishes/', views.menuitems, name='menuitems'),
    #defining dynamic url string as per the parameter passed inside the function.
    path('greet/<str:name>/', views.greet, name='greet'),
    #writing the url for restaurent app finding the description of a particular item
    path('dishes1/<str:dish>/', views.menuitems1, name = 'meuitems1'),
    #Implemented logic if the item doesn't exist it shows not found instead of error
    path('dishes2/<str:dish1>/', views.menuitems2, name= 'menuitems2'),
    #writing url for Dynamic url queries
    #http://localhost:8000:/recipe?food=panner...
    path('recipe/', views.recipe, name='recipe'),
    #adding two numbers using url (http://localhost:8000/addition?value1=10&value2=20) like this we have to write in the url
    path('addition/', views.addition, name= 'addition'),
    #Calculator Problem Solution:
    path('calculator/', views.calculator, name= 'calculator'),
    #Practicing of Calculator
    path('calculate/', views.calculate, name='calculate'),
    #greeting1 using Dynamic query URL
    path('greet1/', views.greet1, name='greet1'),
    #Regular Expression:
    #1. it is for strings
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$', views.user_profile, name='user_profile'),
    #2. it is for numbers
    re_path(r'^items/(?P<item_id>[0-9]+)/$', views. item_details, name='item_details'),
    #3. Alpha Numeric
    re_path(r'^stdntdetails/(?P<reg_nam>[\w-]+)/$', views.RegNname, name='RegNname'),
    #4. writing two regex in single url means categories and subcategories
    re_path(r'^restaruant/(?P<category>[\w-]+)/(?P<subcategory>[\w-])/?$', views.restro_details, name= 'restro_details'),
    #4.1 modified with conditions of above regex
    re_path(r'^rest/(?P<category>[\w-]+)/(?P<subcategory>[\w-]*)/?$', views.restro_details1, name='restro_details'),
    #Django templates
    path('firsthtml/', views.firsthtml, name='firsthtml'),
    path('secondhtmlfetch/', views.secondhtmlfetch, name='secondhtmlfetch'),
    #Tables using django template Logic
    path('table/', views.table, name='table'),
    #question on line number 207>>
    path('restro/<str:food_name>/', views.restro, name='restro'),
    #creating page rounting functions home about food and food2
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('food/', views.food, name='food'),
    re_path(r'^food/(?P<itemname>[a-zA-Z]+)/$', views.food2, name='food2'),
    #Practicing of routing
    path('Illu/', views.Illu, name='Illu'),
    path('vivaram/', views.vivaram, name='vivaram'),
    path('padardam/', views.padardam, name='padardam'),  # Define the URL pattern for padardam
    re_path(r'^padardam2/(?P<padardam_name>)[a-zA-Z]+/$', views.padardam2, name='padardam2'),
    #starting with CSRF tokens line num 275
    path('simpleform/', views.simpleform, name='simpleform'),
    path('sampleform/', views.sampleform, name='sampleform'),
    path('siimpleform/', views.siimpleform, name='siimpleform'),
    path('validation/', views.validation, name='validation'),
    #creating the classes in forms.py line num 358
    path('val_django_form/', views.val_django_form, name = 'val_django_form'),
    #creating a signupform with database line num 374
    path('signup_view/', views.signup_view, name='signup_view'),
    path('signup_success_view/', views.signup_success_view, name='signup_success_view'),
    #Blogpost line 393
    path('blogpost/', views.blogpost, name='blogpost'),
    #Checking for css line num 404
    path('tempform/', views.tempform, name='tempform'),
    #Cookies line 420
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('set-cookie/<str:value>', views.set_cookie, name='set_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
    #Setting up with sessions
    path('set-session/<str:username>/<str:email>/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('delete-session/', views.delete_session, name='delete_session'),
]