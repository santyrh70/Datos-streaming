# instalar Logstash:

```
$ wget https://artifacts.elastic.co/downloads/logstash/logstash-8.5.0-linux-x86_64.tar.gz

$ tar -xzf logstash-8.5.0-linux-x86_64.tar.gz

$ cd logstash-8.5.0

$ bin/logstash -f etl-file.conf
```

##  Lanzar 2 o más ETL a la vez:

Logstash solo permite ejecutar un ETL si se pasa a traves de parametros, por lo que si se quieren tener 2 ETL en parralelo se necesita configurar lo siguiente.
```
#Editar archivo de configuracion 
$ vim config/pipelines.yml

#agregar:
- pipeline.id: nombre del pipeline
  path.config: direción dende se encuentra el archivo .conf del pipeline 
  
###Los archivos .conf no pueden estar en la misma dirección

#Ejecutar el binario sin parametro para que se lance con la configuracion de pipeline.yml
$ bin/logstash

```
