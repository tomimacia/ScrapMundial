from requests_html import HTMLSession
import datetime
# Si no lo tenes, tenes que mandar pip install requests-html

now = datetime.datetime.now()

s = HTMLSession()

file = open("data.txt", "w")

url = "https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/date/product/101397570845/lang/en"

r = s.get(url)

# Aca en elegir tenes que poner los partidos que queres buscar por numero(sin la M),
# por ejemplo los de argentina son 8, 24 y 39 (M8, M24 y M39)

elegir = [8, 24, 39]
partidosElegidos = []
partidosTotales = []

partidosHTML = r.html.find('div.perf_details')

for partidoHTML in partidosHTML:
    partidosTotales.append(partidoHTML.text)


def AñadirPartidos():
    i = 0
    while i < len(elegir):
        partidosElegidos.append(partidosTotales[elegir[i] - 1])
        i += 1


# Consulta los datos y los imprime por consola, y manda todo mas detallado al data.txt(va sobreescribiendo)

def consultarPartidos():
    file.write('Time: ' + now.strftime('%H:%M:%S\n\n'))
    print('Time: ' + now.strftime('%H:%M:%S\n'))
    i = 0
    while i < len(partidosElegidos):
        file.write(partidosElegidos[i]+"\n\n")
        if partidosElegidos[i].find("Currently unavailable") != -1:
            print(f"Partido {elegir[i]} no disponible")
            i += 1
        else:
            print(f"Partido {elegir[i]} disponible")
            i += 1


AñadirPartidos()
consultarPartidos()
