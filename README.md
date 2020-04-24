# The order

Sistema para adminstracion de pedidos de restaurantes ambulantes. 

## Dependencias 

* asgiref==3.2.7
* Django==3.0.5
* mysqlclient==1.4.6
* Pillow==7.1.1
* pytz==2019.3
* sqlparse==0.3.1

## Instalar dependencias 

~~~
pip install -r requirements.txt
~~~


## Comandos para Django

No olvide antes de ejecutar los dos comandos siguientes, crear una base de datos en mysql con el 
nombre de `the_order` y un usuario llamado `gustavo` con contraseña `12345qwe` privilegios sobre dicha base de datos (Puede editar 
esta configuracion en el apartado la base de datos en los `settings.py`  del proyecto).
~~~
python manage.py makemigrations
~~~

~~~
python manage.py migrate
~~~

~~~
python manage.py collectstatic
~~~


~~~
python manage.py createsuperuser
~~~

~~~
python manage.py runserver
~~~

## Funcionamiento

Para ejecutar el proyecto usted debe instalar las dependencias, despues ejecutar los comandos de django en el
orden especificado.

para crear nuevos productos, o crear nuevos food trucks usted debe acceder como super usuario y despues seleccionar
la operaciond eseada y seguir los pasos. 