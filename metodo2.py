import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from sklearn.decomposition import PCA
import sounddevice as sd
from scipy.signal import butter, filtfilt


# Función para aplicar un filtro pasa banda
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    return filtfilt(b, a, data)

# Función para calcular SNR
def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Cargar los archivos de audio
fs1, voz_andrea = wavfile.read('Voz%20Andrea.wav')
fs2, ruido = wavfile.read('RuidoAmbiente.wav')
fs3, voz_paola = wavfile.read('Voz%20Paola.wav')

# Normalizar las señales
voz_andrea = voz_andrea.astype(np.float32) / np.max(np.abs(voz_andrea))
ruido = ruido.astype(np.float32) / np.max(np.abs(ruido))
voz_paola = voz_paola.astype(np.float32) / np.max(np.abs(voz_paola))

# Encontrar la longitud mínima entre las señales
min_length = min(len(voz_andrea), len(ruido), len(voz_paola))

# Recortar las señales a la misma longitud
voz_andrea = voz_andrea[:min_length]
ruido = ruido[:min_length]
voz_paola = voz_paola[:min_length]

# Calcular SNR antes de la separación
snr_voz_andrea = calculate_snr(voz_andrea, ruido)
snr_voz_paola = calculate_snr(voz_paola, ruido)
print(f'SNR antes de la separacion - Voz Andrea: {snr_voz_andrea:.2f} dB')
print(f'SNR antes de la separacion - Voz Paola: {snr_voz_paola:.2f} dB')

# Graficar las tres señales juntas en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(voz_andrea)) / fs1, voz_andrea, color='blue', label='Voz Andrea')
plt.plot(np.arange(len(ruido)) / fs2, ruido, color='red', alpha=0.6, label='Ruido')
plt.plot(np.arange(len(voz_paola)) / fs3, voz_paola, color='cyan', label='Voz Paola')
plt.title('Señales de Voz y Ruido en el Dominio del Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)
plt.legend()
plt.show()

# Aplicar PCA para separar las señales
mezcla = np.vstack((voz_andrea, ruido, voz_paola)).T
pca = PCA(n_components=3)
separadas = pca.fit_transform(mezcla)

# Determinar la componente más correlacionada con la voz de Paola
correlaciones_paola = [np.corrcoef(separadas[:, i], voz_paola)[0, 1] for i in range(3)]
indice_paola = np.argmax(np.abs(correlaciones_paola))

# Determinar la componente más correlacionada con la voz de Andrea
correlaciones_andrea = [np.corrcoef(separadas[:, i], voz_andrea)[0, 1] for i in range(3)]
indice_andrea = np.argmax(np.abs(correlaciones_andrea))

# Aplicar filtro a las señales de voz
lowcut = 300  # Frecuencia de corte baja en Hz
highcut = 3400  # Frecuencia de corte alta en Hz
voz_paola_filtrada = apply_filter(separadas[:, indice_paola], lowcut, highcut, fs1)
voz_andrea_filtrada = apply_filter(separadas[:, indice_andrea], lowcut, highcut, fs1)

# Definir nombres y colores para las componentes separadas
senales_originales = [voz_andrea, ruido, voz_paola]
componentes = ['Voz Andrea Separada', 'Ruido Separado', 'Voz Paola Separada']
colores = ['blue', 'red', 'cyan']

# Usar 'separadas' en lugar de 'senales_ordenadas'
for i in range(3):
    plt.figure(figsize=(10, 4))
    plt.plot(np.arange(len(separadas[:, i])) / fs1, separadas[:, i], color=colores[i], label=componentes[i])
    plt.title(componentes[i])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # Calcular la FFT de la señal separada
    N = len(separadas[:, i])
    freqs = np.fft.fftfreq(N, 1/fs1)
    X = np.abs(fft(separadas[:, i]))
    
    # Graficar el espectro
    plt.figure(figsize=(10, 4))
    plt.semilogx(freqs[:N//2], X[:N//2], color=colores[i])
    plt.title(f'Espectro de {componentes[i]}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.show()

# Graficar señales filtradas y sus espectros
senales_filtradas = [voz_andrea_filtrada, voz_paola_filtrada]
componentes_filtradas = ['Voz Andrea Filtrada', 'Voz Paola Filtrada']
colores_filtradas = ['blue', 'cyan']

for i in range(2):
    plt.figure(figsize=(10, 4))
    plt.plot(np.arange(len(senales_filtradas[i])) / fs1, senales_filtradas[i], color=colores_filtradas[i], label=componentes_filtradas[i])
    plt.title(componentes_filtradas[i])
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # Calcular la FFT de la señal filtrada
    N = len(senales_filtradas[i])
    freqs = np.fft.fftfreq(N, 1/fs1)
    X = np.abs(fft(senales_filtradas[i]))
    
    # Graficar el espectro filtrado
    plt.figure(figsize=(10, 4))
    plt.semilogx(freqs[:N//2], X[:N//2], color=colores_filtradas[i])
    plt.title(f'Espectro de {componentes_filtradas[i]}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.show()
    
# Calcular SNR después del filtrado
snr_voz_andrea_filtrada = calculate_snr(voz_andrea_filtrada, ruido)
snr_voz_paola_filtrada = calculate_snr(voz_paola_filtrada, ruido)
print(f'SNR después de la separacion - Voz Andrea: {snr_voz_andrea_filtrada:.2f} dB')
print(f'SNR después de la separacion - Voz Paola: {snr_voz_paola_filtrada:.2f} dB')

# Reproducir la señal filtrada correspondiente a la voz de Paola
sd.play(voz_paola_filtrada, samplerate=fs1)
sd.wait()

