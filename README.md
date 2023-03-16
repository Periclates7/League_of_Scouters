![Banner](https://github.com/Periclates7/League_of_Scouters/blob/main/img/banner.png)
  
# LEAGUE OF SCOUTERS 🏆🎮
  
El presente proyecto es el proyecto final que se ha entregado en marzo de 2023 a la finalización del Bootcamp en Data Analytics cursado en la escuela tecnológica Ironhack.
  
League of Scouters es una plataforma diseñada para ayudar a los equipos profesionales de League of Legends a encontrar jugadores con potencial para fichar. La plataforma utiliza datos y estadísticas para identificar a los jugadores que destacan en su juego y que podrían tener un buen desempeño en un entorno profesional. Esto permite a los equipos encontrar y contratar a nuevos talentos de manera más efectiva, lo que puede llevar a un mayor éxito en el ámbito competitivo.
  
## 🎯 OBJETIVOS DEL PROYECTO 
  
1. Crear un repositorio en GitHub con una buena organización de los recursos.
2. Extraer los datos de manera óptima.
3. Aplicar herramientas, técnicas y metodologías para la limpieza de datos acordes a nuestras necesidades:
    - Filtrado de los datos extraidos
    - Exploración del conjunto de los datos
    - Limpieza de valores nulos
    - Eliminación de duplicados
    - Transformación de diferentes conjuntos de datos
    - Librerías utilizadas: Pandas, Numpy, Selenium, Scipy, Pylab, Seaborn, Streamlit.
3. Analizar, Adecuar y etiquetar los datos.
4. Calcular y comparar similitudes entre jugadores profesionales y fugadores con potencial.
5. Visualizar los datos a través de Tableau.
6. Realizar un cuadro de mando intuitivo y operativo a través de Streamlit.
  
## ⛏ EXTRACCIÓN Y LIMPIEZA DE LOS DATOS
  
La extracción de datos se ha realizado a través de técnicas y metodologías propias del *web scraping* de la página [League of Graphs](https://www.leagueofgraphs.com/es/). Los datos resultantes son cualitativos y cuantitativos acerca del rendimiento en partida de los 5000 mejores jugadores de League of Legends en la presente temporada.
  
Las funciones creadas para realizar esta labor, incluyen procesos de limpieza del dato. Es por esto que el proceso de limpieza de los datos fue breve y efectivo.
  
## 🔎 ANÁLISIS DE LOS DATOS
  
Esta es la parte más importante del proyecto. Este proceso consistió en primer lugar en la codificación de todas las características categóricas con el fin de convertirlas en valores numéricos y así poder operar con estos valores. En este punto obtenemos un único *DataFrame* en el cual cada uno de sus registros forman un vector y por tanto ocupan una posición en el espacio. El siguiente paso consistió en el cálculo de la distancia y similitud de cada uno de los vectores con respecto al resto, de esta manera obtenemos un *score* el cual nos contará cuales son aquellos jugadores no profesionales que tienen potencial para serlo.
  
## 📊 REALIZACIÓN DEL CUADRO DE MANDO
  
Uno de los objetivos del presente proyecto es que las conclusiones halladas fueran accesibles para cualquier persona sin necesidad de entender acerca del manejo de datos. Es por esto que se ha construído un cuadro de mando el cual filtra a golpe de click los diferentes parámetros por rol, campeones más utilizados, estadísticas de los mejores jugadores o similitudes a jugadores profesionales.

La aplicación se puede desplegar ubicándose en la carpeta principal del presente repositorio y ejecutando en terminal el siguiente código:
  
```
$ streamlit run League_of_scouters.py
```

