from django.shortcuts import render, redirect
from .models import ScanResult

def show_scanner(request):
    if request.method == "POST":
        temperature = request.POST.get("temperature")
        status = request.POST.get("status")

        ScanResult.objects.create(
            temperature=temperature,
            status=status
        )

        return redirect("/")

    results = ScanResult.objects.all()
    context = {
        "results": results
    }
    return render(request, "scanner.html", context)
