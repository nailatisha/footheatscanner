from django.shortcuts import render, redirect, get_object_or_404
from .models import ScanResult, Scan, AIPrediction
from .services import generate_diagnosis
from .ml_model import predict_diagnosis

# LANDING PAGE

def landing(request):
    latest_scan = ScanResult.objects.order_by('-scanned_at').first()
    return render(request, 'scanner/landing.html', {
        'latest_scan': latest_scan
    })



# SCANNER PAGE (FORM + RESULT)

def scanner_view(request):
    if request.method == "POST":
        temperature = float(request.POST.get("temperature"))
        region = request.POST.get("region", "heel")

        # contoh logika delta suhu (nanti dari image / dataset)
        delta_temp = abs(temperature - 32.0)

        diagnosis, confidence = generate_diagnosis(delta_temp)

        ScanResult.objects.create(
            temperature=temperature,
            region=region,
            delta_temp=delta_temp,
            confidence=confidence,
            diagnosis=diagnosis,
            status="Scan completed"
        )

        return redirect("scanner")

    results = ScanResult.objects.order_by("-scanned_at")[:10]

    return render(request, "scanner/scanner.html", {
        "results": results
    })



# RESULT DETAIL (ML OUTPUT)

def results(request, scan_id):
    scan = get_object_or_404(ScanResult, id=scan_id)
    return render(request, 'scanner/result.html', {
        'scan': scan
    })



# ML INFERENCE (DIPANGGIL SERVICE)

def run_inference(scan_result):
    delta_temp = scan_result.delta_temp
    diagnosis, confidence = predict_diagnosis(delta_temp)

    scan_result.diagnosis = diagnosis
    scan_result.confidence = confidence
    scan_result.save()
