#!/bin/bash
#descargamos el repo de github
git clone https://github.com/jheisonV/lulo_test.git
#mantenemos el contenedor vivo pero en segundo plano
docker run --name jheison-lulo -d jheisonv/lulo-test:v2 tail -f /dev/null
#instalamos librerias de python para ejecutar el programa
docker exec -it jheison-lulo /bin/bash
pip install pandas
pio install requests
cd src/
python3 clave.py
cat jhei_test.csv
