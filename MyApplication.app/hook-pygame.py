import os
def _append_to_datas(file_path):
    res_path = os.path.join(pygame_folder, file_path)
    if os.path.exists(res_path):
        datas.append((res_path, "pygame"))


# First append the font file, then based on the OS, append pygame icon file
_append_to_datas("freesansbold.ttf")
if platform.system() == "Darwin":
    _append_to_datas("pygame_icon_mac.bmp")
else:
    _append_to_datas("pygame_icon.bmp")

if platform.system() == "Windows":
    from PyInstaller.utils.hooks import collect_dynamic_libs

    pre_binaries = collect_dynamic_libs("pygame")
    binaries = []