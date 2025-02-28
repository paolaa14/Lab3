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

2.1. Se generó la señal mediante la voz de los dos sujetos de prueba; cada uno dijo  una frase diferente durante el tiempo de captura de la señal (aproximadamente 15 segundos). Las señales de los micrófonos deben ser registradas por el sistema de adquisición y guardas para ser analizadas, lo que se evidencia en las imagenes 2 y 3 es la señal generada mediante de la voz de las dos personas que se tomaron para la prueba,se utilizó la técnica de saparar señales para extraer cada señal de forma individual.

Es importante mencionar que la técnica de separación se llama análisis de componentes independientes (ICA), que basicamente recupera señales originales que surgen de una mezcla sin saber como se combinaron inicialmente, tal como se escucha en los audios, en el código en particular que desarrollamos se implementa ¨FastICA(n_components=3)¨ (significa que se requiere separar las tres señales), lo que se aplica a as tres señales (Voz Andrea, Ruido y Voz Paola) y para lograr sacar los commponentes independientes se utilizó la función fit_transform() (encuentra y extrae las fuentes independientes de la mezcla), es decir las voces y el ruido por aparte, las señales realizadas mediante la voz se evidenciarán en las imagenes 2,3 y 4.


imagen 2; voz andrea separado
<img width="617" alt="Figure 2025-02-27 201341 (1)" src="https://github.com/user-attachments/assets/91ba2eda-bd65-4977-9e17-84e02e79d9cb" />
En esta gráfica es importante mencionar que, se  observa una señal con variaciones claras en amplitud, lo que indica la presencia de segmentos con mayor energía (palabras enfatizadas) y pausas naturales entre palabras, también observamos que la señal parece tener una buena relación señal/ruido (SNR), ya que las variaciones de amplitud son más significativas en comparación con el ruido de fondo y  asu vez, no se observan patrones repetitivos ni artefactos evidentes de interferencia, lo que sugiere una buena separación de la voz, resaltando que si después del filtrado el SNR es más de 20 dB la estracción fue buena y si es inferior a 10 dB la señal aún tiene ruido, pero esto lo veremos en el ítem 3, ya que ahora solo estamos observando la señal separada.


Imagen 3; voz paola separada
<img width="608" alt="Figure 2025-02-27 201341 (5)" src="https://github.com/user-attachments/assets/0fb7fcdc-3ad0-471f-a5cf-e8ae4b191057" />
En esta gráfica es importante mencionar que, la forma de onda tiene características similares a la de Andrea, pero con diferencias en el patrón de amplitud y en la duración de los segmentos hablados, observamos que la señal ha sido correctamente aislada, ya que no se observan rastros significativos de la voz de Andrea ni del ruido ambiental, de la misma manera hay partes de menor amplitud, lo que podría deberse a una diferencia en la intensidad de la voz del hablante o a la posición relativa del micrófono.


Imagen 4; ruido separado
<img width="614" alt="Figure 2025-02-27 201341 (3)" src="https://github.com/user-attachments/assets/55168d99-e83a-4ec0-99ba-6219cda7687e" />
En esta gráfica es importante mencionar que, el ruido separado muestra una señal más uniforme, sin grandes variaciones de amplitud como en las señales de voz, también se pueden notar picos en ciertos momentos, lo que podría deberse a sonidos externos como movimientos de objetos o ecos en la sala.
La energía del ruido parece distribuida a lo largo de toda la señal sin pausas marcadas, lo cual es característico de un ruido de fondo constante.



Para continuar, se implementa un  filtro Butterworth pasa banda (se implementa este filtro porque despues de separarla con la técnica mencioanda la señal puede tener frecuencias no deseadas) para mejorar la calidad de las señales de voz y se definieron frecuencias de corte entre los 300 Hz Y 3400 Hz (que es el rango de frecuencias de la voz humana), que quiere decir que permitirá eliminar el ruido fuera del espectro típico del habla de nuestras voces, respecto al código se implementa  ¨butter_bandpass()¨, con frecuencia de corte baja ; 300 Hz y la frecuencia de corte alta 3.400 Hz y se aplica con apply_filter() usando scipy.signal.filtfilt(), que evita distorsiones en la señal filtrada, es necesario mencionar que este filtrado permitirá mejorar la calidad de la voz al eliminar el ruido de baja y alta frecuencia, por lo que el SNR que se obtendrá será mucho mejor después de la separación.

Posterior,  se utiliza la Transformada Rápida de Fourier para visualizar el espectro de las señales separadas y filtradas verificando si las señales están correctamente aisladas y si el ruido ha sido reducido, asimismo, el código calcula el SNR de cada señal  antes y después de la separación, para medir la mejora en la calidad de la extracción de voz, esto se realiza con la función ¨calculate_snr()¨ que compara la  energía de la señal con la del ruido para determinar la efectividad del proceso de separación.


Es importante tener en cuenta que; si el SNR de las señales de voz es alto, la separación fue exitosa y las grabaciones son aptas para el análisis, mientras que si el SNR es bajo, pueden existir problemas relacionados a la mala posición de los microfonos que generaría una mala captura, o un error en la segmentación de las fuentes  que llevaría a que las voces no se separen correctamente.




3. en
4. em




Imagen 2; espectro de voz paola filtrada;
<img width="625" alt="Figure 2025-02-27 201341 (10)" src="https://github.com/user-attachments/assets/2ae8f0ec-8258-43d5-94d5-e2da7e5c949d" />

Imagen 3;voz paola filtrada;
<img width="608" alt="Figure 2025-02-27 201341 (9)" src="https://github.com/user-attachments/assets/70b9ae11-659a-48f0-833a-50c677e336bc" />


Imagen 4;espectro de voz andrea filtrada;
<img width="625" alt="Figure 2025-02-27 201341 (8)" src="https://github.com/user-attachments/assets/9f4443cf-b787-4bf2-b72d-5ab6f1bae626" />


Imagen 5; voz andrea filtrada;
<img width="608" alt="Figure 2025-02-27 201341 (7)" src="https://github.com/user-attachments/assets/7826d6f2-7dbb-454a-b6d4-f1afee2f8911" />

imagen 6; espectro voz paola separada
<img width="625" alt="Figure 2025-02-27 201341 (6)" src="https://github.com/user-attachments/assets/3e63f054-b406-4709-b55d-37a5822d7dd3" />

Imagen 8; espectro ruido separado
<img width="625" alt="Figure 2025-02-27 201341 (4)" src="https://github.com/user-attachments/assets/d26c3507-1ff7-4afc-8126-3b29222e892f" />



Imagen 10; espectro voz andrea separado
<img width="625" alt="Figure 2025-02-27 201341 (2)" src="https://github.com/user-attachments/assets/122691e9-ff2d-44b4-8760-93a76b0f2c41" />


imagen 12; señales voz y ruido en el dominio del tiempo
<img width="624" alt="Figure 2025-02-27 201341 (0)" src="https://github.com/user-attachments/assets/76ce681d-3fb2-4b10-9c40-a171a967fe9a" />


Imagen 13; SNR antes y después del filtrado
<img width="574" alt="Captura de pantalla 2025-02-27 a la(s) 8 14 59 p m" src="https://github.com/user-attachments/assets/6280e28b-ebdd-48a6-94cf-63aedf5c8b82" />






5. Preguntas finales refuerzo de aprendizaje;

Con esta práctica se espera que como estudiantes logreemos reproducir  por separado el audio de cada una de las voces capturadas a partir de la obtención de dos señales con dos voces mezcladas.
     5.1 .Los estudiantes serán capaces de responder las siguientes preguntas:
      5.2. ¿Cómo afecta la posición relativa de los micrófonos y las fuentes sonoras en la
            efectividad de la separación de señales?
          5.3. ¿Qué mejoras implementaría en la metodología para obtener mejores
                resultados?





