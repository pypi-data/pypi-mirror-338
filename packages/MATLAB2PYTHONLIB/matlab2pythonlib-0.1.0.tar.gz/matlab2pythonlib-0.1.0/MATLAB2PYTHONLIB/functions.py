# Archivo con tus funciones

import datetime
import numpy as np

def datenum_to_date(datenum):
    """Lee el formato datenum de matlab (numeros de orden 7XXXXX) y los cambia a un string de fecha en formato YYYY-MM-DD-HH-mm.
    Por lo general los datos datenum vienen desde un archivo netCDF generado por matlab por lo que pueden venir como un Masked Array.
    Esta Funcion utiliza las librerías datetime y numpy para poder hacer la conversión de fechas."""
    # Primero convierte el maskedArray en un array normal de python
    if isinstance(datenum, np.ma.MaskedArray):
        fechas = np.array(datenum.filled(np.nan))
    else:
        fechas = np.array(datenum)

    # Lista para almacenar las fechas convertidas
    fechas_convertidas = []
    
    for idatenum in fechas.flatten():
         # Conversion de idatenum a un valor escalar
        idatenum = float(idatenum)

        # Convierte un número datenum de MATLAB a datetime de Python
        fecha = datetime.datetime.fromordinal(int(idatenum)) + datetime.timedelta(days=idatenum % 1) - datetime.timedelta(days=366)
        #fechas_convertidas.append(fecha)

        # Redondear al minuto más cercano
        fecha = fecha.replace(microsecond=0)
        if fecha.second >= 30:
            fecha += datetime.timedelta(minutes=1)
        
         # Formatea la fecha a string
        fecha_str = fecha.strftime('%Y-%m-%d-%H-%M')
        fechas_convertidas.append(fecha_str)

    # Retorna las fechas convertidas como un array de numpy
    return np.array(fechas_convertidas)