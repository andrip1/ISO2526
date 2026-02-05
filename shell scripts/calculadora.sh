#!/bin/bash
# 04/02/2026
# Andrés Ballester Lozano

clear

if [ $# -ne 2 ]; then
    echo "Uso: $0 <fichero> <repeticiones>"
    exit 1
fi

fichero=$1
repeticiones=$2
contador=0

if ! [[ $repeticiones =~ ^[0-9]+$ ]]; then
    echo "Error: el segundo parámetro debe ser un número"
    exit 1
fi

if [ -f "$fichero" ]; then
    echo "Error, el fichero existe"
    exit 1
fi

echo "Autor: Andrés Ballester"

while [ $contador -lt $repeticiones ]; do

    read -p "Añada dos valores: " op1 op2

    echo "------------------"
    echo "SUMA S"
    echo "RESTA R"
    echo "MULTIPLICACIÓN M"
    echo "DIVISIÓN D"
    echo "SALIR X"
    echo "------------------"

    read -p "Seleccione operación: " operacion

    case $operacion in
        S)
            resultado=$((op1 + op2))
            echo "S $op1 $op2" >> "$fichero"
            echo "Resultado: $resultado"
            ;;
        R)
            resultado=$((op1 - op2))
            echo "R $op1 $op2" >> "$fichero"
            echo "Resultado: $resultado"
            ;;
        M)
            resultado=$((op1 * op2))
            echo "M $op1 $op2" >> "$fichero"
            echo "Resultado: $resultado"
            ;;
        D)
            if [ "$op2" -eq 0 ]; then
                echo "Error: división entre 0"
            else
                resultado=$((op1 / op2))
                echo "D $op1 $op2" >> "$fichero"
                echo "Resultado: $resultado"
            fi
            ;;
        X)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción no válida"
            ;;
    esac

    echo
    contador=$((contador + 1))

done
