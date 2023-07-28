from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Sum, Max, Min, Avg
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView, View

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#import stripe
# Create your views here.
@login_required(login_url='signin')
def home(request,category_id=None):
	categories = Category.objects.all().order_by('?')
	other_categories = ProductsCategory.objects.all().order_by('?')[1:5]
	
	products = Products.objects.all().order_by('?')

	total_products = Products.objects.all().aggregate(sum=Sum('ProductQuantity'))

	# form ya kusearch
	form = ProductSearchForm(request.POST or None)
	if request.method =="POST":
		products = Products.objects.filter(ProductName__icontains=form['ProductName'].value())

	category = None
	#To SET  PAGINATION IN STOCK LIST PAGE
	paginator = Paginator(products,50)
	page = request.GET.get('page')
	try:
	    products=paginator.page(page)
	except PageNotAnInteger:
	    products=paginator.page(1)
	except EmptyPage:
	    products=paginator.page(paginator.num_pages)

	if category_id:
	#add hii kwa ajili ya pagination ukiselect category
		products = Products.objects.all()

		category = get_object_or_404(Category,id=category_id)
		products= products.filter(category=category)

		#To SET  PAGINATION IN STOCK LIST PAGE
		paginator = Paginator(products,20)
		page = request.GET.get('page')
		try:
		    products=paginator.page(page)
		except PageNotAnInteger:
		    products=paginator.page(1)
		except EmptyPage:
		    products=paginator.page(paginator.num_pages)

	context = {
		"categories":categories,
		"category":category,
		
		"products":products,
		"other_categories":other_categories,
		"page":page,
		"total_products":total_products,
		"form":form,
		
	}

	return render(request, "MyApp/home.html",context)





@login_required(login_url='signin')
def search_product_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ProductName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    product = Products.objects.filter(search)
    mylist= []
    mylist += [x.ProductName for x in product]
    return JsonResponse(mylist, safe=False)



# @login_required(login_url='signin')
# def view_product(request,id):
# 	product = Products.objects.get(id=id)
# 	#some_products = Products.objects.all('-id')[1:5]
	
# 	context = {
# 		"product":product,
# 		#"some_products":some_products,
		
		
		
# 	}

# 	return render(request, "MyApp/view_product.html",context)

class view_product(DetailView):
    model = Products
    template_name = 'MyApp/view_product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        similar_products = Products.objects.all().order_by('?')[:4]
        categories = Category.objects.all()[0:12]
        
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'similar_products':similar_products,
                'categories':categories,
            })
        return context




#--------------------------T-SHIRT--------------------------------------------

def T_shirt(request):
	products = Products.objects.filter(product_category__CategoryName__contains="T-Shirt").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "T_SHIRT/T_shirt.html", context)



#--------------------------SHIRT--------------------------------------------

def Shirt(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Shirt").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "SHIRT/Shirt.html", context)



#--------------------------SKIRT--------------------------------------------

def Skirt(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Skirt").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "SKIRT/Skirt.html", context)




#--------------------------TROUSER--------------------------------------------

def Trouser(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Trouser").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "TROUSER/Trouser.html", context)




#--------------------------SHOES--------------------------------------------

def Shoes(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Shoes").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "SHOES/Shoes.html", context)



#--------------------------SMARTPHONES--------------------------------------------

def SmartPhones(request):
	products = Products.objects.filter(product_category__CategoryName__contains="SmartPhones").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "SMARTPHONES/SmartPhones.html", context)



#--------------------------DELL LAPTOPS--------------------------------------------

def Dell_Laptops(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Dell Laptops").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "DELL_LAPTOPS/Dell_Laptops.html", context)




#--------------------------HP LAPTOPS--------------------------------------------

def Hp_Laptops(request):
	products = Products.objects.filter(product_category__CategoryName__contains="HP Laptops").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "HP_LAPTOPS/Hp_Laptops.html", context)





#-------------------------LENOVO LAPTOP----------------------------------
def Lenovo_Laptops(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Lenovo Laptops").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "LENOVO_LAPTOPS/Lenovo_Laptops.html", context)


#--------------------------WEB--------------------------------------------

def Web(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Web").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "WEB/Web.html", context)



#--------------------------GRAPHICS--------------------------------------------

def Graphics(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Graphics").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "GRAPHICS/Graphics.html", context)




#--------------------------GOWN--------------------------------------------

def Gown(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Gown").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "GOWN/Gown.html", context)



#--------------------------ARDUINO PRODUCTS-----------------------
def Arduino_Products(request):
	products = Products.objects.filter(product_category__CategoryName__contains="Arduino Products").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "ArduinoProducts/Arduino_Products.html", context)






#--------------------------SCHOOL PRODUCTS--------------------------------------------

def School_Products(request):
	products = Products.objects.filter(product_category__CategoryName__contains="School Products").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "SCHOOLPRODUCTS/School_Products.html", context)

#--------------------------MORE----------------------------------------
def More(request):
	products = Products.objects.filter(product_category__CategoryName__contains="More").order_by('?')
	similar_products = Products.objects.all().order_by('?')[:6]
	context ={
		"products":products,
		"similar_products":similar_products,
	}
	return render(request, "MORE/More.html", context)







#----------------------ADD TO CART---------------------------------------------
def add_to_cart(request, pk):
	item = get_object_or_404(Products, pk=pk)
	# if item.quantity == 0:
	# 	messages.info(request, f"There is no any {item.ProductName} product(s) in a stock for now")
	# 	return redirect('product_details', id=id)
	# else:
	    
	order_item, created = OrderItem.objects.get_or_create(
	    item=item,
	    user=request.user,
	    ordered=False,
	    
    )
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
	    order = order_qs[0]
	    if order.items.filter(item_id=item.pk).exists():
	        order_item.quantity += 1
	        
	        order_item.save()
	        
	        messages.success(request, f"{item.ProductName}'s quantity was updated")
	        return redirect('view_product',pk=pk)
	    else:
	        order.items.add(order_item)

	        
	        order.save()
	        
	        messages.success(request, f"{item.ProductName} was added to your Order")
	        return redirect('view_product',pk=pk)

	else:
	    ordered_date = timezone.now()
	    order = Order.objects.create(
	        user=request.user, ordered=False, ordered_date=ordered_date)
	    order.items.add(order_item)
	    
	    
	    order.save()
	    
	    messages.success(request, f"{item.ProductName} was added to your Order")
	    return redirect('view_product',pk=pk)




#--------------------------REMOVE FROM CART--------------------------------------




def remove_from_cart(request, pk):

    item = get_object_or_404(Products, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item_id=item.pk).exists():
            order.items.remove(order_item)
            

            order.save()
            messages.success(request, f"{item.ProductName} was removed from your Order")
                
            return redirect('view_product',pk=pk)
        else:
            messages.info(request, f"{item.ProductName} was not in your Order")
            return redirect('view_product',pk=pk)
    else:
        messages.info(request, "You don't have an active order!")
        return redirect('view_product',pk=pk)





 #-----------------REMOVE SINGLE FROM THE CART---------------------------------
def remove_single_from_cart(request, pk):
	item = get_object_or_404(Products, pk=pk)
	order_item, created = OrderItem.objects.get_or_create(
	    item=item, user=request.user, ordered=False)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
	    order = order_qs[0]
	    if order.items.filter(item__id=item.pk).exists():
	        if order_item.quantity > 1:
	            order_item.quantity -= 1
	            order_item.save()
	        else:
	            order.items.remove(order_item)
	            order.save()
	        messages.success(request, f"{item.ProductName}'s quantity was updated")
	        return redirect('order_summary')
	    else:
	        messages.info(request, f"{item.ProductName} was not in your Order")
	        return redirect('order_summary')
	else:
	    messages.info(request, "You don't have an active Order!")
	    return redirect('order_summary')



#-----------------------------ORDER SUMMARY------------------------------

class order_summary(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'order':order
        }
        return render(self.request, 'MyApp/order_summary.html',context)





#----------------------ADD TO CART---------------------------------------------
def add_to_cart2(request, pk):
	item = get_object_or_404(Products, pk=pk)
	# if item.quantity == 0:
	# 	messages.info(request, f"There is no any {item.ProductName} product(s) in a stock for now")
	# 	return redirect('product_details', id=id)
	# else:
	    
	order_item, created = OrderItem.objects.get_or_create(
	    item=item,
	    user=request.user,
	    ordered=False,
    )
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
	    order = order_qs[0]
	    if order.items.filter(item_id=item.pk).exists():
	        order_item.quantity += 1
	        order_item.save()
	        messages.success(request, f"{item.ProductName}'s quantity was updated")
	        return redirect('order_summary')
	    else:
	        order.items.add(order_item)
	        order.save()
	        messages.success(request, f"{item.ProductName} was added to your Order")
	        return redirect('order_summary')

	else:
	    ordered_date = timezone.now()
	    order = Order.objects.create(
	        user=request.user, ordered=False, ordered_date=ordered_date)
	    order.items.add(order_item)
	    order.save()
	    messages.success(request, f"{item.ProductName} was added to your Order")
	    return redirect('order_summary')




#--------------------------REMOVE FROM CART 2--------------------------------------




def remove_from_cart2(request, pk):

    item = get_object_or_404(Products, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item_id=item.pk).exists():
            order.items.remove(order_item)
            order.save()
            messages.success(request, f"{item.ProductName} was removed from your Order")
                
            return redirect('order_summary')
        else:
            messages.info(request, f"{item.ProductName} was not in your Order")
            return redirect('order_summary')
    else:
        messages.info(request, "You don't have an active order!")
        return redirect('order_summary')











#---------------------------------------CONTACT ME----------------------------



@login_required(login_url='signin')
def contact_me(request):
	order = Order.objects.get(user=request.user, ordered=False)
	form = ContactMeForm()


	if request.method == 'POST':
		#To assign username automatically
	    username = request.user.username
	    
	    #subject = request.POST.get['subject']
	    message = request.POST.get('message')
	    phone = request.POST.get('phone')
	    email = request.POST.get('email')
	    place = request.POST.get('place')

	    new_msg = ContactMe.objects.create(username=username, email=email, place=place, phone=phone, message=message)



	    new_msg.save()

	    #HAPA USER IKISUBMIT DATA ZILE ORDER NA TAARIFA ZINGINE ZIJE KWANGU

	    to = request.POST.get('email')
	    username = request.user.username
	    phone = request.POST.get('phone')
	    place = request.POST.get('place')
	    message = message = request.POST.get('message')
	   # send_date = request.POST['send_date']
	    #to_dimoso_email = request.POST['to_dimoso_email']
	    to_dimoso_email = "juniordimoso8@gmail.com"
	    
	                
	    html_content = render_to_string(
	        "MyApp/email_template.html",
	        {
	        'title':'D-Trader ', 
	        'username':username,
	        'phone':phone,
	        'place':place,
	        "message":message,
	        "to":to,
	        "order":order,
	       # "send_date":send_date
	        
	        
	        
	        })
	    text_content = strip_tags(html_content)
	    email = EmailMultiAlternatives(
	    "D-Trader",
	    #content
	    text_content,
	    #from email
	    settings.EMAIL_HOST_USER,
	    #to
	    [to_dimoso_email]


	    )
	    email.attach_alternative(html_content,"text/html")
	    email.send(fail_silently=True)


	    #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
	    username = request.user.username
	    #last_name = request.POST['last_name']
	    email = request.POST.get('email')
	    subject = "Welcome to D-Trader"
	    message = f"Ahsante  {username} kwa kuweka oda ya bidhaa kutoka kwetu, wasiliana nasi kupitia Email: {to_dimoso_email} au Kwa namba ya simu 0628431507"
	    from_email = settings.EMAIL_HOST_USER
	    recipient_list = [email]
	    send_mail(subject, message, from_email, recipient_list, fail_silently=True)






	    #HAPA USER IKISUBMIT DATA ZILE ORDER NA TAARIFA ZINGINE ZIJE KWAKE

	    to = request.POST.get('email')
	    username = request.user.username
	    phone = request.POST.get('phone')
	    place = request.POST.get('place')
	    message = message = request.POST.get('message')
	   # send_date = request.POST['send_date']
	    #to_dimoso_email = request.POST['to_dimoso_email']
	    to_dimoso_email = "juniordimoso8@gmail.com"
	    
	                
	    html_content = render_to_string(
	        "MyApp/user_email_template.html",
	        {
	        'title':'D-Trader ', 
	        'username':username,
	        'phone':phone,
	        'place':place,
	        "message":message,
	        "to":to,
	        "order":order,
	       # "send_date":send_date
	        
	        
	        
	        })
	    text_content = strip_tags(html_content)
	    email = EmailMultiAlternatives(
	    "D-Trader",
	    #content
	    text_content,
	    #from email
	    settings.EMAIL_HOST_USER,
	    #to
	    [to]


	    )
	    email.attach_alternative(html_content,"text/html")
	    email.send(fail_silently=True)
	    messages.success(request,f"Message Sent Successfully to {to_dimoso_email} - D-Trader Manager ")
	    return redirect('contact_me')
	
	context = {
		"form":form,
		"order":order,
	}

	return render(request, "MyApp/contact_me.html",context)













#--------------------------CHECKOUT VIEW------------------------------


class CheckoutView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        # address = Address.objects.get(user=self.request.user, default=True)
        coupon_form = CouponForm()
        form = AddressForm()
        context = {
            'form': form,
            'order': order,
            'coupon_form': coupon_form,
            "DISPLAY_COUPON_FORM": True
            # 'address': address
        }
        return render(self.request, 'MyApp/checkout.html', context)

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = AddressForm(self.request.POST or None)
        if form.is_valid():
            street_address = form.cleaned_data.get('street_address')
            apartment_address = form.cleaned_data.get('apartment_address')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            save_info = form.cleaned_data.get('save_info')
            use_default = form.cleaned_data.get('use_default')
            payment_option = form.cleaned_data.get('payment_option')

            address = Address(
                user=self.request.user,
                street_address=street_address,
                apartment_address=apartment_address,
                country=country,
                zip=zip,
            )
            address.save()
            if save_info:
                address.default = True
                address.save()

            order.address = address
            order.save()

            if use_default:
                address = Address.objects.get(
                    user=self.request.user, default=True)
                order.address = address
                order.save()

            if payment_option == "S":
                return redirect('payment', payment_option="M-PESA")

            if payment_option == "P":
                return redirect('payment', payment_option="TIGO PESA")
            if payment_option == "H":
                return redirect('payment', payment_option="HALO PESA")

            if payment_option == "A":
                return redirect('payment', payment_option="AIRTEL MONEY")
            messages.info(self.request, "Invalid payment option")
            return redirect('checkout')
        else:
            print('form invalid')
            return redirect('checkout')


def payment_complete(request):
    x=datetime.datetime.today()
    current_date = x.strftime('%d-%m-%Y %H:%M')
    body = json.loads(request.body)
    order = Order.objects.get(
        user=request.user, ordered=False, id=body['orderID'])
    payment = Payment(
        user=request.user,
        stripe_charge_id=body['payID'],
        amount=order.get_total()
    )
    payment.save()

    # assign the payment to order
    order.payment = payment
    order.ordered = True
    order.save()
    messages.success(request, "Payment was successful")
    return redirect('home')


class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)

        context = {
            'order': order,
            "DISPLAY_COUPON_FORM": False

        }
        return render(self.request, 'MyApp/payment.html', context)

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        try:
            customer = stripe.Customer.create(
                email=self.request.user.email,
                description=self.request.user.username,
                source=self.request.POST['stripeToken']
            )
            amount = order.get_total()
            charge = stripe.Charge.create(
                amount=amount * 100,
                currency="usd",
                customer=customer,
                description="Test payment for buteks online",
            )
            payment = Payment(
                user=self.request.user,
                stripe_charge_id=charge['id'],
                amount=amount
            )
            payment.save()

            order.ordered = True
            order.payment = payment
            order.save()

            messages.success(self.request, "Payment was successful")
            return redirect('payment_error_message')
        except stripe.error.CardError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('payment_error_message')
        except stripe.error.InvalidRequestError as e:
            messages.success(self.request, "Invalid request")
            return redirect('payment_error_message')
        except stripe.error.AuthenticationError as e:
            messages.success(self.request, "Authentication error")
            return redirect('payment_error_message')
        except stripe.error.APIConnectionError as e:
            messages.success(self.request, "Check your connection")
            return redirect('payment_error_message')
        except stripe.error.StripeError as e:
            messages.success(
                self.request, "There was an error please try again")
            return redirect('payment_error_message')
        except Exception as e:
            messages.success(
                self.request, "A serious error occured we were notified")
            return redirect('payment_error_message')


class CouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            try:
                order = Order.objects.get(user=self.request.user, ordered=False)
                order.coupon = Coupon.objects.get(code=code)
                order.save()
                messages.success(self.request, "Successfully added coupon !")
                return redirect('checkout')
            except ObjectDoesNotExist:
                messages.success(self.request, "You don't have an active order")
                return redirect('home')
        messages.success(self.request, "Enter a valid coupon code")
        return redirect('checkout')



def payment_error_message(request):
	return render(request, "MyApp/payment_error_message.html")











#----------------------------------Wish List---------------------------------

def wish_list(request):
	order = Order.objects.get(user=request.user, ordered=False)

	context = {
		"order":order,
	}
	
	return render(request, "MyApp/wish_list.html",context)

def vendor_registration(request):
	if request.method == 'POST':
	    username = request.POST.get('username')
	    email = request.POST.get('email')
	    password = request.POST.get('password')
	    password2 = request.POST.get('password2')
	    #role = request.POST['role']

	    if password == password2:
	        if MyUser.objects.filter(email=email).exists():
	            messages.info(request, f"Email {email} Already Taken")
	            return redirect('vendor_registration')
	        elif MyUser.objects.filter(username=username).exists():
	            messages.info(request, f"Username {username} Already Taken")
	            return redirect('vendor_registration')
	        else:
	            user = MyUser.objects.create_user(username=username, email=email, password=password)
	            user.save()


	            #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
	            username = request.POST.get('email')
	            #last_name = request.POST['last_name']
	            email = request.POST.get('email')
	            subject = "Welcome to DIMOSO ELECTRONICS CENTER"
	            message = f"Ahsante  {username} kwa kujisajili kwenye mfumo wetu kama {username} email yako {email}. Nunua bidhaa bora na kwa bei nafuu kupitia Dimoso Electronics Center, unaweza kuweka order au kunitumia email kwa ajili ya kupata bidhaa zako kwa haraka. Ahsante {username} endelea kutembelea mfumo wetu "
	            from_email = settings.EMAIL_HOST_USER
	            recipient_list = [email]
	            send_mail(subject, message, from_email, recipient_list, fail_silently=True)



	            # #log user in and redirect to settings page
	            user_login = auth.authenticate(email=email, password=password)
	            auth.login(request, user_login)

	            
	            return redirect('home')
	    else:
	        messages.info(request, 'The Two Passwords Not Matching')
	        return redirect('vendor_registration')

	else:

		return render(request, "MyApp/vendor_registration.html")


def my_account(request):
	
	return render(request, "MyApp/my_account.html")

def D_trader_forum(request):
	
	return render(request, "MyApp/D_trader_forum.html")


@login_required(login_url='signin')
def search_products_everywhere(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(ProductName__icontains=query)
        results=Products.objects.filter(mysearch)
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'MyApp/search_products_everywhere.html',context)




def privacy_policy(request):
	privacy = PrivacyPolicy.objects.all()
	context = {
		"privacy":privacy,
	}
	return render(request, "MyApp/privacy_policy.html",context)


def uchafu(request):
	
	return render(request, "MyApp/uchafu.html")





@login_required(login_url='signin')
def ask(request):
	# order = Order.objects.get(user=request.user, ordered=False)
	# form = ContactMeForm()


	if request.method == 'POST':
		#To assign username automatically
	    username = request.user.username
	    
	    #subject = request.POST.get['subject']
	    
	    phone = request.POST.get('phone')
	    email = request.POST.get('email')
	    description = request.POST.get('description')

	    ask = Ask.objects.create(username=username, email=email, description=description, phone=phone)



	    ask.save()


	    #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
	    username = request.user.username
	    #last_name = request.POST['last_name']
	    email = request.POST.get('email')
	    subject = "Welcome to D-Trader"
	    message = f"Thanks {username} for asking your question, we will send your answer to your email: {email}"
	    from_email = settings.EMAIL_HOST_USER
	    recipient_list = [email]
	    send_mail(subject, message, from_email, recipient_list, fail_silently=True)




	    #HAPA USER IKISUBMIT DATA HILO SWALI NA TAARIFA ZINGINE ZIJE KWANGU

	    to = request.POST.get('email')
	    username = request.user.username
	    phone = request.POST.get('phone')
	    description = request.POST.get('description')
	    
	   # send_date = request.POST['send_date']
	    #to_dimoso_email = request.POST['to_dimoso_email']
	    to_dimoso_email = "juniordimoso8@gmail.com"
	    
	                
	    html_content = render_to_string(
	        "MyApp/ask_template.html",
	        {
	        'title':'D-Trader', 
	        'username':username,
	        'phone':phone,
	        'description':description,
	        
	        "to":to,
	        
	       # "send_date":send_date
	        
	        
	        
	        })
	    text_content = strip_tags(html_content)
	    email = EmailMultiAlternatives(
	    "D-Trader",
	    #content
	    text_content,
	    #from email
	    settings.EMAIL_HOST_USER,
	    #to
	    [to_dimoso_email]


	    )
	    email.attach_alternative(html_content,"text/html")
	    email.send(fail_silently=True)








	    messages.success(request,f"Message Sent Successfully to D-Trader Manager ")
	    #return HttpResponseRedirect(request.path)
	    return HttpResponse(f"Thanks {username} for asking your question, we will send your answer to your email: {to}")
	
	

	




