class Persona
    def set_nombre(nombre)
        @nombre = nombre
    end

    def presentarse
        if define? @nombre
            puts "hola, mi nombre es #{@nombre}"
        else
            puts "no me puedo presentar, aún no tengo asignado un nombre"
        end
    end
end


a = Persona.new
a.presentarse
a.set_nombre("pepe")
a.presentarse
