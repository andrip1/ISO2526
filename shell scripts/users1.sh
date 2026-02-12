#!/bin/bash
#Fecha: 12/02/2026
#Autor: Andrés Ballester

whoami=$(whoami)

if [ $# -eq 0 ]; then
    uid=1000
else
    uid=$1
fi

echo "--------------------------------------"
echo "Informe de usuarios el día $(date +%d-%m-%Y) a las $(date +%H:%M)"
echo "UID solicitado: $uid"
echo "--------------------------------------"

total=0

for linea in $(cat /etc/passwd); do

    usuario=$(echo "$linea" | cut -d ":" -f 1)
    uid1=$(echo "$linea" | cut -d ":" -f 3 )

    if [ "$uid1" = "$uid" ]; then
        echo "Usuario: $usuario - UID: $uid1"
        total=$((total+1))
    fi

done

echo "--------------------------------------"
echo "Total: $total usuarios"
echo "--------------------------------------"
echo "$(date +%d-%m-%Y) $(date +%H:%M) el usuario $whoami ha solicitado un informe" >> /tmp/logeventos
echo "--------------------------------------"
