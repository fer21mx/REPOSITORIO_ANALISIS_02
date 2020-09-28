#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
with open ("synergy_logistics_database.csv", "r") as archivo_csv:
    contenido =csv.reader(archivo_csv)

    exportaciones = []
    importaciones = []
    for direction in contenido:
        if direction [1] == 'Exports':
            exportaciones.append(direction)
        elif direction [1] == 'direction':
            continue
        else:
            importaciones.append(direction)
        
    # Rutas de exportación:
    def contador_de_rutas(lista):
        rutas = []
        contador_de_rutas = []
        contador = 0
        texto_1 = [('La ruta que tiene origen en'), ('y destino a '), ('ha sido demandada '), ('veces.')] 
        for ruta in lista:
            ruta_actual = (ruta[2], ruta[3])
            if ruta_actual not in contador_de_rutas:
                for sen in lista:
                    if ruta_actual == (sen[2], sen[3]): 
                        contador += 1
                contador_de_rutas.append(ruta_actual)
                rutas.append((texto_1[0], ruta[2], texto_1[1],  ruta[3], texto_1[2],  contador, texto_1[3]))
                contador = 0 
                
        rutas.sort(key=lambda x : x[5], reverse=True)  
        las_mas_demandadas = []
        for x in rutas:
            if len(las_mas_demandadas) < 10:
                las_mas_demandadas.append(x)
            else:
                break
            
        return las_mas_demandadas

                      
    # Medios de transporte.
    def best_transport (listas):        
         transportes = []
         contador_de_transportes = []
         contador = 0 
         texto = [('El transporte por '), ('tuvo'), ('demandas')]
         for trans_mode in listas:
             actual_transpor = (trans_mode[7])
             if actual_transpor not in contador_de_transportes:
                for mode in listas:
                    if actual_transpor == (mode[7]):
                        contador += 1
                        
                contador_de_transportes.append(actual_transpor)
                transportes.append((texto[0], trans_mode[7], texto[1], contador, texto[2]))
                contador = 0
                
         transportes.sort(key=lambda x : x[1], reverse=True)
         return transportes
        
    def valor_trans (listax):
        trans_solitarios = []
        for x in listax:
            if x[7] not in trans_solitarios:
                trans_solitarios.append(x[7])
            elif x[7] == 'transport_mode':
                continue
        conteo = 0
        trans_valor = []
        texto = [('El transporte por '), ('generó un valor a la empresa de: ')]
        for w in trans_solitarios:
            for p in listax:
                if w == p[7]:
                    conteo += int(p[9])
                    r = (w, conteo)
            trans_valor.append((texto[0], r[0], texto[1], r[1]))
            conteo = 0
        trans_valor.sort(key=lambda  x : x[3], reverse=True) 
        return trans_valor
    
    # Mejores valores.        
    def lista_value(listaa):
        lista_valores = []
        suma_total = []
        for valor in listaa:
            lista_valores.append(int(valor[9]))
            
        suma_total = sum(lista_valores)
        ochenta_porciento = (suma_total * 0.8)
        
        paises_solitarios = []
        for x in listaa:
            if x[2] not in paises_solitarios:
                paises_solitarios.append(x[2])
            elif x[2] == 'origin':
                continue
            
        conteo = 0
        paises_valor = []
        
        for u in paises_solitarios:
            for j in listaa:
                if u == j[2]:
                    conteo += int(j[9])
                    g = (u, conteo)
            paises_valor.append(g)
            conteo = 0
        
        paises_valor.sort(key=lambda x : x[1], reverse=True)
        
        paises_80_porciento = []
        contador = 0
        for o in paises_valor:
            if o[0] not in paises_80_porciento and int(contador) < ochenta_porciento:
                contador += int(o[1])
                paises_80_porciento.append(o[0])
        
       
        impresion_paises = [('Los países que representan el 82 % del valor total son: ', paises_80_porciento, 'generando un valor en conjunto de:')]
        impresion_paises.append(contador)
        return impresion_paises
    
    
    print('Bienvenido a Synergy logistics database')
    Pregunta_1 = input('¿Quieres ir al  Menú? ')
    if Pregunta_1 == 'Sí':
        print('Las diez rutas más demandadas')
        print('Medios de transporte más importantes')
        print('Países generadores del 80 % del valor de las exportaciones')
        Pregunta_2 = input('¿Qué quieres ver? ')
        if Pregunta_2 == 'Las diez rutas más demandadas':
            print('Exportaciones')
            print('Importaciones')
            Pregunta_3 = input('Selecciona una variante: ')
            if Pregunta_3 == 'Exportaciones':
                print(contador_de_rutas(exportaciones))
            elif Pregunta_3 == 'Importaciones':
                print((contador_de_rutas(importaciones)))

            else:
                print('Lo sentimos, revisa tu ortografía y vuelve a cargar el código')
        elif Pregunta_2 == 'Medios de transporte más importantes':
            print('Exportaciones')
            print('Importaciones')
            Pregunta_4 = input('Selecciona una variante ')
           
            if Pregunta_4 == 'Exportaciones':
                Pregunta_4_1 = ('¿Qué quieres saber? ')
                print()
                print('Demanda de cada transporte')
                print('Valor adquirido de cada método de transporte')
                Pregunta_4_2 = input('¿Qué quieres saber? ')
                if Pregunta_4_2 == 'Demanda de cada transporte':
                    print(best_transport(exportaciones))
                elif Pregunta_4_2 == 'Valor adquirido de cada método de transporte':
                    print(valor_trans(exportaciones) )
                else:
                    print('Lo sentimos, revisa tu ortografía y vuelve a cargar el código')
            elif Pregunta_4 == 'Importaciones':
                print('Demanda de cada transporte')
                print('Valor adquirido de cada método de transporte')
                Pregunta_4_1 = input('¿Qué quieres saber? ')
                
                if Pregunta_4_1 == 'Demanda de cada transporte':
                    print(best_transport(importaciones))
                elif Pregunta_4_1 == 'Valor adquirido de cada método de transporte':
                    print(valor_trans(importaciones) )
                else:
                    print('Lo sentimos, revisa tu ortografía y vuelve a cargar el código')
        elif Pregunta_2 == 'Países generadores del 80 % del valor de las exportaciones':
            print('Exportaciones')
            print('Importaciones')
            print()
            Pregunta_5 = input('Selecciona una variante: ')
            
            if Pregunta_5 == 'Exportaciones':
                print(lista_value(exportaciones))
            elif Pregunta_5 == 'Importaciones':
                print(lista_value(importaciones))
            
            else:
                print('Lo sentimos, revisa tu ortografía y vuelve a cargar el código')
            

    elif Pregunta_1 == 'No':
        print('Lo sentimos, si buscas algo, aquí no lo encontrarás')
    else:
        print('Lo sentimos, solo puedo leer un "Sí" o es su defecto, un "No", revisa tu ortografía e inténtalo nuevamente')
    print()
    print('Gracias por tu visita, si quieres seguir investigando, vuelve a cargar la página.')

        