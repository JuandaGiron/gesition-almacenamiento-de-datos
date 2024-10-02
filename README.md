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

![image](https://github.com/user-attachments/assets/61351cb5-c081-4c3e-8a46-da94c7c25323)


