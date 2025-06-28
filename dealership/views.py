 # backend/dealership/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Dealership
from reviews.models import Review
from reviews.forms import ReviewForm
from django.core.paginator import Paginator

def index(request):
    dealerships = Dealership.objects.all()  # get all dealerships
    return render(request, 'index.html', {'dealerships': dealerships})

 

def dealership_detail(request, pk):
    dealership = get_object_or_404(Dealership, pk=pk)
    reviews = Review.objects.filter(dealership=dealership).order_by('-created_at')

    paginator = Paginator(reviews, 5)  # 5 reviews per page
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
    # Handle review submission
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.dealership = dealership
            review.save()
            return redirect('dealership_detail', pk=dealership.pk)
    else:
        form = ReviewForm()

    context = {
        'dealership': dealership,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'dealership/detail.html', context)