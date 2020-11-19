1 - Installer chocolatey, kør følgende kommando i powershell som  adminstrator:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
2 - Installer make:
choco install make
3 - Installer kaggle vha. makefile(naviger til makefile stien i cmd og kør kommando):
make kaggle
4 - Hent / slet dataset vha. makefile kommandoer.