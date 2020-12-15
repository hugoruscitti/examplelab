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
	rm -rf public
	@echo "Compilando el sitio."
	make compilar
	@echo "Creando directiva para deployar en dokku..."
	touch public/.static
	@echo "Realizando deploy..."
	@cd public; git init; git add .; git config user.email "hugoruscitti@gmail.com"; git config user.name "Hugo Ruscitti"; git commit -am 'rebuild' --allow-empty; git remote add origin dokku@examplelab.com.ar:examplelab; git push --set-upstream origin master -f
	rm -rf public
	@echo "${G}Listo, se hizo el deploy en https://examplelab.examplelab.com.ar${N}"
