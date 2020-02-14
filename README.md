Burriking 🍔🍟
====================================
A little burguer shop with global ambitions.

## Un poco de historia
Un día Albert E. quedó con su buen amigo Jose R. para comentarle que quería abrir un restaurante. Era una idea que le estaba rondando por la cabeza desde hacía varios años, como la asignatura que siempre tienes pendiente o como aquella novia/o que nunca funcionó. Para ello necesitaba un socio en el que confiar ciegamente la receta secreta del aliño de carne para hamburguesa de su querida madre. Allí en un sofá de su casa, cerveza en mano, se empezó a forjar la idea. Aunque no eran empresarios, sabían que tenían que estudiar a la competencia, hicieron un recorrido por las mejores hamburgueserías de Torrevieja, Guardamar, Villena y, finalmente Benejúzar. Al final llegaron a una conclusión: no hay hamburgueserías que traten su producto desde un punto de vista estrictamente gourmet.

Albert no dudó en contactar con su buena amiga Mercedes C., chef reconocida, cinco estrellas Michelín. Mercedes lo vio clarísimo desde el principio: "Es una idea fantástica pero arriesgada. ¿Os atrevéis? Para hacer hamburguesas gourmet la cocina debe funcionar como un restaurante gourmet, con mucho personal de cocina cualificado y bien organizado y yo conozco a la mejor jefa de cocina, Angie C., hemos estado trabajando en mi restaurante juntas durante mucho tiempo."

Mientras buscaban la ubicación adecuada, un día Albert paseando por Malasaña pasó por delante del antiguo Sumo, mítico restaurante japones de los años setenta, ¡se traspasaba!. Albert no durmió hasta conseguir convencer a su dueño, Luismi M., de que el japones ya no estaba en auge y que tenían que apostar por las hamburguesas. Luismi rápidamente se dio cuenta de la oportunidad de mercado que tenía delante y sólo acepto a alquilarles el local a condición de entrar a trabajar en el proyecto.

El sueño se convirtió en realidad, el resto es historia...

## En la actualidad
Burriking en la actualidad está presente en Madrid, Dublín, Valencia, Cáceres y Benejúzar, con un total de 24 tiendas, 240 empleados y una facturación de cuatro millones de euros anuales. El éxito de nuestras tiendas actuales es tal, que ahora mismo nos encontramos en un proceso de expansión para llevar Burriking a 16 países con 470 tiendas más en total. Para soportar tal brutal expansión, el equipo técnico tiene que escalar el sistema que se emplea ahora mismo, basado en hojas de excel y comunicación manual entre los propios empleados. Lo bueno de tener un sistema informático tan rudimentario es que da mucha libertad al equipo técnico para tomar decisiones de diseño nuevas, además, como todos los procesos son manuales, podremos definir como serán estos procesos con nuestras futuras herramientas.

## Que se necesita
Albert, nuestro CEO, le ha pedido a la CTO (Mabel O.) que le entregue en las próximas dos semanas un MVP técnico que actúe como base y ejemplo para poder dárselo a la empresa consultora de turno (Evil Corp). Este MVP va a estar acotado en funcionalidad, pero definirá la calidad del software a desarrollar por Evil Corp. Mabel está hasta arriba de trabajo y se ha visto obligada a externalizar el desarrollo del backend del MVP. Por lo tanto, aquí es dónde entras tú como desarrollador externo, para llevar a cabo el desarrollo del MVP del backend. Como puedes ver, es una pequeña tarea pero importante, pues tendrá implicaciones en la arquitectura de todo el sistema futuro de Burriking.

El departamento de frontend acaba de terminar la primera funcionalidad de la Web App para el customer, la de pedir hamburguesas. Esta consta de un formulario para rellenar el pedido de la comida y de un listado para ver el estado de los pedidos. Para ello necesitamos la parte de backend necesaria para hacer funcionar los dos casos de uso que frontend tiene ya hechos. Hemos dejado en la carpeta `frontend` dos mockups que se usaron para desarrollar el diseño del frontend.

En esta primera versión necesitamos:

- Soporte del backend para hacer un pedido soportando todas las opciones de comida disponibles.
- Soporte del backend para listar los pedidos hechos por mi usuario. Dónde se muestra de cada pedido: toda la comida pedida, el precio total y la fecha de realización del pedido.

Mabel en una charla escuchó que los servicios o micro-servicios están de moda. Ha escuchado que son buenos para escalar sistemas y probablemente lo tenga en cuenta para valorar el MVP. Pero a ella no le importan mucho los lenguajes de programación, porque cree que todos son buenos (incluso Lisp), así que tienes total libertad de elección para el lenguaje.

### El menú
Burriking ofrece una gran variedad de opciones que permiten al cliente personalizar su hamburguesa como más le guste. Se puede comprar una hamburguesa, patatas y bebida de forma individual o las tres cosas juntas (llamado burrimenú). El precio se calcula en función de como el cliente personalice su hamburguesa. Además, si es un burrimenú tiene un porcentaje de descuento del 15% sobre el total de la hamburguesa, pero tiene que pagar bebida y patatas.  

El precio de la hamburguesa base es de 5€ y se puede personalizar con muchas opciones. En el plan de expasión se habla de más formas de personalización de la hamburguesa que vendrán determinadas por un nuevo departamento de I+D, no deberíamos de saberlo, pero en unos meses ¡tendresmos nuevas opciones para personalizar la hamburguesa! 

Las opciones actuales son:  

Pan a elegir entre: chapata, molde o deluxe.  

Las opciones de la carne son casi infinitas. Además, se pueden combinar dos tipos de carne en la misma hamburguesa modificando a su vez el tamaño y la forma de cocinarlas. Por ejemplo, una de pollo poco hecha de 250g y otra veggie al punto de 380g.

- Tipos de carne: wagyu, pollo, cerdo, pescado, veggie, cebra o angus.  
- Tamaños: 125g (+2€), 250g (+2.5€) o 380g (+3.5€).  
- Cocinada: al punto, hecha o poco hecha.  

Ingredientes extra:

- Tomate (+1€), dos tipos: cherry o normal.
- Queso (+1.5€), solo cheddar.

En cuanto al burrimenú:

- Patatas:
    
    * Tipos: deluxe, gajo o de la abuela.
    * Tamaños: pequeñas (+2.5€) o grandes (+3.5€).
 
- Refresco: 
    
    * Burricola (+2.3€).
    * Burribeer (+2.5€).
    * Brawndo (+7.5€).

Además tenemos dos promociones activas:

- Euromanía: Todos los miércoles y domingos todas las patatas valen 1€.  
- Jarramanía: Si pides dos burribeer y unas patatas (da igual el tamaño de las patatas) el total son 3€. Válido todos los días de 16-19:30hs hasta el 30 de septiembre de este año.  

### Nuestros procesos actuales

Ahora mismo cuando un cliente llega a uno de nuestros restaurantes mantiene una conversación, tal que:  
...  
Customer "C": Buenos días.  
Barista "B": Buenos días.  
...  
C: Eh tron, yo y la Yoly tenemos hambre, me pones una hamburguesa con queso y patatas grandes, quiero la carne de cerdo tamaño mediano, poco hecha.  
B: ¿Señor, quiere bebida? Así es el burrimenú y le sale más barato.  
C: Ah, sí claro.  
...  
C: ¿Está mi pedido ya?  
B: No, no lo está.  
...  
C: ¿Cuánto es mi pedido?  
B: Su pedido son X€.  
C: Toma 30€.  
B: Gracias. Tome sus Y€ de cambio.  
C: Gracias.  
...  
C: ¿Está mi pedido ya?  
B: No, no lo está.  
...  
C: ¿Está mi pedido ya?  
B: Sí. Aquí lo tiene.  
...  
C: Gracias.  
B: Adiós.  
C: Adiós.  

En esta conversación el barista tiene abierto un excel, donde en una hoja especial llamada "Almacén", va mirando las provisiones que les quedan. En el caso de que el customer pida algo de lo que no queda, el barista se lo comunica.  

Al mismo tiempo el barista tiene conversaciones con los chefs de cocina, por ejemplo:  

Barista "B": Tengo un pedido nuevo: hamburguesa mediana de cerdo, poco hecha, con queso.  
Chef "C": Oído cocina.   
...  
B: ¿Está el pedido?  
C: No.  
...  
B: ¿Está el pedido?  
C: No.  
...  
B: ¿Está el pedido?  
C: Sí, toma.  

Los chefs de cocina tienen una media de 7min para preparar una hamburguesa. Las patatas y la bebida las suelen preparar los baristas y tardan unos 2min de media. 

### Gestión de la tienda

Al final de cada mes, el encargado de la tienda llama a la oficina y les comunica uno a uno los pedidos. De cada pedido comunica todos sus ingredientes, la cantidad, la fecha y el precio total. Así, los empleados de la oficina pueden saber que suministros se necesitan para el siguiente mes y llevar la contabilidad global de todas las tiendas.

Los oficinistas, una vez tienen todos los pedidos de todas las tiendas, hacen un único pedido global al proveedor con las necesidades de cada tienda. 

### Gestión de la empresa 

Por otro lado, sabemos que en el plan de expansión se planea añadir un nuevo departamento de inteligencia empresarial o en inglés, business intelligence. Así se podrá llevar un control de las rentabilidades de cada tienda, los días y horas que más se vende y si las promociones están funcionando como se esperaba.

Nota de Citibox
===========
El ejercicio simula ser un proyecto real para intentar abarcar varias fases del ciclo de lanzamiento de un proyecto software. Su objetivo principal es demostrar conocimientos y razonamientos al problema propuesto. Para demostrar conocimientos y/o razonamientos no hace falta que sea mediante el código de programación. La solución propuesta puede estar formada por código de programación, artefactos del diseño de software, incluso ideas bien reflejadas y expresadas. Lo que sí se debería dejar reflejado mediante código de programación es lo que se pide explícitamente en el enunciado con las lógicas asociadas.
Esta es una prueba de desarrollador backend, intenta no poner esfuerzos en cosas que están fuera del desarrollo de backend, como puede ser, configurar servicios con Docker. 
Si tienes cualquier duda de lo que sea, por favor, ¡pregúntanos!

