import datetime
from datetime import timedelta

from car_shop.settings import EMAIL_HOST_USER  # IT SHOWS SOME ERROR BUT ITS WORKS
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def seller_log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pas = request.POST.get('password')
        call_model = reg_seller.objects.all()
        for i in call_model:
            if i.companyemail == email and i.password == pas:
                request.session['id'] = i.id
                return redirect(seller_profile)
                # return HttpResponse('Login Success')
        else:
            return HttpResponse('Login Failed')
    return render(request, '1 seller-log.html')


def seller_reg(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        profilepic = request.FILES.get('profilepic')
        businessname = request.POST.get('companyname')
        businessemail = request.POST.get('companyemail')
        businessphone = request.POST.get('phonenumber')
        businessaddress = request.POST.get('address')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpassword')

        if password == confirmpass:
            call_model = reg_seller(fullname=fullname, username=username, profilepic=profilepic,
                                    companyname=businessname
                                    , companyemail=businessemail,
                                    companyphone=businessphone, companyaddress=businessaddress, password=password)
            call_model.save()
            return HttpResponse('registration success')
        else:
            return HttpResponse('registration Failed')

    return render(request, '2 seller-reg.html')


def seller_profile(request):
    id1 = request.session['id']
    a = reg_seller.objects.get(id=id1)
    img = str(a.profilepic).split('/')[-1]
    return render(request, '3 seller-profile.html', {'data': a, 'image': img})


def product_upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        description = request.POST.get('description')
        km = request.POST.get('km')
        price = request.POST.get('price')
        fuel = request.POST.get('fuel')
        owner = request.POST.get('vehicleowner')
        cat = request.POST.get('category')

        call_model = upload_product(image=image, name=name, description=description, km=km,
                                    price=price, fuel=fuel, owner=owner, category=cat)
        call_model.save()
        return HttpResponse('Product Upload Successfully')
    # else:
    #     return HttpResponse('Product Upload Unsuccessfully')

    return render(request, '4 product-upload.html')


def seller_edit_profile(request):
    id1 = request.session['id']
    a = reg_seller.objects.get(id=id1)
    img = str(a.profilepic).split('/')[-1]
    if request.method == 'POST':
        a.fullname = request.POST.get('fullname')
        a.username = request.POST.get('username')
        # a.profilepic = request.FILES.get('profilepicture')
        if request.FILES.get('profilepicture') == None:
            a.save()
        else:
            a.profilepic = request.FILES['profilepicture']
            a.save()
        a.companyname = request.POST.get('companyname')
        a.companyaddress = request.POST.get('address')
        a.companyemail = request.POST.get('email')
        a.companyphone = request.POST.get('phone')
        a.save()
        return redirect(seller_profile)
    return render(request, '5 seller-profile-edit.html', {'data': a, 'image': img})


def display_product(request):
    id = []
    im = []
    na = []
    ds = []
    km = []
    pr = []
    fu = []
    ow = []
    ca = []
    a = upload_product.objects.all()
    for i in a:
        idd = i.id
        id.append(idd)
        imm = str(i.image).split('/')[-1]
        im.append(imm)
        naa = i.name
        na.append(naa)
        dss = i.description
        ds.append(dss)
        kmm = i.km
        km.append(kmm)
        prr = i.price
        pr.append(prr)
        fuu = i.fuel
        fu.append(fuu)
        oww = i.owner
        ow.append(oww)
        caa = i.category
        ca.append(caa)
    mylist = zip(im, na, ds, km, pr, fu, ow, ca, id)
    return render(request, '6 product-display.html', {'data': mylist})


def buyer_log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pas = request.POST.get('password')
        call_model = reg_buyer.objects.all()
        for i in call_model:
            if i.email == email and i.password == pas:
                request.session['b_id'] = i.id
                return redirect(buyer_product_view)
                # return HttpResponse('Login Success')
        else:
            return HttpResponse('Login Failed')
    return render(request, '7 buyer-log.html')


def buyer_reg(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        profilepic = request.FILES.get('profile')
        address = request.POST.get('address')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpassword')

        a = reg_buyer(fullname=fullname, username=username, profilepic=profilepic,
                      address=address, email=email, gender=gender, password=password)
        call_model = reg_buyer.objects.all()

        for i in call_model:
            if i.email == email or i.username == username:
                return HttpResponse('Already Registered')
        else:
            a.save()
        if password == confirmpass:
            return HttpResponse('Registration Success')
        else:
            return HttpResponse('Invalid Password')
    return render(request, '8 buyer-reg.html')


def buyer_profile(request):

    id1 = request.session['b_id']
    a = reg_buyer.objects.get(id=id1)
    img = str(a.profilepic).split('/')[-1]
    return render(request, '9 buyer-profile.html', {'data': a, 'image': img})


def buyer_logout(request):
    logout(request)
    return redirect(buyer_log)


def buyer_profile_edit(request):
    id1 = request.session['b_id']
    a = reg_buyer.objects.get(id=id1)
    img = str(a.profilepic).split('/')[-1]
    if request.method == 'POST':
        a.fullname = request.POST.get('fullname')
        a.username = request.POST.get('username')
        # a.profilepic = request.FILES.get('profile')
        if request.FILES.get('profile') == None:
            a.save()
        else:
            a.profilepic = request.FILES['profile']
            a.save()
        a.address = request.POST.get('address')
        a.email = request.POST.get('email')
        a.gender = request.POST.get('gender')
        a.save()
        return redirect(buyer_profile)
    return render(request, '10 buyer-profile-edit.html', {'data': a, 'image': img})


# def buyer_product_view(request):
#     id = []
#     im = []
#     na = []
#     ds = []
#     km = []
#     pr = []
#     fu = []
#     ow = []
#     ca = []
#     a = upload_product.objects.all()
#     for i in a:
#         idd = i.id
#         id.append(idd)
#         imm = str(i.image).split('/')[-1]
#         im.append(imm)
#         naa = i.name
#         na.append(naa)
#         dss = i.description
#         ds.append(dss)
#         kmm = i.km
#         km.append(kmm)
#         prr = i.price
#         pr.append(prr)
#         fuu = i.fuel
#         fu.append(fuu)
#         oww = i.owner
#         ow.append(oww)
#         caa = i.category
#         ca.append(caa)
#     print(ca)
#     mylist = zip(im, na, ds, km, pr, fu, ow, ca, id)
#     return render(request, '12 buyer-product-view.html', {'data': mylist})


def buyer_product_view(request):
    category = request.GET.get('category')  # Get the selected category from the GET request

    # Filter products based on the selected category if provided, otherwise get all products
    if category:
        products = upload_product.objects.filter(category=category)
    else:
        products = upload_product.objects.all()

    # Process and prepare data
    data = [
        (str(product.image).split('/')[-1],
         product.name,
         product.description,
         product.km,
         product.price,
         product.fuel,
         product.owner,
         product.category,
         product.id)
        for product in products
    ]

    return render(request, '12 buyer-product-view.html', {'data': data})


def product_edit(request):
    return render(request, '11 product-edit.html')


def wishlist(request, id):
    a = upload_product.objects.get(id=id)
    idd = request.session['b_id']  # userid already login functionil create cheythit ond (request.session['id'])
    c = wish.objects.all()
    for i in c:
        if id == i.pro_id and idd == i.userid:
            return HttpResponse('item already exist')
    else:
        b = wish(userid=idd, pro_img=a.image, pro_name=a.name, pro_des=a.description, pro_km=a.km, pro_price=a.price,
                 pro_fuel=a.fuel, pro_owner=a.owner, pro_category=a.category, pro_id=a.id)
        b.save()
        return HttpResponse('item added to wish list')


def wishlist_view(request):
    usr_id = request.session['b_id']
    id = []
    p_id = []
    u_id = []
    img = []
    name = []
    price = []
    a = wish.objects.all()
    for i in a:
        idd = i.id
        id.append(idd)
        u_idd = i.userid
        u_id.append(u_idd)
        p_idd = i.pro_id
        p_id.append(p_idd)
        imgg = str(i.pro_img).split('/')[-1]
        img.append(imgg)
        namee = i.pro_name
        name.append(namee)
        pricee = i.pro_price
        price.append(pricee)

    mylist = zip(img, name, price, id, u_id, p_id)
    return render(request, '13 wishlist.html', {'data': mylist, 'userid': usr_id})


def delete_wish(request, id):
    a = wish.objects.get(id=id)
    a.delete()
    return redirect(wishlist_view)


def add_to_cart(request, id):
    a = upload_product.objects.get(id=id)
    idd = request.session['b_id']  # userid already login functionil create cheythit ond (request.session['id'])
    c = cart.objects.all()
    for i in c:
        if id == i.pro_id and idd == i.userid:
            return HttpResponse('item already exist')
    else:
        count = 1
        b = cart(userid=idd, pro_img=a.image, pro_name=a.name, pro_des=a.description, pro_km=a.km, pro_price=a.price,
                 pro_fuel=a.fuel, pro_owner=a.owner, pro_category=a.category, pro_id=a.id, quantity=count)
        b.save()
        return HttpResponse('item added to cart list')


def cart_view(request):
    usr_id = request.session['b_id']
    id = []
    p_id = []
    u_id = []
    img = []
    name = []
    price = []
    fuel = []
    cat = []
    qty = []
    ow = []
    subtotal = 0
    a = cart.objects.filter(userid=usr_id)

    for i in a:
        idd = i.id
        id.append(idd)
        u_idd = i.userid
        u_id.append(u_idd)
        p_idd = i.pro_id
        p_id.append(p_idd)
        imgg = str(i.pro_img).split('/')[-1]
        img.append(imgg)
        namee = i.pro_name
        name.append(namee)
        pricee = i.pro_price
        price.append(pricee)
        fuell = i.pro_fuel
        fuel.append(fuell)
        catt = i.pro_category
        cat.append(catt)
        qtyy = i.quantity
        qty.append(qtyy)
        oww = i.pro_owner
        ow.append(oww)

    subtotal = sum(price)
    request.session['subtotal'] = subtotal
    request.session.save()
    mylist = zip(img, name, price, id, u_id, p_id, fuel, cat, qty, ow)
    return render(request, '14 cart-view.html', {'data': mylist, 'userid': usr_id, 'subtotal': subtotal})


def delete_cart(request, id):
    a = cart.objects.get(id=id)
    a.delete()
    return redirect(cart_view)


def cartincrement(request, id):
    a = cart.objects.get(id=id)
    b = upload_product.objects.get(id=a.pro_id)
    price = b.price
    a.quantity += 1
    a.pro_price = price * a.quantity
    a.save()
    return redirect(cart_view)


def cartdecrement(request, id):
    a = cart.objects.get(id=id)
    b = upload_product.objects.get(id=a.pro_id)
    price = b.price
    a.quantity -= 1
    a.pro_price = price * a.quantity
    a.save()
    return redirect(cart_view)


def shipping_address(request):
    try:
        user_id = request.session['b_id']
        a = delivery_address.objects.all()

        for i in a:
            if i.userid == user_id:
                return redirect(address_display)
        else:
            raise Exception

    except Exception:

        if request.method == 'POST':
            user_id = request.session['b_id']
            fullname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            address = request.POST.get('address')
            city = request.POST.get('city')
            postal = request.POST.get('zipcode')
            phone = request.POST.get('phone')
            email = request.POST.get('emailaddress')

            call_model = delivery_address(userid=user_id, fullname=fullname, lastname=lastname, address=address,
                                          city=city, postal=postal, phone=phone, email=email)
            call_model.save()
            return redirect(address_display)
        return render(request, '15 shipping-address.html')


def address_display(request):
    warning_message = None
    user_id = request.session['b_id']
    a = delivery_address.objects.all()
    if request.method == 'POST':
        address1 = request.POST.get('selected_address')
        if address1:
            request.session['ad'] = address1
            return redirect(payment)
        else:
            warning_message = 'Please select an address'
    return render(request, '16 shipping-address-view.html', {'data': a, 'id': user_id, 'warning': warning_message})


def add_new_address(request):
    if request.method == 'POST':
        user_id = request.session['b_id']
        fullname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal = request.POST.get('zipcode')
        phone = request.POST.get('phone')
        email = request.POST.get('emailaddress')

        call_model = delivery_address(userid=user_id, fullname=fullname, lastname=lastname, address=address,
                                      city=city, postal=postal, phone=phone, email=email)
        call_model.save()
        return redirect(address_display)
    return render(request, '15 shipping-address.html')


def full_details(request):
    user_id = request.session['b_id']
    model_cart = cart.objects.all()
    model_address = delivery_address.objects.all()

    total_price = request.session['subtotal']
    address1 = []
    order_date = datetime.date.today()
    estimate_date = order_date + timedelta(days=30)

    for i in model_address:
        if i.userid == user_id:
            address1.append(i.fullname)
            address1.append(i.lastname)
            address1.append(i.address)
            address1.append(i.city)
            address1.append(i.postal)
            address1.append(i.phone)
            address1.append(i.email)

    product_list = []
    for i in model_cart:
        if i.userid == user_id:
            pic = str(i.pro_img).split('/')[-1]
            product_list.append(pic)
            product_list.append(i.pro_name)
            product_list.append(i.pro_des)
            product_list.append(i.pro_km)
            product_list.append(i.pro_price)
            product_list.append(i.pro_fuel)
            product_list.append(i.pro_owner)
            product_list.append(i.pro_category)
            product_list.append(i.quantity)

    call_model = details_full(userid=user_id, address=address1, product_list=product_list, total_price=total_price,
                              order_date=order_date, estimated_date=estimate_date)
    call_model.save()

    return HttpResponse('success')


def payment(request):
    user_id = request.session['b_id']
    id = []
    p_id = []
    u_id = []
    img = []
    name = []
    price = []
    fuel = []
    cat = []
    qty = []
    ow = []
    subtotal = 0
    carts = cart.objects.filter(userid=user_id)
    buyer = reg_buyer.objects.filter(id=user_id)

    for i in carts:
        idd = i.id
        id.append(idd)
        u_idd = i.userid
        u_id.append(u_idd)
        p_idd = i.pro_id
        p_id.append(p_idd)
        imgg = str(i.pro_img).split('/')[-1]
        img.append(imgg)
        namee = i.pro_name
        name.append(namee)
        pricee = i.pro_price
        price.append(pricee)
        fuell = i.pro_fuel
        fuel.append(fuell)
        catt = i.pro_category
        cat.append(catt)
        qtyy = i.quantity
        qty.append(qtyy)
        oww = i.pro_owner
        ow.append(oww)

    subtotal = sum(price)
    request.session['subtotal'] = subtotal
    request.session.save()
    mylist = zip(img, name, price, id, u_id, p_id, fuel, cat, qty, ow)

    if request.method == 'POST':
        card_number = request.POST.get('cardnumber')
        card_holder = request.POST.get('cardholder')
        expires = request.POST.get('expires')
        ccv = request.POST.get('ccv')

        subject = 'checking'
        message = 'success'
        email_from = EMAIL_HOST_USER
        send_mail(subject, message, email_from, ['nithin8157885525@gmail.com'])

        carts.delete()

        return redirect(preview)

    return render(request, '17 payment.html', {'data': mylist, 'userid': user_id, 'subtotal': subtotal})


def preview(request):
    user_id = request.session['b_id']
    id = []
    p_id = []
    u_id = []
    img = []
    name = []
    price = []
    fuel = []
    cat = []
    qty = []
    ow = []
    subtotal = 0
    carts = cart.objects.filter(userid=user_id)


    for i in carts:
        idd = i.id
        id.append(idd)
        u_idd = i.userid
        u_id.append(u_idd)
        p_idd = i.pro_id
        p_id.append(p_idd)
        imgg = str(i.pro_img).split('/')[-1]
        img.append(imgg)
        namee = i.pro_name
        name.append(namee)
        pricee = i.pro_price
        price.append(pricee)
        fuell = i.pro_fuel
        fuel.append(fuell)
        catt = i.pro_category
        cat.append(catt)
        qtyy = i.quantity
        qty.append(qtyy)
        oww = i.pro_owner
        ow.append(oww)

    subtotal = sum(price)
    request.session['subtotal'] = subtotal
    request.session.save()

    mylist = zip(img, name, price, id, u_id, p_id, fuel, cat, qty, ow)

    return render(request,'18 preview-page.html',{'data': mylist, 'userid': user_id, 'subtotal': subtotal})


