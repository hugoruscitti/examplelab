N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

all:
	@echo ""
	@echo "${B}Comandos disponibles${N}"
	@echo ""
	@echo "    ${G}ejecutar${N}                   ejecuta el modo servidor sin mostrar borradores."
	@echo "    ${G}ejecutar_con_borradores${N}    ejecuta el modo servidor mostrando borradores."
	@echo "    ${G}compilar${N}                   genera todos los archivos estáticos."
	@echo "    ${G}deploy${N}                     sube el sitio para que esté online."
	@echo ""
	@echo ""


ejecutar:
	@echo "${G}Ejecutando el servidor en http://localhost:1313/ ...${N}"
	hugo serve --disableLiveReload

ejecutar_con_borradores:
	@echo ${G}"Ejecutando el servidor (con borradores) en http://localhost:1313/ ...${N}"
	hugo serve --disableLiveReload -D

compilar:
	hugo

deploy: 
	@echo "Compilando el sitio."
	git pull origin master
	hugo -d docs
	git add docs
	git commit -am "actualizando archivos .html"
	git push origin master
	@echo "${G}Listo, se hizo el deploy en https://www.examplelab.com.ar${N}"
