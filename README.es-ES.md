

![OlliePy logo](./sphinxSource/source/_static/imgs/logo.png)
<br/>
<br/>
![TestReport](https://github.com/ahmed-mohamed-sn/olliePy/workflows/TestReport/badge.svg?branch=master)
![CI](https://github.com/ahmed-mohamed-sn/olliePy/workflows/CI/badge.svg)
[![Coverage](https://codecov.io/github/ahmed-mohamed-sn/olliepy/coverage.svg?branch=master)](https://codecov.io/gh/ahmed-mohamed-sn/olliepy)
<br/>
[![Downloads](https://pepy.tech/badge/olliepy)](https://pepy.tech/project/olliepy)
[![Downloads](https://pepy.tech/badge/olliepy/month)](https://pepy.tech/project/olliepy/month)
[![Downloads](https://pepy.tech/badge/olliepy/week)](https://pepy.tech/project/olliepy/week)
<br/>
[![PyPI Latest Release](https://img.shields.io/pypi/v/olliepy.svg)](https://pypi.org/project/olliepy/)
[![License](https://img.shields.io/pypi/l/olliepy.svg)](https://github.com/ahmed-mohamed-sn/olliepy/blob/master/LICENSE)
<br/>
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/olliepy.svg)](https://pypi.python.org/pypi/olliepy/)
<br/>
<br/>

<h3>
<a href="../../issues/new">:speech_balloon: Haz una pregunta</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="../../issues?q=is%3Aissue+is%3Aclosed+sort%3Aupdated-desc">:book: Revisa preguntas</a>
</h3>

# OlliePy
> **OlliePy** es un paquete de Python que puede ayudar a los científicos de datos a
> explorar sus datos y evaluar y analizar sus experimentos de aprendizaje automático
> utilizando el poder y la estructura de las aplicaciones web modernas. 
> El científico de datos solo necesita proporcionar los datos y cualquier información
> requerida, y OlliePy generará el resto.

## <br/>Documentación
Comienza siguiendo la [guía](https://ahmed-mohamed-sn.github.io/olliePy/)

### Instalación
`pip install -U olliepy`

### Soporte de sistemas operativos
- Linux
- MacOs
- Windows (desde la versión v0.2.6+ de olliepy)

### Ejemplos
Comienza utilizando los [ejemplos](https://github.com/ahmed-mohamed-sn/olliePy/tree/master/examples) proporcionados

## Informe de análisis de errores para regresión
**OlliePy** puede ayudarte a realizar análisis de errores para problemas de regresión.

### Características
- Comparar diferentes conjuntos de datos
- Comparar diferentes grupos de error en tus datos.
- Verificar cambios en los datos (data shift) utilizando los informes de características numéricas y categóricas
- Verificar cambios conceptuales (concept shift) utilizando el informe de patrones

![error analysis report demo](./sphinxSource/source/_static/imgs/error-analysis-regression-demo.gif)

## <br/> Panel interactivo
**OlliePy** también puede ayudarte a crear un panel interactivo en minutos.
El panel puede utilizarse para el EDA o para el análisis de errores en problemas de clasificación o regresión.
El rendimiento del panel depende del tamaño de los datos, el número de gráficos y las especificaciones del equipo utilizado.

![interactive dashboard demo](./sphinxSource/source/_static/imgs/interactive-dashboard-demo.gif)

### Características
- Gráficos arrastrables y redimensionables
- Filtrado cruzado
- Elige entre 14 gráficos personalizables diferentes
- Se pueden aplicar diferentes agregaciones
- Gráficos con función de búsqueda
- Crear nuevos gráficos
- Editar gráficos existentes
- Eliminar gráficos
- Modo oscuro
- Función de guardado automático
- Los gráficos pueden bloquearse en su posición
- Pantalla completa
- Agrupar características numéricas para usarlas en mapas de calor, gráficos de filas, etc.


### Gráficos disponibles 
|                                                                                                   |                                                                                                |
|:-------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
|            **Gráfico de barras** ![bar-chart](./sphinxSource/source/_static/gifs/bar-chart.gif)           |            **Diagrama de caja** ![box-plot](./sphinxSource/source/_static/gifs/box-plot.gif)           |
|          **Tabla de datos** ![data-table](./sphinxSource/source/_static/gifs/data-table.gif)          |            **Mapa de calor** ![heat-map](./sphinxSource/source/_static/gifs/heatmap.gif)            |
|            **Histograma** ![histogram](./sphinxSource/source/_static/gifs/histogram.gif)           |       **Mapa de Leaflet** ![leaflet-map](./sphinxSource/source/_static/gifs/leaflet-map.gif)       |
| **Visualización numérica** <br/> ![number-display](./sphinxSource/source/_static/gifs/number-display.gif) |          **Gráfico circular** ![pie-chart](./sphinxSource/source/_static/gifs/pie-chart.gif)          |
|            **Gráfico de filas** ![row-chart](./sphinxSource/source/_static/gifs/row-chart.gif)           |      **Gráfico de dispersión** ![scatter-plot](./sphinxSource/source/_static/gifs/scatter-plot.gif)     |
|            **Gráfico de sol radiante** ![sun-burst](./sphinxSource/source/_static/gifs/sun-burst.gif)           |   **Gráfico de barras temporal** ![time-bar-chart](./sphinxSource/source/_static/gifs/time-bar-chart.gif)  |
|      **Diagrama de caja temporal** ![time-box-plot](./sphinxSource/source/_static/gifs/time-box-plot.gif)     | **Gráfico de líneas temporal** ![time-line-chart](./sphinxSource/source/_static/gifs/time-line-chart.gif) |


## Hoja de ruta de OlliePy
- [x] Informe de análisis de errores para regresión
- [x] Panel interactivo
- [ ] Panel interactivo incrustado
- [ ] Informe de evaluación y comparación de modelos de aprendizaje automático que incluye interpretación del modelo y verificación de sesgos
- [ ] Informe de análisis de errores para clasificación
