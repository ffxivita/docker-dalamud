.. highlight:: dockerfile
.. highlight:: json

===============
DevContainer
===============

I `Dev Container <https://code.visualstudio.com/docs/remote/containers>`_ sono una funzionalità di `Visual Studio Code <https://code.visualstudio.com>`_ che permettono di usare un container docker per lo sviluppo. Questa feature si compone essenzialmente di un file ``Dockerfile`` o ``docker-compose.yml`` e un file json, chiamato ``devcontainer.json`` o ``.devcontainer.json`` se il file si trova nella root del vostro progetto.

.. code-block:: json
    {
        "dockerFile": "Dockerfile",
        "updateRemoteUserUID": true,
        "containerUser": "dev",
        "remoteUser": "dev",
        "postAttachCommand": "dotnet restore",
        "customizations": {
            "vscode": {
                "extensions": [
                    "ms-dotnettools.csharp",
                    "wayou.vscode-todo-highlight",
                    "vivaxy.vscode-conventional-commits"
                ]
            }
        }
    }

Ed ecco il file ``Dockerfile`` di un nostro plugin.

.. code-block:: dockerfile
    FROM  ghcr.io/ffxivita/docker-dalamud:latest
    ENV DOTNET_CLI_TELEMETRY_OPTOUT=1
    ENV DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1
    # Crea un utente non-root.
    RUN adduser --disabled-password --gecos "" dev
    # Installa le dipendenze.
    RUN apk add --update openssh
    # Clona il repository dentro /workspaces (sovvrascrive se già presente).
    WORKDIR /workspaces
    RUN git clone https://github.com/DarkArtek/XIVITASanctuary.git