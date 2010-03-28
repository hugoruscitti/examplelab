class Fruta

    def initialize(estado="madura")
        @estado = estado
    end
end

manzana = Fruta.new()
puts manzana.inspect

manzana = Fruta.new('podrida')
puts manzana.inspect
