palabras_disponibles = ['perro', 'gato', 'liebre']
palabra = palabras_disponibles[rand(3)]

print "intente adivinar entre las siguientes palabras:\n"

for p in palabras_disponibles
    print "\t" + p + "\n"
end

print ">> "
elige = STDIN.gets
elige.chop!

if palabra == elige
    print "Has ganado !"
else
    print "Lo siento, no has adivinado\n"
    print "la palabra oculta era " + palabra
end

