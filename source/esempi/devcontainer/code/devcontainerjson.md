# DevContainer (Json)

Dentro alla cartella `.devcontainer` ci dovrà essere il file `devcontainer.json` o se non volete usare la cartella `.devcontainer` il file dovrà essere nella root del progetto e chiamarsi `.devcontainer.json`

L'esempio sottostante è preso da un nostro progetto attuale e utilizza la cartella `devcontainer` con al suo interno il file
`Dockerfile` e il file `devcontainer.json` di cui avete il codice di seguito:

``` json
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

```