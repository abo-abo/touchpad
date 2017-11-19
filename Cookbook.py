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

def publish(recipe):
    return ["rm -rf dist/",
            "python3 setup.py sdist",
            "twine upload dist/*"]

def clean(recipe):
    return ["rm -rf dist",
            "rm -rf *.egg-info"]
