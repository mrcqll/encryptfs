from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FileUploadForm
from .models import UploadedFile


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(
        request,
        "files/register.html",
        {"form": form}
    )


@login_required
def dashboard(request):
    uploaded_files = UploadedFile.objects.filter(
        owner=request.user
    ).order_by("-uploaded_at")

    return render(
        request,
        "files/dashboard.html",
        {"files": uploaded_files}
    )


@login_required
def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.owner = request.user
            uploaded_file.save()
            return redirect("dashboard")
    else:
        form = FileUploadForm()

    return render(
        request,
        "files/upload.html",
        {"form": form}
    )


@login_required
def download_file(request, file_id):
    uploaded_file = get_object_or_404(
        UploadedFile,
        id=file_id,
        owner=request.user
    )

    try:
        return FileResponse(
            uploaded_file.file.open("rb"),
            as_attachment=True,
            filename=uploaded_file.file.name.split("/")[-1]
        )
    except OSError:
        raise Http404("File not found")