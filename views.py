from django.http import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from .models import System

# Create your views here.

def redirect_home(request):
    return redirect('home/')


def home(request):
    return render(request, 'home.html')


def latenciaCliente(request):
    classe = System()
    latenciaCliente = classe.getLatenciaCliente()
    array = []
       
    for object in latenciaCliente:
        array.append(object["latencia"]) 

    media = int(round((sum(array)/len(array)), 0)) 
    maxima = max(array)
    minima = min(array)    
          
    return render(request, 'latenciaCliente.html', {"media": media, "max": maxima, "min": minima})

    
def returnLatenciaCliente(request) -> list:
    '''Retorna a media da latencia de cada mês'''
    classe = System()
    latenciaCliente = classe.getLatenciaCliente()
    array = []
    medias = []
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', ]
    for mes in range(12):
        for object in latenciaCliente:
            dias = 0
            if object['data'][5:7] == meses[mes]:
                array.append(object['latencia'])
                dias += 1

        medias.append(round((sum(array) / len(array)), 2))
        array.clear()

    return JsonResponse({'latenciaClienteArray': medias})


def falhas(request):
    classe = System()
    falhas = classe.getFalhas()
    array = []
           
    for object in falhas:
        for n in range(object["quantidade_falha"]):
            array.append(object["tipo_falha"]) 

    servidor_indisponivel_count = array.count('Servidor indisponível')
    time_out_count = array.count('Erro 408 (tempo excedido)')
    api_indisponivel_count = array.count('API pagamento indisponível')
    total_falhas = servidor_indisponivel_count + time_out_count + api_indisponivel_count

    array_count = [servidor_indisponivel_count, time_out_count, api_indisponivel_count]
    dict = {servidor_indisponivel_count: 'Servidor indisponível', time_out_count: 'Erro 408 (tempo excedido)', api_indisponivel_count: 'API pagamento indisponível'}
    numero_maior_ocorrencia = max(array_count)
    falha_maior_ocorrencia = dict.get(numero_maior_ocorrencia)
          
    return render(request, 'falhas.html', {"total": total_falhas, "maior_ocorrencia":  falha_maior_ocorrencia})


def returnFalhas(request):
    classe = System()
    falhas = classe.getFalhas()
    array = []

    for object in falhas:
        for n in range(object['quantidade_falha']):
            array.append(object['tipo_falha'])

    servidor_indisponivel_count = array.count('Servidor indisponível')
    time_out_count = array.count('Erro 408 (tempo excedido)')
    api_indisponivel_count = array.count('API pagamento indisponível')

    return JsonResponse({'servidor_indisponivel': servidor_indisponivel_count, 'time_out': time_out_count, 'api_indisponivel': api_indisponivel_count})


def ataques(request):
    classe = System()
    ataques = classe.getAtaques()
    array = []
    

    for object in ataques:
        for n in range(object['quantidade']):
            array.append(object['tipo_ataque'])

    ddos_count = array.count('DDoS')
    dos_count = array.count('DoS')
    spoofing_count = array.count('Spoofing')
    exploits_count = array.count('Exploits')
    total_ataques = ddos_count + dos_count + spoofing_count + exploits_count

    array_count = [ddos_count, dos_count, spoofing_count, exploits_count]
    dict = {ddos_count: 'DDoS', dos_count: 'DoS', spoofing_count: 'Spoofing', exploits_count: 'Exploits'}
    numero_maior_ocorrencia = max(array_count)
    ataque_maior_ocorrencia = dict.get(numero_maior_ocorrencia)

    return render(request, 'ataques.html', {"total": total_ataques, "maior_ocorrencia":  ataque_maior_ocorrencia})


def returnAtaques(request) -> list:
    classe = System()
    ataques = classe.getAtaques()
    array = []

    for object in ataques:
        for n in range(object['quantidade']):
            array.append(object['tipo_ataque'])

    ddos_count = array.count('DDoS')
    dos_count = array.count('DoS')
    spoofing_count = array.count('Spoofing')
    exploits_count = array.count('Exploits')

    return JsonResponse({'DDoS': ddos_count, 'DoS': dos_count, 'Spoofing': spoofing_count, 'Exploits': exploits_count})


def latenciaAPI(request):
    classe = System()
    latenciaAPI = classe.getLatenciaAPI()
    array = []
           
    for object in latenciaAPI:
        array.append(object["latencia"]) 

    media = int(round((sum(array)/len(array)), 0)) 
    maxima = max(array)
    minima = min(array) 
          
    return render(request, 'latenciaAPI.html', {"media": media, "max": maxima, "min": minima})


def returnLatenciaAPI(request) -> list:
    '''Retorna a media da latencia de cada mês'''
    classe = System()
    latenciaCliente = classe.getLatenciaAPI()
    array = []
    medias = []
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', ]
    for mes in range(12):
        for object in latenciaCliente:
            dias = 0
            if object['data'][5:7] == meses[mes]:
                array.append(object['latencia'])
                dias += 1

        medias.append(round((sum(array) / len(array)), 2))
        array.clear()

    return JsonResponse({'latenciaAPI': medias})


def usuarios(request):
    classe = System()
    usuarios = classe.getUsers()
    array = []

    for object in usuarios:
        array.append(object['cidade'])

    recife_count = array.count('Recife')
    joao_pessoa_count = array.count('João Pessoa')
    sjose_campos_count = array.count('São José dos Campos')
    curitiba_count = array.count('Curitiba')

    array_counts = [recife_count, joao_pessoa_count, sjose_campos_count, curitiba_count]
    dict = {recife_count: 'Recife', joao_pessoa_count: 'João Pessoa', sjose_campos_count: 'São José dos Campos', curitiba_count: 'Curitiba'}
    numero_cidade_com_maior_ocorrencia = max(array_counts)
    numero_cidade_com_menor_ocorrencia = min(array_counts)

    cidade_com_maior_ocorrencia = dict.get(numero_cidade_com_maior_ocorrencia)
    cidade_com_menor_ocorrencia = dict.get(numero_cidade_com_menor_ocorrencia)

    return render(request, 'usuarios.html', {'maior': cidade_com_maior_ocorrencia, 'menor': cidade_com_menor_ocorrencia})


def returnUsuarios(request):
    classe = System()
    usuarios = classe.getUsers()
    array = []

    for object in usuarios:
        array.append(object['cidade'])

    recife_count = array.count('Recife')
    joao_pessoa_count = array.count('João Pessoa')
    sjose_campos_count = array.count('São José dos Campos')
    curitiba_count = array.count('Curitiba')

    return JsonResponse({'recife': recife_count, 'joao_pessoa': joao_pessoa_count, 'sjose_campos': sjose_campos_count, 'curitiba': curitiba_count})



def novosUsuarios(request):
    classe = System()
    novosUsuarios = classe.getNovosUsuarios()
    array = []
           
    for object in novosUsuarios:
        array.append(object["quantidade_Novos_usuarios"]) 

    media = int(round((sum(array)/len(array)), 0)) 
    maxima = max(array)
    minima = min(array) 
          
    return render(request, 'novosUsuarios.html', {"media": media, "max": maxima, "min": minima})


def returnNovosUsuarios(request) -> list:
    '''Retorna a media de novos usuarios de cada mês'''
    classe = System()
    novosUsuarios = classe.getNovosUsuarios()
    array = []
    medias = []
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', ]
    for mes in range(12):
        for object in novosUsuarios:
            dias = 0
            if object['data'][5:7] == meses[mes]:
                array.append(object['quantidade_Novos_usuarios'])
                dias += 1

        medias.append(round((sum(array) / len(array)), 2))
        array.clear()

    return JsonResponse({'novosUsuarios': medias})


def acessos(request):
    classe = System()
    acessos = classe.getAcessos()
    array = []
           
    for object in acessos:
        array.append(object["quantidade_Acessos"]) 

    media = int(round((sum(array)/len(array)), 0)) 
    maxima = max(array)
    minima = min(array) 
          
    return render(request, 'acessos.html', {"media": media, "max": maxima, "min": minima})
    


def returnAcessos(request) -> list:
    '''Retorna a media de acessos de cada mês'''
    classe = System()
    acessos = classe.getAcessos()
    array = []
    medias = []
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', ]
    for mes in range(12):
        for object in acessos:
            dias = 0
            if object['data'][5:7] == meses[mes]:
                array.append(object['quantidade_Acessos'])
                dias += 1

        medias.append(round((sum(array) / len(array)), 2))
        array.clear()

    return JsonResponse({'acessos': medias})


def vendas(request):
    classe = System()
    vendas = classe.getVendas()
    array = []
           
    for object in vendas:
        array.append(object["quantidade_Vendas"]) 

    media = int(round((sum(array)/len(array)), 0)) 
    maxima = max(array)
    minima = min(array) 
          
    return render(request, 'vendas.html', {"media": media, "max": maxima, "min": minima})    


def returnVendas(request):
    '''Retorna a media de vendas de cada mês'''
    classe = System()
    vendas = classe.getVendas()
    array = []
    medias = []
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', ]
    for mes in range(12):
        for object in vendas:
            dias = 0
            if object['data'][5:7] == meses[mes]:
                array.append(object['quantidade_Vendas'])
                dias += 1

        medias.append(round((sum(array) / len(array)), 2))
        array.clear()

    return JsonResponse({'vendas': medias})

