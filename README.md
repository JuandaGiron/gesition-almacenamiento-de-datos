# Proyecto-gestion-almacenamiento-de-datos
Integrantes:
Alejandro Solano - Juan David Girón

Problematica

Analizar un conjunto de datos recopilados por la Secretaría de Seguridad de Cali durante 2020, el cual se centra en la criminalidad y la seguridad urbana en la ciudad. Este conjunto de datos no solo permite monitorear y analizar delitos en distintas comunas y barrios de la ciudad, sino que también puede integrarse con otras bases de datos relevantes, como registros policiales y datos sociodemográficos. Esto facilitaría la identificación de patrones y tendencias delictivas, así como la determinación de las zonas y momentos del día más propensos a la ocurrencia de crímenes. Al entender mejor la naturaleza de estos delitos, las autoridades pueden optimizar la asignación de recursos, diseñar estrategias de prevención más efectivas y enfocar los esfuerzos de seguridad, mejorando así la respuesta ante la criminalidad en Cali y por tanto disminuir la tasa de crimenes en la ciudad.

Para llevar a cabo el analisis se cuenta con un data de 8640 registros y 14 caracteristicas, la descripción de cada una de las variables se presenta a continuación:

ID= número consecutivo para llevar a cabo un control de los registros (entero)

Lugar= Espacio donde se llevo a cabo el delito, puede ser un espacio publico, domicilio, etc. (categórico)

Etapa= Describe si el delito se encuentra en algun tipo de proceso investigativo o judicial (categórico)

Mes= Mes en que ocurrió el delito (categórico)

Fecha= Fecha en la que se registro el delito año/mes/dia (date)

Dia= Dí de la semana que se presenta el delito (categórico)

Hora= Hora del día que se registro el hecho (time)

Usuario= Identificador de usuario sufrió el delito (categórico)

ID_barrio= Identificador númerico del barrio donde ocurrio el delito (entero)

Barrio1= Nombre del barrio donde se registro el crimen (caregórico)

Comuna= Número de la comuna donde se registro el delito (entero)

Estrato= Estrato socioeconomico del lugar donde se llevo a cabo el delito (entero)

Hora1= Hora del dia que se registro el hecho (time)

Hora_r = Hora redondeada para establecer intervalos de tiempo (entero)

En primer lugar, se presenta una visualización de la data, a fin de comprender con mayor detalle la definición de las variables.


Ahora bien, se presentan algunas gráficas desarrolladas en el análisis exploratorio de datos, esto permite obtener una mayor comprensión de los datos y su importancia para el analisis de delitos en la ciudad de cali; en primer lugar se presenta un gráfico de barras que relaciona la frecuencia de delitos en cada comuna de la ciudad en función de los meses

![image](https://github.com/user-attachments/assets/7a06e38f-ccf5-4d33-b958-53b6a5d745db)

Según el gráfico, se puede concluir que enero es el mes con la mayor cantidad de delitos en todas las comunas de la ciudad, seguido de febrero. Además, se observa una tendencia decreciente a medida que avanzan los meses, lo que indica que al inicio del año el índice de delitos es elevado y disminuye en comparación con el mes anterior.

Por otra parte, se presenta la frecuencia absoluta de los delitos por cada mes, este gráfico permite brindar un panorama general del comportamiento de los datos en fucnión del tiempo

![image](https://github.com/user-attachments/assets/3692ec68-a669-47f5-9b2a-d5a2cf22afca)

El gráfico respalda lo mencionado anteriormente, evidenciando que enero es el mes con mayor frecuencia de delitos, y que estos tienden a disminuir con el tiempo. Esta alta incidencia en enero podría estar relacionada con dinámicas estacionales, como el incremento del flujo de personas y de dinero durante las festividades y vacaciones, lo que crea un entorno propicio para la ocurrencia de delitos.

Adicionalmente se presenta una grafica que relaciona la frecuencia de delitos en función de los dias de semana.
![image](https://github.com/user-attachments/assets/61351cb5-c081-4c3e-8a46-da94c7c25323)

La gráfica muestra que los hurtos ocurren con mayor frecuencia hacia el final de la semana laboral, alcanzando su punto máximo los días viernes, seguido de cerca por jueves y miércoles, con más de 1,300 incidentes reportados en estos días. En contraste, el domingo es el día con la menor cantidad de hurtos, con menos de 1,000 reportes, lo que sugiere una disminución significativa de la actividad delictiva. Los días lunes, martes y miércoles presentan una actividad delictiva media, con cifras cercanas a los 1,200-1,300 hurtos. El sábado, aunque registra menos incidentes que el resto de la semana, aún supera al domingo en número de hurtos. Estos patrones podrían estar relacionados con el aumento de la actividad económica y social hacia el final de la semana, mientras que el domingo, al haber menos movimiento en la ciudad, presenta menos oportunidades para que se cometan delitos.

Por otro lado, se expone una grafica que relaciona la frecuencia de delitos en función de la hora del día

![image](https://github.com/user-attachments/assets/9ef0ff76-6aee-428b-8c8e-ac737ac9c0a5)

La gráfica ilustra la distribución de hurtos a lo largo de las 24 horas, destacando picos en momentos específicos. Se registra un primer pico significativo cerca de la medianoche, con casi 500 incidentes, lo que indica alta actividad delictiva en la noche. Entre la 1 y las 4 de la mañana, los hurtos disminuyen notablemente, pero a partir de las 5 de la mañana, comienza un aumento que alcanza su punto máximo entre las 7 y las 11 horas, especialmente alrededor de las 10. Durante el mediodía y la tarde, los hurtos se mantienen elevados, con fluctuaciones, y un nuevo pico se observa alrededor de las 19 y 20 horas, superando nuevamente los 500 incidentes. A partir de las 21 horas, la actividad delictiva comienza a disminuir, siendo especialmente baja a las 23 horas antes de volver a aumentar a medianoche.

Asimismo, se presenta la frecuencia de delitos en función de los barrios de las comunas que fueron identificadas como aquellas que tienen mayor ocurrencia.

![image](https://github.com/user-attachments/assets/d477c56e-5471-47a5-bca5-47a3efa782db)

Las gráficas presentan la cantidad de hurtos cometidos en diferentes barrios dentro de las comunas 2, 3, 17 y 19 donde se puede apreciar lo siguiente:

- **Comuna 2**: 
En esta comuna, los barrios con mayor cantidad de hurtos son Prados del Norte, San Vicente y Santa Mónica, cada uno registrando más de 100 hurtos. Otros barrios como La Flora, Versalles y Vípasa también muestran una actividad delictiva relevante, aunque menor.

- **Comuna 3**: 
   El barrio con mayor cantidad de hurtos es San Pedro, superando ampliamente a otros barrios. El Nacional muestra el nivel más bajo de delitos.

- **Comuna 17**: 
  En esta comuna, los hurtos están más concentrados en Lili. También destacan barrios como Urbanización San Joaquín y el ingenio,, aunque en menor medida.

- **Comuna 19**: 
San Fernando Viejo y San Fernando Nuevo son los barrios con más hurtos reportados, ambos superando los 100 casos. Otros barrios como Urbanización Tequendama, El Cedro y El Lido también muestran una considerable actividad delictiva.

por utlimo, con referencia al analisis exploratorio, se presneta un mapa de la ciudad y se marcan aquellas comunas que tienen mayor cantidad de delitos, esto permite brindar una idea sobre aquellas zonas geograficas que se pueden indetificar como "zonas rojas"

  ![image](https://github.com/user-attachments/assets/2516d450-fcc4-4054-b98b-06b4a89c7419)

El mapa muestra la distribución de las comunas de Cali, utilizando un esquema de colores que indica la incidencia de hurtos: los tonos oscuros representan mayor frecuencia, mientras que los claros indican menos casos. Las comunas más afectadas por hurtos son la 19, 17, 2 y 3, con la comuna 19 registrando el mayor número de incidentes, posiblemente debido a su alta urbanización y actividad económica. En contraste, las comunas 1, 20 y 22 muestran una menor incidencia de hurtos. Las comunas 1 y 20, de estratos socioeconómicos más bajos, pueden experimentar otros tipos de delitos, mientras que la comuna 22, una zona exclusiva habitada por personas de alto poder adquisitivo, presenta una baja incidencia de hurtos.

Una vez completado el análisis exploratorio, se procedió a exportar la base de datos limpia y se creó la correspondiente en MySQL. Este paso es fundamental, ya que permite realizar consultas de manera efectiva, garantizando la integridad, accesibilidad y eficiencia en la gestión de la información, además de facilitar el manejo de grandes volúmenes de datos. Para llevar a cabo este proceso, se estableció la conexión a SQL desde Python y se creó la tabla con las características correspondientes. El resultado se presenta en la siguiente imagen:

![base de datos  SQL](https://github.com/user-attachments/assets/e8c9fd58-58e7-4147-9024-e8d072e4021f)

Posteriormente, se realizaron algunas consultas para probar las funcionalidades de la herramienta. Sin embargo, es importante destacar que estos registros son únicamente con fines de prueba y no representan información verídica. En primer lugar, se agregó un registro al final de la base de datos; cabe recordar que inicialmente contábamos con 8.640 registros, por lo que el registro 8.641 representa el nuevo ingreso. El resultado de la consulta se muestra en la siguiente imagen.

![Consulta1](https://github.com/user-attachments/assets/029656a7-cc78-426c-a083-760ca08fec1f)
Asimismo, fue realiza una consulta donde fueron agregados cinco registros con información aleatoria; despues fue empleado el metodo "DELETE" y "WHERE" para eliminar el ultimo registro, correspondiente al 8.645. El resultado se muestra en la imagen

![Consulta2](https://github.com/user-attachments/assets/14823754-0c88-46f0-b73f-9dd14301752f)
La utlima consulta, correspondió a cambiar un campo especifico dentro de un registro, para esto fue empleado el metodo "SET" y "WHERE"

Ahora bien, la utltima parte coprresponde al despliegue
