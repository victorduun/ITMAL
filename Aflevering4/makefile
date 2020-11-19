SHELL = cmd
path = ${USERPROFILE}\.kaggle\kaggle.json
kaggleusername = aseitmal
kaggleapitoken = {"username":"${kaggleusername}","key":"f780921f2ee591e0afa799e19439b732"}

.PHONY: kaggle

all: data/raw/shipsnet.json

kaggle: 
	pip install kaggle
	$(shell echo ${kaggleapitoken} > ${path}) 
	echo Wrote api token to ${path}

data/raw/shipsnet.json:
	$(shell kaggle datasets download -d rhammell/ships-in-satellite-imagery -p ./data/raw)
	$(shell powershell -command "Expand-Archive -Force './data/raw/ships-in-satellite-imagery.zip' './data/raw/'")
	echo done

clean:
	rm -rf .\data\raw\scenes
	rm -rf .\data\raw\shipsnet
	del .\data\raw\*.zip
	del .\data\raw\*.json