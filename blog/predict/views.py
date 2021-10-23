from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        
        age = float(request.POST.get('age'))
        Medu = float(request.POST.get('Medu'))
        Fedu = float(request.POST.get('Fedu'))
        failures = float(request.POST.get('failures'))
        freetime = float(request.POST.get('freetime'))
        goout = float(request.POST.get('goout'))
        Walc = float(request.POST.get('Walc'))
        absences = float(request.POST.get('absences'))
        G1 = float(request.POST.get('G1'))
        G2 = float(request.POST.get('G2'))


        model = pd.read_pickle(r"C:\Users\k1r\Desktop\blog\reg.pickle")
        
        result = model.predict([[age,Medu,Fedu,failures,freetime,goout,Walc,absences,G1,G2]])
        classification = result[0]

        PredResults.objects.create(age=age, Medu=Medu, Fedu=Fedu, failures=failures, freetime=freetime, goout=goout, Walc=Walc, absences=absences, G1=G1,
                                   G2=G2, classification=classification)

        return JsonResponse({'result': classification, 'age': age,
                             'Medu': Medu, 'Fedu': Fedu, 'failures': failures, 'freetime': freetime, 'goout': goout, 'Walc': Walc , 'absences': absences, 'G1': G1, 'G2': G2},
                            safe=False)


def view_results(request):
    
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
