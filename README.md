Funcionamiento
--------------
El script esta pensado para enviar cada dia a las 19:15 la asistencia a clase (en segundo plano sin mostrar nada molesto por pantalla), él mismo detecta si estás en el centro (La Salle) o no, y en función de esto envia un tipo de asistencia u otra.


Plataforma
------------
- Linux (Ubuntu 18.04.5)
  - crontab
  - python3 / pip3


- Windows
  - Te buscas la vida (puedes usar https://www.z-cron.com/es/ para programar la ejecucin del script cada x tiempo)
  - Python3 / pip3


Instalación
------------
 - cd /opt
 - sudo git clone git@github.com:elChechu/tracker.git
 - nano credenciales.txt
 - cd tracker
 - sudo ./run.sh
