class Libro:
    """Representa un librp con titulo, autor y año de publicacion."""

    def __init__(self, titulo, autor, año):
        """Inicializa un libro con sus detalles.
        Args:
            titulo (str): El titulo del libro.
            autor (str): El autor del libro.
             año (int): El año de publicaion. """
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def descripcion(self):
        """Devuelve una descripcion brebe del libro
        returns:
            str: Descripcion en formato 'titulo, por autor (año)'"""
        return f"{self.titulo}, por {self.autor} ({self.año})"