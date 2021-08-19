from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def resume_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, f' {data.name.title()}, Your response has been recorded')
            return redirect('resume')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


def blog_grid(request):
    return render(request, 'blog-grid.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def portfolio_detail(request):
    return render(request, 'portfolio-details.html')