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
    return filter(touchpad_p, get_all_ids())

def set_touchpad_enabled(iid):
    print(lf("xinput enable {iid}"))
    return sc("xinput enable {iid}")

def set_touchpad_disabled(iid):
    print(lf("xinput disable {iid}"))
    return sc("xinput disable {iid}")

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
    if all([touchpad_enabled_p(x) for x in get_ids()]):
        disable_all_touchpads()
    else:
        enable_all_touchpads()
