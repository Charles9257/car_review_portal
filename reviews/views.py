from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseForbidden

@login_required
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('dealership_detail', pk=review.dealership.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'edit': True})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")

    if request.method == 'POST':
        dealership_pk = review.dealership.pk
        review.delete()
        return redirect('dealership_detail', pk=dealership_pk)
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})
