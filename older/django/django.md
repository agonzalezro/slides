Introducción a **django**
======

---

¿Qué es django?
--------
De la wikipedia:

_Django es un framework de desarrollo web de código abierto, escrito en Python, que cumple en cierta medida el paradigma del [Modelo Vista Controlador](http://es.wikipedia.org/wiki/Modelo_Vista_Controlador)._

![django](django.png)

_La meta fundamental de Django es facilitar la creación de sitios web complejos. Django pone énfasis en el re-uso, la conectividad y extensibilidad de componentes, del desarrollo rápido y del principio de **DRY** (del inglés Don't Repeat Yourself)_

---

¿Qué es un framework?
---------------------
También de la wikipedia:

_(...) un conjunto estandarizado de conceptos, prácticas y criterios para enfocar un tipo de problemática particular, que sirve como referencia para enfrentar y resolver nuevos problemas de índole similar._

_En el desarrollo de software, un framework es una **estructura conceptual y tecnológica de soporte definida, normalmente con artefactos o módulos de software concretos, con base en la cual otro proyecto de software puede ser organizado y desarrollado**. Típicamente, puede incluir soporte de programas, bibliotecas y un lenguaje interpretado entre otros programas para ayudar a desarrollar y unir los diferentes componentes de un proyecto._

---

Manos a la obra
===============

---

Instalación
-----------

<div class="notes">También está disponible en los repositorios, aquí explicamos la vía "difícil".</div>

#Descarga
    !console
    wget http://www.djangoproject.com/download/1.2.1/tarball/

#Instalación
    !console
    tar zxvf Django-1.2.1.tar.gz
    cd Django-1.2.1
    sudo python setup.py install

#Test
    !python
    >>> import django
    >>> print django.VERSION
    (1, 2, 0, 'final', 0)

---

Nuestro primer proyecto
-----------------------

Vamos a hacer un **mini-mini-gestor de contenidos**.

#Crear un proyecto
    !console
    $ django-admin.py startproject hello

#Crear una aplicación
    !console
    $ cd hello
    $ django-admin.py startapp world

---

Repasando lo que tenemos
------------------------
#~/hello/
- `__init__.py`: típico fichero de python necesario para importar.
- `manage.py`: nos permitirá gestione en nuestro proyecto como sincronizar la BD o arrancar el servidor.
- `settings.py`: configuración de nuestro proyecto.
- `urls.py`: aquí gestionaremos a donde van todas las peticiones que se hacen a nuestro servidor.

#~/hello/world/
- `__init__.py`: idem.
- `models.py`: los modelos de nuestra aplicación. 
- `tests.py`: los test unitarios.
- `views.py`: las vistas.

---

Configurar el entorno
---

Necesitamos configurar una base de datos como mínimo, para el ejemplo usaremos sqlite por lo que debemos tener instalado el módulo `python-sqlite`.

    !python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

---

Nuestro primer modelo
---

[Lista completa de campos disponibles.](http://docs.djangoproject.com/en/dev/ref/models/fields/)

#models.py

    !python
    # *-* coding: utf-8 *-*

    from django.db import models

    class Noticia(models.Model):
        titulo = models.CharField(max_length=64, blank=False, help_text="El título de tu noticia.")
        entrada = models.CharField(max_length=512, blank=True, help_text="La entradilla de tu noticia.")
        cuerpo = models.TextField(blank=False, help_text="El cuerpo de tu noticia.")

---

Preparándonos para escribir
-----------

Necesitamos activar la interfaz de administrador para poder hacerlo.

#urls.py

    !python
    from django.conf.urls.defaults import *

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        # Example:
        # (r'^hello/', include('hello.foo.urls')),

        # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
        # to INSTALLED_APPS to enable admin documentation:
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        (r'^admin/', include(admin.site.urls)),
    )

---

Preparándose para escribir (2)
-------

#settings.py

    !python
    (...)

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        'world',
    )

    (...)

---

Preparándose para escribir (3)
----------

Necesitamos registrar nuestro modelo en la interfaz admin, para ello necesitamos crear el fichero `admin.py` que no existe todavía en nuestra aplicación.

#admin.py

    !python
    from django.contrib import admin
    from models import Noticia

    class NoticiaAdmin(admin.ModelAdmin):
        list_display = ('titulo', 'entrada')
        #pass

    admin.site.register(Noticia, NoticiaAdmin)



---

Preparándonos para escribir (4)
------

#Sincronizando la base de datos

    !console
    $ python manage.py syncdb

    ...

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (Leave blank to use 'alex'): alex
    E-mail address: alex@lukkom.com
    Password: 
    Password (again): 
    Superuser created successfully.
    Installing index for auth.Permission model
    Installing index for auth.Group_permissions model
    Installing index for auth.User_user_permissions model
    Installing index for auth.User_groups model
    Installing index for auth.Message model
    Installing index for admin.LogEntry model
    No fixtures found.

---

¡Ahora sí!
-----

#Arrancando el servidor

    !console
    $ python manage.py runserver
    Validating models...
    0 errors found

    Django version 1.2, using settings 'hello.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


#Trasteando en nuestra interface de administrador
Visita: [http://localhost:8000/admin](http://localhost:8000/admin) y échale un ojo a la interface que nos proporciona `django-admin`.

---

Algo más avanzado
=====

---

Creando una vista simple
------

#views.py
    !python
    from models import Noticia
    from django.shortcuts import render_to_response

    def show_all(request):
        noticias = Noticia.objects.all()
        return render_to_response('show_all.html', locals())
        #return render_to_response('show_all.html', {'noticias': noticias, })

---

Creando una vista simple (2)
--------

#urls.py
    !python
    from django.conf.urls.defaults import *

    from world.views import show_all

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',

        (...)

        (r'^noticias/todas$', show_all)
        #(r'^noticias/todas$', 'world.views.show_all')
    )


---

Creando una vista simple (3)
-------

#settings.py
    !python
    TEMPLATE_DIRS = (
        'templates/',
    )

#templates/show_all.html
    !html
    <h1>Noticias</h1>
    {% for noticia in noticias %}
        <h2>{{ noticia.titulo }}</h2>
        <p>{{ noticia.entrada }}</p>
    {% endfor %}

#¡A probarlo!
    !console
    $ python manage.py runserver

Ahora puedes visitar [http://localhost:8000/noticias/todas](http://localhost:8000/noticias/todas) y ver el resultado.

---

¡Un último esfuerzo!
====

---

Creando una vista con parámetros
-----

#urls.py
Debemos añadir un dispatcher que reciba el identificador de la noticia que queremos ver, para ello agregamos esto a la variable patterns:

    !python
    url(r'^noticias/noticia/(\d+)/?$', 'world.views.show_one', name='show_one'),


#views.py
    !python
    from django.shortcuts import get_object_or_404

    def show_one(request, id):
        #noticia = Noticia.objects.get(pk=id)
        noticia = get_object_or_404(Noticia, pk=id)
        return render_to_response('show_one.html', locals())


---

Creando una vista con parámetros (2)
-----

Tenemos que cambiar el template que usamos anteriormente `show_all.html` para que tenga un link a cada noticia.

#show_all.html
    !html
    <h1>Noticias</h1>
    {% for noticia in noticias %}
        <h2><a href="{% url show_one noticia.id %}">{{ noticia.titulo }}</a></h2>
        <p>{{ noticia.entrada }}</p>
    {% endfor %}

Y tras ello crear nuestra nueva template:
#show_one.html
    
    !html
    <h1>{{ noticia.titulo }}</h1>
    <h2>{{ noticia.entrada }}</h2>
    <p>{{ noticia.cuerpo }}</p>

Pruébalo visitando [http://localhost:8000/noticias/todas](http://localhost:8000/noticias/todas).

---

**agonzalezro**@gmail.com
===
