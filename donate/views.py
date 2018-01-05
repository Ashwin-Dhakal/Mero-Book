from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Details
from .forms import Donate_Book
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from . import forms

def index(request):
    total_books = Details.objects.all().count()
    total_users = User.objects.all().count()
    context = {
        "total_books": total_books,
        "total_users": total_users,
        "ward_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27,
                       28, 29, 30, 31, 32, 33, 34, 35],
        "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],

    }

    return render(request, 'donate/index.html', context)


def books_list(request):
    queryset = Details.objects.all().order_by("-id")
    context = {
        "object_list": queryset,  # this context is the dictionary for impoting the objects of databaset
    }
    return render(request, 'donate/books_list.html', context)


@login_required(login_url='/login/')
def book_detail(request, id):
    instance = get_object_or_404(Details, id=id)
    context = {
        "instance": instance,
        "ward_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35],
        "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "edition_count": ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"],

    }
    return render(request, 'donate/book_detail.html', context)


@login_required(login_url='/login/')
def profile(request):
    queryset_list = Details.objects.filter(user_id=request.user.id).order_by("-id")
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "queryset_list": queryset,
        "page_request_var": page_request_var
    }
    return render(request, 'donate/profile.html', context)


def contributer_board(request):
    return render(request, 'donate/contributer_board.html')


@login_required(login_url='/login/')
def search_list(request):
    query1 = request.GET.get('q1')
    query2 = request.GET.get('q2')
    query3 = request.GET.get('q3')
    query4 = request.GET.get('q4')
    only_open = Details.objects.filter(Status="Open")
    if query1 and query2 and query3 and query4:
        queryset_list = only_open.filter(
            Q(Name__iexact=query1) &
            Q(Class=query2) &
            Q(Your_District__iexact=query3) &
            Q(Ward_number=query4)
        ).distinct()
        paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)
        context = {
            "queryset_list": queryset,
            "page_request_var": page_request_var
        }
        return render(request, 'donate/search_list.html', context)
    else:
        return render(request, 'donate/404.html')


@login_required(login_url='/login/')  # LOGIN_URL = '/login/'
def donate_book(request):
    form = Donate_Book(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message response
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "ward_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35],
        "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "edition_count": ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth" ],
    }

    return render(request, 'donate/donate_book.html', context)


def donate_book_update(request, id=None):
    instance = get_object_or_404(Details, id=id)
    form = Donate_Book(request.POST or None, instance=instance)
    if request.user.is_authenticated() and instance.user.id == request.user.id:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # message_response
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "instance": instance,
            "form": form,
            "ward_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35],
            "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "edition_count": ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"],

        }
        return render(request, 'donate/donate_book.html', context)
    else:
        response = HttpResponse("You donot have permission to do this")
        return response


def test(request):
    queryset = Details.objects.filter(Name__iexact="Q")
    total_users = User.objects.all().count()
    context = {
        "object_list": queryset,  # this context is the dictionary for impoting the objects of databaset
        "total_users": total_users,
    }
    return render(request, 'donate/test.html', context)

#
# def delete(request, id=None):
#     instance = get_object_or_404(Details, id=id)
#     if request.user.is_authenticated() and instance.user.id == request.user.id:
#         instance.delete()
#         return redirect("books_list")
#     else:
#         response = HttpResponse("You dont have permission to do this")
#         return response

def contact_us(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ashwindhakal97@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "donate/contact_us.html", {'form': form})

def success(request):
    return render(request, 'donate/success.html')
