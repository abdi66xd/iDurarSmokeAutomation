#!/bin/bash

# Esperar hasta que el controlador de Chrome esté disponible
while [ ! -f /usr/bin/chromedriver ]; do
    sleep 1
done

# Iniciar el servidor Selenium
java -jar /tmp/selenium-server-standalone.jar
