from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume

def main_page(request):
    return render(request, 'main.html')

@login_required
def upload_resume(request):
    try:
        resume = request.user.resume
    except Resume.DoesNotExist:
        resume = None

    if request.method == 'POST':
        form = ResumeUploadForm(
            request.POST,
            request.FILES,
            instance=resume
        )
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.parsed = False
            resume.save()
            return redirect('profile')
    else:
        form = ResumeUploadForm(instance=resume)

    return render(
        request,
        'accounts/upload_resume.html',
        {'form': form}
    )
