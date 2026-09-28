
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

from .models import User, CardSale


# =========================
# DASHBOARD
# =========================

def dashboard(request):

    sales = CardSale.objects.select_related('user').order_by('-id')

    total_cards = sales.aggregate(
        total=Sum('card_quantity')
    )['total'] or 0

    total_amount = sales.aggregate(
        total=Sum('total_amount')
    )['total'] or 0

    users = User.objects.all().order_by('name')

    context = {
        'sales': sales,
        'users': users,
        'total_cards': total_cards,
        'total_amount': total_amount,
    }

    return render(
        request,
        'sales/dashboard.html',
        context
    )


# =========================
# USER CRUD
# =========================

def user_list(request):

    users = User.objects.all().order_by('-id')

    return render(
        request,
        'sales/user_list.html',
        {'users': users}
    )


def user_create(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')

        User.objects.create(
            name=name,
            phone=phone,
            photo=photo
        )

        return redirect('user_list')

    return render(
        request,
        'sales/user_form.html'
    )


def user_update(request, id):

    user = get_object_or_404(User, id=id)

    if request.method == 'POST':

        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')

        photo = request.FILES.get('photo')

        if photo:
            user.photo = photo

        user.save()

        return redirect('user_list')

    return render(
        request,
        'sales/user_form.html',
        {'user': user}
    )


def user_delete(request, id):

    user = get_object_or_404(User, id=id)

    if request.method == 'POST':

        user.delete()

        return redirect('user_list')

    return render(
        request,
        'sales/user_delete.html',
        {'user': user}
    )


# =========================
# CARD SALE CRUD
# =========================

def sale_list(request):

    sales = CardSale.objects.select_related(
        'user'
    ).order_by('-id')

    return render(
        request,
        'sales/sale_list.html',
        {'sales': sales}
    )


def sale_create(request):

    users = User.objects.all().order_by('name')

    if request.method == 'POST':

        user_id = request.POST.get('user')
        quantity = int(
            request.POST.get('card_quantity')
        )

        user = get_object_or_404(
            User,
            id=user_id
        )

        CardSale.objects.create(
            user=user,
            card_quantity=quantity,
            price_per_card=50
        )

        return redirect('sale_list')

    return render(
        request,
        'sales/sale_form.html',
        {'users': users}
    )


def sale_update(request, id):

    sale = get_object_or_404(
        CardSale,
        id=id
    )

    users = User.objects.all().order_by('name')

    if request.method == 'POST':

        user_id = request.POST.get('user')
        quantity = int(
            request.POST.get('card_quantity')
        )

        sale.user = get_object_or_404(
            User,
            id=user_id
        )

        sale.card_quantity = quantity

        sale.save()

        return redirect('sale_list')

    return render(
        request,
        'sales/sale_form.html',
        {
            'sale': sale,
            'users': users
        }
    )


def sale_delete(request, id):

    sale = get_object_or_404(
        CardSale,
        id=id
    )

    if request.method == 'POST':

        sale.delete()

        return redirect('sale_list')

    return render(
        request,
        'sales/sale_delete.html',
        {'sale': sale}
    )

