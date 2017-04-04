#!/bin/bash

java -jar jenkins-cli.jar -s https://localhost:8080/ install-plugin $1
