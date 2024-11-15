from django.shortcuts import render


def study_in_us(request):
    return render(request, 'study/usa.html')


def study_in_austrilia(request):
    return render(request, 'study/austrilia.html')


def study_in_canada(request):
    return render(request, 'study/canada.html')


def study_in_japan(request):
    return render(request, 'study/japan.html')


def study_in_korea(request):
    return render(request, 'study/korea.html')


def study_in_europe(request):
    return render(request, 'study/europe.html')
