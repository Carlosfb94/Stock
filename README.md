# Stock

Repositorio con datos de inventario y ventas.

## Descripci\u00f3n de columnas del archivo Excel

A continuaci\u00f3n se detallan las columnas utilizadas en la planilla de stock:

- **Columna A**: En la celda `A1` se indica la fecha. El resto de la columna est\u00e1 vac\u00edo, salvo algunas filas donde aparece la leyenda `Total + [sigla del laboratorio]`, que indica el total acumulado para ese laboratorio.
- **Columna B**: C\u00f3digo de producto.
- **Columna C**: Sigla del laboratorio asociado al producto.
- **Columna D**: Nombre del producto. Cada producto aparece dos veces: una fila corresponde al costo y la otra al precio de venta (relacionadas con la columna E).
- **Columna E**: En la primera fila se muestra el costo del producto y en la siguiente, donde se repite el nombre, el precio de venta.
- **Columna F**: Margen num\u00e9rico, calculado como el valor absoluto de la diferencia entre costo y precio.
- **Columnas G a S**: Representan diferentes meses (fechas en los encabezados) y contienen las ventas de esos periodos. El mismo producto aparece dos veces: una fila para las cantidades y otra para las ventas de cada mes.
- **Columna T**: Stock disponible del producto a la fecha.
- **Columna U**: Total hist\u00f3rico vendido en cantidades. Los valores en negro corresponden a la venta hist\u00f3rica y los de color rojo indican la venta del periodo actual.
