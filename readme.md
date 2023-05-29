Proyecto Creado por: Alejandro Sossa 29/05/2023

Titulo: Space Shooter

Descripcion:
El juego consiste en evitar los meteoros, tienes opciones para defenderte como la barra de espacio, la cual te sirve para arrojar un laser.

Funciones Usadas:
drawtext()
draw_shield_bar()
update()
shoot()
new_meteor()

Clases Usadas:
Class Player
Class Meteor
Class Bullet

Descripcion del codigo:
Todo el juego se ejecuta en un bucle while, se colocan todas las funciones alli, se verifica colision de la nave con el meteoro en caso de 4 choques pierde, se usa la funcion sprite.collide para saber si la nave a colisionado, se recorre en bucles for algunas cosas, como la creacion de nuevos lasers, la suma del puntaje, se acumula en la variable score y alli se lleva un registro de cuantos meteoros se logran destruir.
