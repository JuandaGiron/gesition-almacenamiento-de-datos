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
