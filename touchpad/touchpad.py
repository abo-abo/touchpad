#* Imports
import re
import time
import pycook.elisp as el
sc = el.sc
lf = el.lf

#* Functions
def get_all_ids():
    xinput = sc("xinput --list")
    return el.re_seq("id=([0-9]+)", xinput)

def touchpad_p(iid):
    xinput = sc("xinput --list-props {iid}").lower()
    return re.search("touchpad", xinput, re.IGNORECASE)

def get_ids():
    return el.cl_remove_if_not(touchpad_p, get_all_ids())

def set_touchpad_enabled(iid):
    return sc("xinput set-prop {iid} \"Device Enabled\" 1")

def set_touchpad_disabled(iid):
    return sc("xinput set-prop {iid} \"Device Enabled\" 0")

def touchpad_props(iid):
    return sc("xinput --list-props {iid}")

def touchpad_name(iid):
    return touchpad_props(iid).split("\n")[0][:-1]

def touchpad_enabled_p(iid):
    props = touchpad_props(iid)
    m = re.search("device enabled[^:]*:\s*([01])", props, re.IGNORECASE)
    return m.group(1) == "1"

def disable_all_touchpads():
    for iid in get_ids():
        print("Disabling: ", touchpad_name(iid))
        set_touchpad_disabled(iid)
        time.sleep(1)

def enable_all_touchpads():
    for iid in get_ids():
        print("Enabling:", touchpad_name(iid))
        set_touchpad_enabled(iid)
        time.sleep(1)

def main():
    if all(el.mapcar(touchpad_enabled_p, get_ids())):
        disable_all_touchpads()
    else:
        enable_all_touchpads()
