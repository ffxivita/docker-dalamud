# Docker-Dalamud
Un ambiente di sviluppo comtrollato per lo sviluppo di plugin  [Dalamud](https://github.com/goatcorp/Dalamud) con Dotnet, su base `Dotnet/SDK:<ver>-alpine`. 

Il target primario di questa immagine è per i [development containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers) e ambienti CI/CD, anche se funziona in ogni ambiente.

## Pre-Requisiti
Per compilare il vostro progetto che ha Dalamud dentro ad un container, dovete perforza usare  `DalamudLibPath` e avere il seguente snippet di codice dentro il vostro file csproj:

```
<PropertyGroup Condition="'$(OS)' != 'Windows_NT'">
  <DalamudLibPath>$(DALAMUD_HOME)/</DalamudLibPath>
  <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
</PropertyGroup>
```

## Uso 
Questa immagine viene pubblicata con due tag disinti, `latest` e `staging`, che ovviamente includono versioni differenti di  Dalamud. Tutti i files necessari vengono dal repository ufficuale [Dalamud-Distrib](https://github.com/goatcorp/dalamud-distrib).

### Latest 
Latest è la versione corrente e stabile di Dalamud e può essere richiamata aggiungendo quanto segue al vostro Dockerfile:

```
FROM ghcr.io/ffxivita/docker-dalamud:latest
```

### Staging
Staging è la versione di Dalamud ancora in via di sviluppo e può essere usata aggiungendo quanto segue al vostro Dockerfile:

```
FROM ghcr.io/ffxivita/docker-dalamud:staging
```

## Aggiornamento Immagini Container
Tutti i container vengono aggiornati automaticamente ogni settimana per includere l'ultima versione di Dalamud che il tag consente. La versione di .NET verrà incrementata quando sarà supportata.
