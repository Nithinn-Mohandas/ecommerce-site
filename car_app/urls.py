from django.urls import path

from .views import *

urlpatterns = [
    path('index/', index),
    path('seller-log/', seller_log),
    path('seller-reg/', seller_reg),
    path('seller-profile/', seller_profile),
    path('product-upload/', product_upload),
    path('edit-profile/', seller_edit_profile),
    path('product-display/', display_product),
    path('buyer-log/', buyer_log),
    path('buyer-reg/', buyer_reg),
    path('buyer-profile/', buyer_profile),
    path('buyer-logout/',buyer_logout),
    path('buyer-profile-edit/', buyer_profile_edit),
    # path('buyer-product/',buyer_product_view),

    path('buyer-product/', buyer_product_view, name='buyer_product_view'),

    path('wishlist/<int:id>', wishlist),
    path('wishlist-view/', wishlist_view),
    path('delete-wish/<int:id>', delete_wish),

    path('addtocart/<int:id>', add_to_cart),
    path('cartview/', cart_view),
    path('delete-cart/<int:id>',delete_cart),

    path('increment/<int:id>',cartincrement),
    path('decrement/<int:id>',cartdecrement),

    path('address-display/',address_display),
    path('shipping-address/',shipping_address),
    path('add-new-address/',add_new_address),
    path('preview/',full_details),
    path('payment/',payment),
    path('success/',preview),

]
