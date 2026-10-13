try:
    from setuptools import find_packages, setup  # type: ignore[import-not-found]
except ModuleNotFoundError as exc:
    raise RuntimeError("Setuptools no está instalado. Instálalo con 'python -m pip install setuptools'.") from exc

# python setup.py sdist para ver las caracteristicas de este ejemplo
setup(
    name = "Utilities",
    version = "0.1",
    packages = find_packages(),
    description = "Matematicas y String",
    author = "Juan Mejia",
    author_email = "mi_correo@gmail.com"
)

#Instalar pip install twine
#twine upload dist/*