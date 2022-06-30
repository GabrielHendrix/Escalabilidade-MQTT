#Reproduzindo os Testes

Um ambiente para fazer teste de carga e compreender o uso do protocolo MQTT. 

##Conteúdo:

- `publisher.py` Faz uma publicação em um tópico.
- `subscriber.py` Faz a inscrição em um tópico.
- `log_proc.sh` Captura o uso de CPU e memória


##Uso

1. Instalar  Mosquitto e o gnuplot
```
sudo apt-get install mosquitto mosquitto-clients
sudo apt-get install gnuplot
```

2. O broker vai ser inicializado por padrão.  Para ver os logs é necessário
pará-lo e reinicializá-lo.

```
sudo /etc/init.d/mosquitto stop
sudo mosquitto –v
```

3. Em um novo terminal execute o log_proc.sh

4. Abra outros dois terminais, e rode, separadamente, os scripts `publisher.py` e `subscriber.py`. 

5. Ao final, será gerado um mem-graph.png com o uso de CPU e memória.