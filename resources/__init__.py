import numpy as np
import scipy.fftpack as fourier
import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def get_fourier(time : str, count : str, data):
    """
        devuelve el apellido con el nombre
    """

    t = time
    cantidad = count

    Ts = float(t)/int(cantidad)      # Definimos un tiempo y frecuencia de muestreo
    Fs=1/Ts

    x = np.array(data)
    leng = len(x)
    n = 1*np.arange(0, leng)

    gk = fourier.fft(x)            # Calculamos la FFT
    M_gk = abs(gk) /1000
    M_gk_len = len(M_gk)//8
    M_gk =M_gk[0:M_gk_len - 1]
    print(type(M_gk), M_gk_len)    # Calculamos la Magnitud de la FFT

    F = Fs*np.arange(0, len(x))/len(x)
    F = F[0:M_gk_len - 1]            # Definimos el Vector de Frecuencias
    list_f = list(F)
    lis_mk = list(M_gk)

    return json.loads(json.dumps({'amplitud': list(data), 'timepo': list(n), 'frecuencia': list_f, 'amplitud_fft': lis_mk }, cls=NpEncoder))


def get_alert(amplitud : list, freceuncia : list):
    """
        devuelve el apellido con el nombre
    """
    alarma = {}

    return 'alerta'
