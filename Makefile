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
	rm -rf dist
	@echo "Compilando el sitio."
	make compilar
	@echo "Clonando repositorio para realizar el deploy."
	git clone --depth 1 dokku@hugoruscitti.com.ar:examplelab dist/
	@echo "Moviendo archivos..."
	@cp -r public/* dist/
	@echo "Realizando deploy..."
	@cd dist; git add .; git config user.email "hugoruscitti@gmail.com"; git config user.name "Hugo Ruscitti"; git commit -am 'rebuild' --allow-empty; git push -f
	rm -rf public
	rm -rf dist
	@echo "${G}Listo, se hizo el deploy en https://examplelab.com.ar${N}"
