# Mercado Libre DataSec Technical Challenge

|Challenge|Link|
|---|---|
|1°|[Link](https://github.com/Tnr1112/MercadoLibre-DataSec-Technical-Challenge/blob/a7a985b6c905f48feecbefa9d5f7020e76e4ddd4/challenge1.py)|
|2°|[Link](https://github.com/Tnr1112/MercadoLibre-DataSec-Technical-Challenge/blob/a7a985b6c905f48feecbefa9d5f7020e76e4ddd4/challenge2.py)|
|3°|[Link](https://github.com/Tnr1112/MercadoLibre-DataSec-Technical-Challenge/blob/a7a985b6c905f48feecbefa9d5f7020e76e4ddd4/challenge3.py)|

## Alternativas solución descartadas

Tanto para el challenge N°1 como para N°2 tuve más de una posible solución pero por diferentes motivos que más abajo enuncio, decidí quedarme con la versión publicada. 

### Challenge N°1

Además de la versión publicada, originalmente consideré una solución donde primero obtenía las coordenadas de todas las bombas para luego generar el nuevo tablero asignando valores sólo a los casilleros adyacentes. Sin embargo, decidí descartar esta solución por considerarla menos eficiente ya que requería más iteraciones. 

### Challenge N°2

En este challenge consideré implementar un algoritmo de caching para evitar consultas innecesarias a la API que podrían resultar en costos adicionales. Consistía en guardar temporalmente en un archivo local los datos consultados para sólo volver a descargarlos cuando se reciba una consulta transcurrido un periodo preestablecido de tiempo. Sin embargo, teniendo en cuenta que probablemente el script forme parte de un sistema más grande, asumí que si se quisiese implementar algún tipo de caching se haría a nivel sistema y no script por script, por lo que descarté la implementación de dicho algoritmo.    
