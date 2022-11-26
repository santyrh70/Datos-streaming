# instalar Kafka
```
$ sudo yum install java-1.8.0  
$ wget https://archive.apache.org/dist/kafka/3.3.1/kafka_2.12-3.3.1.tgz

$ tar -xzf kafka_2.12-3.3.1.tgz $ cd kafka_2.12-3.3.1
```

***Iniciar zookeeper***:
```
$ bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
```

***Iniciar el servidor de Kafka:***
```
$ bin/kafka-server-start.sh -daemon config/server.properties
```

***Crear un tópico:***
```
$ bin/kafka-topics.sh --create --bootstrap-server localhost:9092 -- replication-factor 1 --partitions 1 --topic sample-topic
```

***Listar los tópicos:***
```
$ bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

***Borrar un tópico:***
```
$ bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic sample-topic
```

## PRODUCERS:
```
$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic sample- topic
```

## CONSUMERS:
```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sample-topic --from-beginning
```

## Detener el servidor de Kafka:
```
$ bin/kafka-server-stop.sh
```

## Detener zookeeper:
```
$ bin/zookeeper-server-stop.sh
```
