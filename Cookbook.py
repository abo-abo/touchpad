#* Imports
from pycook.recipes.pip import clean, sdist, reinstall

#* Recipes
def publish(recipe):
    return sdist(recipe) + ["twine upload dist/*"] + clean(recipe)
