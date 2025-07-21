import requests
def get_weather(city:str)-> str:#Tipo de dato strip
    base_url = f"https://wttr.in/{city}?format=%t" #f"" de format
    response = requests.get(base_url)#metodo get
    
    if response.status_code == 200:#Información del servidor funciona "200"
        return response.text.strip()#el return guarda el dato y lo muestra en donde uno quiere y print("") lo muestra en la terminal
    else:
        return "No se pudo obtener información del clima de su ciudad, intentelo mas tarde"
print(get_weather('cusco'))

def frase_1():
    base_url = f"https://zenquotes.io/api/random"
    response = requests.get(base_url)
    
    if response.status_code == 200:#Información del servidor funciona "200"
        return  response.text.strip()
        
    else:
        return "No se pudo obtener información del clima de su ciudad, intentelo mas tarde"
print(frase_1())    
