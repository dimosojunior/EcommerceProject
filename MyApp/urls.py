
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('<int:category_id>/', views.home, name="product_by_category"),
    path('search_product_autocomplete/', views.search_product_autocomplete, name="search_product_autocomplete"),
    path('view_product/<str:pk>/', views.view_product.as_view(), name="view_product"),
    


    path('T_shirt/', views.T_shirt, name="T_shirt"),


    path('Shirt/', views.Shirt, name="Shirt"),


    path('Skirt/', views.Skirt, name="Skirt"),


    path('SmartPhones/', views.SmartPhones, name="SmartPhones"),


    path('Dell_Laptops/', views.Dell_Laptops, name="Dell_Laptops"),


    path('Hp_Laptops/', views.Hp_Laptops, name="Hp_Laptops"),


    path('Trouser/', views.Trouser, name="Trouser"),

    path('Shoes/', views.Shoes, name="Shoes"),


    path('Web/', views.Web, name="Web"),


    path('Graphics/', views.Graphics, name="Graphics"),


    path('Gown/', views.Gown, name="Gown"),

    path('School_Products/', views.School_Products, name="School_Products"),

    path('Arduino_Products/', views.Arduino_Products, name="Arduino_Products"),

    path('Lenovo_Laptops/', views.Lenovo_Laptops, name="Lenovo_Laptops"),



    path('More/', views.More, name="More"),

    path('uchafu/', views.uchafu, name="uchafu"),








    path('add_to_cart/<str:pk>/', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<str:pk>/', views.remove_from_cart, name="remove_from_cart"),
    path('add_to_cart2/<str:pk>/', views.add_to_cart2, name="add_to_cart2"),
    path('remove_from_cart2/<str:pk>/', views.remove_from_cart2, name="remove_from_cart2"),
    path('remove_single_from_cart/<str:pk>/', views.remove_single_from_cart, name="remove_single_from_cart"),
    path('order_summary/', views.order_summary.as_view(), name="order_summary"),
    path('contact_me/', views.contact_me, name="contact_me"),



    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    path('add-coupon', views.CouponView.as_view(), name="add_coupon"),
    path('payment-complete', views.payment_complete, name="payment_complete"),
    path('payment_error_message', views.payment_error_message, name="payment_error_message"),






    path('wish_list/', views.wish_list, name="wish_list"),
    path('vendor_registration/', views.vendor_registration, name="vendor_registration"),
    path('my_account/', views.my_account, name="my_account"),
    path('D_trader_forum/', views.D_trader_forum, name="D_trader_forum"),
    path('search_products_everywhere/', views.search_products_everywhere, name="search_products_everywhere"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
    path('ask/', views.ask, name="ask"),
]