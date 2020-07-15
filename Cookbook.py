#* Imports
import pycook.recipes.pip as pip
from pycook.recipes.pip import clean, sdist

#* Recipes
def pip_reinstall(recipe):
    res = []
    if pip.package_installed_p("touchpad"):
        res += [pip.uninstall("touchpad")]
    res += [pip.install(".")]
    return res

def publish(recipe):
    return sdist(recipe) + ["twine upload dist/*"] + clean(recipe)
