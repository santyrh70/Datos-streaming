# instalar ElasticSearch:

```
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.5.0-linux-x86_64.tar.gz

$ tar -xzf elasticsearch-8.5.0-linux-x86_64.tar.gz

$ cd elasticsearch-8.5.0/

```

Editar configuraciones
```
$ vim config/elasticsearch.yml

http.port: 9200
http.host: 0.0.0.0
```



##  iniciar servidor:

```
$ bin/elasticsearch -d -p pid
```

##  inicio por primera vez:

Luego de iniciar por primera vez el servidor, se debe editar el siguiente archivo para desabilitar las opciones de seguridad 
```
$ vim config/elasticsearch.yml

#Editar de esta manera
xpack.security.enabled: false
xpack.security.http.ssl:
  enabled: false

#se reinicia el servidor
$ pkill -F pid
$ bin/elasticsearch -d -p pid
```

##  detener servidor:
```
$ pkill -F pid
```
