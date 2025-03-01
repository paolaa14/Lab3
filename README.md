En este laboratorio se realizó un evento tipo coctel en una aula insonorizada, se instalaron varios micrófonos en distintos lugares para escuchar inicialmente el ruido ambiente, posterior se grabaron las voces de 2 sujetos para saber que era lo que estaban diciendo; una vez terminó la fiesta, se solicitó a los ingenieros que entregaran el audio de la voz de uno de los participantes.

Posterior , se analizaron las voces grabadas por los microfonos que eran mezclas de señales que provenían de diferentes fuentes (personas) para todos los casos y se encontraron con el problema de aislar la voz de interés. El problema de la "fiesta de cóctel" se refiere a la capacidad de un sistema para concentrarse en una sola fuente sonora mientras filtra las demás en un entorno con múltiples emisores de sonido. Este problema es común en sistemas de audición tanto humanos como artificiales, y su resolución es esencial enaplicaciones como la mejora de la voz, el reconocimiento de habla y la cancelación de ruido.
Para este laboratorio,se recreó el problema de la fiesta de coctel, donde existen 2 fuentes sonoras capturadas por un arreglo de 3 micrófonos de acuerdo con la siguiente metodología.




1. Configuración del sistema:

1.1. Se conectaron los 3 micrófonos al sistema de adquisición de datos y se distribuyeron de una forma estratégica en la sala insonorizada. Los micrófonos estaban ubicados de manera que cada uno capturó diferentes combinaciones de las señales provenientes de las dos fuentes, tal como se evidenciará en la imagen 1.


Imagen 1. Organizacion microfonos;
![WhatsApp Image 2025-02-27 at 20 49 38](https://github.com/user-attachments/assets/e4d0c5e3-a3f4-42c0-b970-86eeedc8014b)


Se ubicaron dos personas en posiciones fijas dentro de la sala insonorizada (una en cada extremo). Es importante mencionar que estaban localizados a distancias diferentes y orientados en distintas direcciones para simular un entorno de "fiesta de cóctel".


Es importante destacar, que como se evidencia en la imagen 1, los microfonos implementados son de tipo apple, el cual posee distintas características que interfieren en las señales que se observarán más adelante, los dispositivos apple que implementamos poseen una frecuencia de muestreo de 44.1 kHz o de 48 KHz. Asimismo, el sistema de adquisición  es de digitalización, es decir que en esta práctica de laboratorio se diseñó para que logrará capturar las señales de voz en un entorno que a pesar de ser insonorizado se escucha ruido de ambiente, donde de la misma manera para el tiempo de la captura fue de aproximadamente 15 segundos por audio, también  se calculará el snr midiendo el ruido en la sala con los tres micrófonos.


2. Captura de la señal:

2.1.Se generó la señal mediante la voz de los dos sujetos de prueba; cada uno dijo  una frase diferente durante el tiempo de captura de la señal (aproximadamente 15 segundos). Las señales de los micrófonos deben ser registradas por el sistema de adquisición y guardas para ser analizadas, lo que se evidencia en la imagen 2, donde se observa la señal de voz de Paola junto con las señales de Andrea y el ruido en el dominio del tiempo. Se aprecia una superposición entre las señales, lo que sugiere que la separación de fuentes es necesaria para extraer la voz de interés.


imagen 2; señales voz y ruido en el dominio del tiempo


<img width="624" alt="Figure 2025-02-27 201341 (0)" src="https://github.com/user-attachments/assets/76ce681d-3fb2-4b10-9c40-a171a967fe9a" />

2.2. Se grabo el ruido de la sala que en nuestro caso fue un salón insonorizado, con 3 micrófonos distintos (como se observó previamente en la imagen 1), donde es importante mencionar que los audios del ruido ambiente y la voz de paola y andrea, se encuentran en la parte inicial de este trabajo, es decir, que si desean escuchar los audios los pueden descargar, esto se hizo con el fin de mostrar la práctica simultanemanete a la explicación. A partir de esto, se quería calcular el SNR de cada señal (cada voz se le saco una señal), lo cual se obversavará en la imagen 3, más adelante.



- Antes de continuar se debe aclarar;

Para correr el codigo y que funcione correctamente se deben descargar ciertas cosas, inicialmente en la consola de spyder se deben descargar librerías de la siguiente manera; pip install numpy matplotlib wfdb scipy, estas son para;

- import numpy as np: es para que permita correr cálculos númericos y arrays en caso de tenerlos.
- import matplotlib.pyplot as plt :grafica señales de audio y transformaciones, como espectros de frecuencia
- import scipy.io.wavfile as wavfile ; lee archivos en formato WAV, Con wavfile.read() se cargan  archivos WAV y se obtiene su frecuencia de muestreo y los datos.
-from scipy.fftpack import fft; Importa la Transformada Rápida de Fourier (FFT), que se usa para convertir una señal del dominio del tiempo al dominio de la frecuencia.
- from sklearn.decomposition import FastICA; implementa el Análisis de Componentes Independientes (ICA), que se usa para separar señales mezcladas (más adelante lo veremos).
- import sounddevice as sd; permite la grabación y reproducción de audio en tiempo real, se usa para capturar sonido desde un micrófono o reproducir audio procesado.
- from scipy.signal import butter, filtfilt; se usa para diseñar y aplicar filtros (como el que usaremos más adelante), butter();  crea un filtro Butterworth, que es un tipo de filtro pasa-bajos, pasa-altos, pasa-banda, etc y filtfilt() aplica el filtro a una señal sin introducir desfases.

 

Con estas librerias descargadas, se procedió a calcular el SNR, el código calcula el SNR de cada señal  antes y después del filtrado  ,que se usa para medir como se encuentra la señal o mas bien la calidad de esta, este cálculo se realiza de la siguiente manera; 

  ¨def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)  # Potencia promedio de la señal
    noise_power = np.mean(noise ** 2)    # Potencia promedio del ruido
    snr = 10 * np.log10(signal_power / noise_power)  # Cálculo del SNR en dB
    return snr ¨

 y los resultados se evalúan con el criterio:
-SNR < -10 dB → Mala calidad.
-SNR entre 10 y 20 dB → Aceptable.
-SNR > 20 dB → Excelente calidad.

En la imagen a continuación se observan los valores obtenidos;

Imagen 3; SNR antes y después del filtrado


<img width="574" alt="Captura de pantalla 2025-02-27 a la(s) 8 14 59 p m" src="https://github.com/user-attachments/assets/6280e28b-ebdd-48a6-94cf-63aedf5c8b82" />


Teniendo en cuenta esto, la voz de andrea pasó de 22.97 dB , a 40.58 dB, lo que indica una mejora significativa  de las claridad de la señal, y la voz de paola pasó de 23.08 dB a 40.67dB, lo que evidencia una mejoría muy alta.

Para conluir la parte del SNR, antes de realizar el  filtrado, el SNR estaba en un rango aceptable (~23 dB), indicando que la señal tenía una calidad moderada, no obstante después del filtrado, el SNR aumentó a más de 40 dB, lo que indica una calidad excelente en la separación y limpieza de la señal, por lo que el método de separación de señales demuestra su efectividad en mejorar la señal capturada.



  
