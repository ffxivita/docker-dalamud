.. highlight:: xml
.. index:: Requisiti
.. _Requisiti

================
Requisiti
================

Per compilare il vostro progetto che ha Dalamud dentro ad un container,
dovete perforza usare ``DalamudLibPath`` e avere il seguente snippet di
codice dentro il vostro file csproj:

.. code-block:: xml

   <PropertyGroup Condition="'$([System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform($([System.Runtime.InteropServices.OSPlatform]::Linux)))'">
       <DalamudLibPath>$(DALAMUD_HOME)/</DalamudLibPath>
       <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
   </PropertyGroup>