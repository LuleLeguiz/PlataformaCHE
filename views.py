from django.http import HttpResponse
from django.shortcuts import render

def Passenger(request):
    #passenger = passenger(name= "Silvio", last_name= "Rodriguez", destination="Argentina")
    #passenger.save()
    #Doct_Txt = f'---> Nombre: {passenger.name}, Apellido: {passenger.last_name}, Destino: {passenger.destination}'

    return render(request, 'AppChe\passenger.html')

def BusCompany(request):
    #name = name(bus_name='Tropic Bus', bus_destination='Argentina, Paraguay, Brasil')
    #name.save()
    #Doct_Txt = f'---> Empresa: {name.bus_name}, Destino: {name.bus_destination}'
    
    return render(request, 'AppChe\bus_company.html')


def BusInfo(request):
    #seats = seats(seats_number= '35', seats_type= 'Semi Cama')
    #seats.save()
    #Doct_Tct = f'---> Cantidad de Asientos: {seats.seats_number}, Tipos de Asientos: {seats.seats_type}'
    
    return render(request, 'AppChe\bus_info.html')
