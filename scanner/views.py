from django.shortcuts import render, redirect
from .models import ScanResult

def show_scanner(request):
    if request.method == "POST":
        ScanResult.objects.create(
            temperature=request.POST.get("temperature"),
            status=request.POST.get("status")
        )
        return redirect("/")

    results = ScanResult.objects.all().order_by("-scanned_at")

    return render(
        request,
        "scanner.html",
        {"results": results}
    )
