class libro :
    def __init__(self,titulo,autor,año):
        self.titulo=titulo
        self.autor=autor
        self.año=año

    def mostrar_infor(self):
        print(f"el titulo es │{self.titulo}│,el autor es │{self.autor}│, │{self.año}│")
#creamos instancia 
mi_libro=libro("Tesla","ezrea","1870")
mi_libro.mostrar_infor()
        
        
