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

public_remoto:
	git clone dokku@examplelab.com.ar:examplelab public_remoto

deploy: public_remoto
	rm -rf public
	@echo "Compilando el sitio."
	make compilar
	@echo "Creando directiva para deployar en dokku..."
	touch public/.static
	@echo "Realizando deploy..."
	@cd public_remoto; git checkout -f; git pull
	@cp -r public/* public_remoto
	@cd public_remoto; git add .; git commit -am "rebuild"; git push origin master
	@rm -rf public
	@echo "${G}Listo, se hizo el deploy en https://examplelab.examplelab.com.ar${N}"
