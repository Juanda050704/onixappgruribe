import csv

def crearCSV(lista,nombreCSV,encabezados):
    with open('data/'+nombreCSV,mode='w',newline='',encoding='utf-8') as archivo_csv:
        writer=csv.writer(archivo_csv)
        writer.writerow(encabezados)
        writer.writerows(lista)