HTML'e Giriş
============

Merhabalar,

Bir önceki dersimizde, HTML'in ne olduğuyla ilgili
kısa bir tanımlama yapmıştık. İncelemek isterseniz
:ref:`html_nedir` başlıklı makalemize göz
atabilirsiniz.


Basit Bir HTML Sayfası
----------------------

.. code-block:: html

    
    <!DOCTYPE html>

    <html>

    <head>
        <title>Document</title>
    </head>

    <body>
        <h1>Sayfa Başlığı</h1>
        <p>Paragraf metni</p>
    </body>

    </html>


Açıklama
^^^^^^^^

- ``<!DOCTYPE html>`` Sayfanın HTML5 olduğunun tanımlamasıdır.
- ``<html>`` HTML sayfanın ana kapsayıcısıdır.
- ``<head>`` Tarayıcı ve arama motorlarına, sayfa hakkında bilgi vermek adına yazılan **meta** kodlarının yer aldığı, **style, script**, vb. gibi yapıların sayfaya dahil edildiği bölümdür.
- ``<title>`` Sayfanın ana başlığının tanımlandığı yerdir.
- ``<body>`` Sayfanın görülebilen alanında yer alan elementlerin kapsayıcısıdır. Özetle, girdiğiniz websitelerdeki gördüğünüz tüm metin, video, resim vb yapıların içerisinde bulunduğu yerdir.
- ``<h1>`` Sayfa içerisindeki en büyük başlığı tanımlamak için kullanılır.
- ``<p>`` Sayfa içerisindeki paragrafları tanımlamak için kullanılır.