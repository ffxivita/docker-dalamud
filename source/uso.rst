.. highlight:: dockerfile

===============
Uso
===============


Questa immagine viene pubblicata con due tag distinti, ``latest`` e
``staging``, che ovviamente includono versioni differenti di Dalamud.
Tutti i files necessari vengono dal repository ufficuale
`Dalamud-Distrib <https://github.com/goatcorp/dalamud-distrib>`__.

Latest
================
Latest è la versione corrente e stabile di Dalamud e può essere
richiamata aggiungendo quanto segue al vostro Dockerfile:

.. code-block:: dockerfile

   FROM ghcr.io/ffxivita/docker-dalamud:latest

Staging
================
Staging è la versione di Dalamud ancora in via di sviluppo e può essere
usata aggiungendo quanto segue al vostro Dockerfile:

.. code-block:: dockerfile

   FROM ghcr.io/ffxivita/docker-dalamud:staging

.. toctree::
    :titlesonly: