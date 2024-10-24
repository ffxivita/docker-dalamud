# DevContainer (Dockerfile)

Questo dockerfile è preso da un plugin esistente di xivita ed è utilizzato per lo sviluppo su sistemi non windows.

``` dockerfile
    # Immagine da usare
    FROM  ghcr.io/ffxivita/docker-dalamud:latest@sha256:add01fe4e17995e1e486387b9b2153231380ab75cec78a2d9361d1bb126e3731
    
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
