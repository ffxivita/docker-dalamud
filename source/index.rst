.. XIVITA Docker Dalamud documentation master file, created by
   sphinx-quickstart on Tue Sep 20 10:59:41 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Docker-Dalamud
==============

Un ambiente di sviluppo comtrollato per lo sviluppo di plugin
`Dalamud <https://github.com/goatcorp/Dalamud>`__ con Dotnet, su base
``Dotnet/SDK:<ver>-alpine``.

Il target primario di questa immagine è per i `development
containers <https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers>`__
e ambienti CI/CD, anche se funziona in ogni ambiente.

Pre-Requisiti
-------------

Per compilare il vostro progetto che ha Dalamud dentro ad un container,
dovete perforza usare ``DalamudLibPath`` e avere il seguente snippet di
codice dentro il vostro file csproj:

::

   <PropertyGroup Condition="'$([System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform($([System.Runtime.InteropServices.OSPlatform]::Linux)))'">
       <DalamudLibPath>$(DALAMUD_HOME)/</DalamudLibPath>
       <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
   </PropertyGroup>

Uso
---

Questa immagine viene pubblicata con due tag disinti, ``latest`` e
``staging``, che ovviamente includono versioni differenti di Dalamud.
Tutti i files necessari vengono dal repository ufficuale
`Dalamud-Distrib <https://github.com/goatcorp/dalamud-distrib>`__.

Latest
~~~~~~

Latest è la versione corrente e stabile di Dalamud e può essere
richiamata aggiungendo quanto segue al vostro Dockerfile:

::

   FROM ghcr.io/ffxivita/docker-dalamud:latest

Staging
~~~~~~~

Staging è la versione di Dalamud ancora in via di sviluppo e può essere
usata aggiungendo quanto segue al vostro Dockerfile:

::

   FROM ghcr.io/ffxivita/docker-dalamud:staging

Aggiornamento Immagini Container
--------------------------------

Tutti i container vengono aggiornati automaticamente ogni settimana per
includere l'ultima versione di Dalamud che il tag consente. La versione
di .NET verrà incrementata quando sarà supportata.
.. toctree::
   :maxdepth: 2
   :titlesonly:
