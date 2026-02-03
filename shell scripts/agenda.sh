#
#
# Andrés Ballester

while true; do 
echo "MENÚ"
echo "A añadir entrada"
echo "B buscar por dni"
echo "C ver agenda completa"
echo "D eliminar todas las entradas de la agenda"
echo "E finalizar"
read -p "Elige una opción " opcion

case $opcion in 
	A)
		read -p "introduzca el dni de la persona " dni 
		if [ grep "$dni" agenda.txt ]; then 
			echo "la persona está registrada"
		else
			echo "Persona no registrada"
			read -p "introduzca nombre " nombre
			read -p "introduzca apellidos " apellidos
			read -p "introduzca localidad " localidad
			echo "$dni":"$nombre":"$apellidos":"$localidad" >> agenda.txt
			echo >> agenda.txt
			echo "Datos añadidos a agenda.txt"
		fi

		;;
	B)
		read -p "introduzca dni" dni
		if [ grep -q "$dni" agenda.txt ]; then 
			grep "$dni" agenda.txt
		else
			echo "dni no existe"

		fi
		;;
	C)	
		if [ -s agenda.txt  ]; then 
			cat agenda.txt
		else
		echo "agenda vacia"
		fi

		;;

	D) 
		truncate -s 0 agenda.txt
		;;

	E) 
		echo "saliendo"
		exit

		;;

esac
done
