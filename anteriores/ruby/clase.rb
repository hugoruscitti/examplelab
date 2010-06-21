class Animal
    def respirar
        puts "estoy respirando"
    end
end

class Persona < Animal
    def saludar_a(otra_persona, mas)
        puts "hola #{otra_persona}, ¿como estás?"
    end
end


toto = Persona.new()
toto.saludar_a "pepe", "toto"
toto.respirar
