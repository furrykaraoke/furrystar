#! /bin/bash
# Skrypt/parenaście komend do automatyzacji wdrazaniu na proda/nadpisania zmian bo nie chce mi sie 1000 razy pisac tego samego do cholery co każdą zmianę xD
# automatize shit <root@bonn333.eu>
docker stop furrystar && docker rm furrystar && docker rmi furrystar:dev && docker build -t furrystar:dev . && docker run -v /app/furrystar/db:/furrystar/db --name=furrystar -d furrystar:dev
