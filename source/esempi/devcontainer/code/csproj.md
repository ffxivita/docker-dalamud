# Dev Container (CSProj)
Per quanto riguarda il vostro file progetto, lo snippet sottostante dovrebbe darvi una idea di come implementarlo sui vostri plugin.
Ancora una volta, il seguente blocco di codice è preso da un nostro plugin.

``` xml
    <PropertyGroup>
        <DalamudLibPath>$(appdata)\XIVLauncher\addon\Hooks\dev\</DalamudLibPath>
        <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
    </PropertyGroup>

    <PropertyGroup Condition="'$([System.Runtime.InteropServices.RuntimeInformation]::IsOSPlatform($([System.Runtime.InteropServices.OSPlatform]::Linux)))'">
        <DalamudLibPath>$(DALAMUD_HOME)/</DalamudLibPath>
        <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>
    </PropertyGroup>

    <PropertyGroup Condition="'$(IsCI)' == 'true'">
        <DalamudLibPath>Dalamud</DalamudLibPath>
    </PropertyGroup>

    <ItemGroup>
        <Reference Include="FFXIVClientStructs">
            <HintPath>$(DalamudLibPath)FFXIVClientStructs.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="Newtonsoft.Json">
            <HintPath>$(DalamudLibPath)Newtonsoft.Json.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="Dalamud">
            <HintPath>$(DalamudLibPath)Dalamud.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="ImGui.NET">
            <HintPath>$(DalamudLibPath)ImGui.NET.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="ImGuiScene">
            <HintPath>$(DalamudLibPath)ImGuiScene.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="Lumina">
            <HintPath>$(DalamudLibPath)Lumina.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="Lumina.Excel">
            <HintPath>$(DalamudLibPath)Lumina.Excel.dll</HintPath>
            <Private>false</Private>
        </Reference>
        <Reference Include="CheapLoc">
            <Private>false</Private>
            <HintPath>$(DalamudLibPath)CheapLoc.dll</HintPath>
        </Reference>
    </ItemGroup>

    <ItemGroup>
        <PackageReference Include="DalamudPackager" Version="2.1.8"/>
    </ItemGroup>
```