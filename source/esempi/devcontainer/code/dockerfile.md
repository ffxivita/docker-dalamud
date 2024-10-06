# DevContainer (Dockerfile)

Questo dockerfile è preso da un plugin esistente di xivita ed è utilizzato per lo sviluppo su sistemi non windows.

``` dockerfile
    # Immagine da usare
    FROM  ghcr.io/ffxivita/docker-dalamud:latest@sha256:efb8d769a0304cf58a07ded2013854b5c74b59966a630497207d9b1a61f67ea9
    
    # Variabili d'Ambiente
    ENV DOTNET_CLI_TELEMETRY_OPTOUT=1
    ENV DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1
    
    # Crea un utente non-root.
    RUN adduser --disabled-password --gecos "" dev
    
    # Installa le dipendenze.
    RUN apk add --update openssh
    
    # Clona il repository dentro /workspaces (sovvrascrive se già presente).
    WORKDIR /workspaces
    
    RUN git clone https://github.com/ffxivita/testplugin.git
```
