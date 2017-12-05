#* Imports
from pycook.elisp import sc

#* Functions
def pip3_package_installed_p(package):
    try:
        s = sc("pip3 show {package}")
        return s != ""
    except:
        return False

#* Recipes
def pip_reinstall(recipe):
    res = []
    if pip3_package_installed_p("touchpad"):
        res.append("sudo -H pip3 uninstall -y touchpad")
    res.append("sudo -H pip3 install .")
    return res

def sdist(recipe):
    return [
        "rm -rf dist/",
        "mv README.org README",
        "python setup.py sdist",
        "mv README README.org"]

def clean(recipe):
    return ["rm -rf dist *.egg-info"]

def publish(recipe):
    return sdist(recipe) + ["twine upload dist/*"] + clean(recipe)
