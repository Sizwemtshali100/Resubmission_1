from django.shortcuts import redirect, render
from flask import Response
from . models import Contract_Model
from . forms import Contract_forms
from django.http import HttpResponseRedirect, HttpResponse
import csv
from django.http import FileResponse
import io
from django.core.paginator import Paginator


#Generate Textfiles
def csv_File(request):
    Response_csv = HttpResponse(content_type='text/csv')
    Response_csv['content_disposition'] = 'attachment; filename=Contract_id.csv'

    #Creating a writer for CSV
    writer = csv.writer(Response_csv)

    Model_csv = Contract_Model.objects.all()

    #Add column names
    writer.writerow([
        'Contract_id', 
        'Initials',
        'ID_Number',
        'Surname',
        'Premium',
        'Name_of_Bank',
        'Name_of_Branch',
        'Name_of_Type',])

    #Looping through Contract
    for csv_models in Model_csv:
        writer.writerow([csv_models.Contract_ID, csv_models.Initials, csv_models.ID_Number, csv_models.Surname, csv_models.Premium ,csv_models.Name_of_Bank])

    return Response_csv

def TextFile(request):
    Response_text = HttpResponse(content_type='text/plain')
    Response_text['Content-disposition'] = 'attachment; filename=Once_1.txt'

    Text_model = Contract_Model.objects.all()
    Listings = []

    for model_text in Text_model:
        Listings.append(f'{model_text.ID_Number}\n')

    Response_text.writelines(Listings)
    return Response_text    
# Create your views here.
def Delete(request, details_id):
    Delete = Contract_Model.objects.get(pk=details_id)
    Delete.delete()
    return redirect('Home') 

def Update(request, details_id):
    Update = Contract_Model.objects.get(pk=details_id)
    Update_form = Contract_forms(
        request.POST or None, instance=Update
        )
    if Update_form.is_valid():
        Update_form.save()
        return redirect('Home')
    return render(request, 'May_4_app/Update.html',
    {'Update':Update, 'Update_form':Update_form})

def Search(request):
    if request.method == 'POST':
        Searched = request.POST['Searched']
        Search_Results = Contract_Model.objects.filter(Contract_ID__contains=Searched)
        return render(request, 'May_4_app/Search.html',
    {'Searched':Searched,
    'Search_Results':Search_Results})
    else:
        return render(request, 'May_4_app/Search.html',
    )

def Details(request, details_id):
    Details_get = Contract_Model.objects.get(pk=details_id)
    return render(request, 'May_4_app/Details.html',
    {'Details_get':Details_get})

def Home(request):
    Contracts_View = Contract_Model.objects.all()

    return render(request, 'May_4_app/Home.html',
    {'Contracts_View':Contracts_View})

def Add_Contract(request):
    Submitted = False
    if request.method == 'POST':
        The_form = Contract_forms(request.POST)
        if The_form.is_valid():
            The_form.save()
            return HttpResponseRedirect('/Add_Contract?Submitted=True')
    else:
        The_form = Contract_forms
        if 'Submitted' in request.GET:
            Submitted = True
    return render(request, 'May_4_app/Add_Contract.html',
    {'The_form':The_form, 'Submitted':Submitted})
