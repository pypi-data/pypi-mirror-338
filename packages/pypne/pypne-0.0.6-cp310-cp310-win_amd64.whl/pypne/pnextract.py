import numpy as np
from pathlib import Path
import os
import sys
from contextlib import contextmanager, nullcontext, redirect_stdout
from .libcpp import pypne_cpp


@contextmanager
def suppress_stdout():
    """彻底屏蔽所有 stdout（Python + C/C++）"""
    original_stdout_fd = sys.stdout.fileno()
    original_stdout = os.dup(original_stdout_fd)
    null_fd = os.open(os.devnull, os.O_WRONLY)

    try:
        os.dup2(null_fd, original_stdout_fd)
        with open(os.devnull, "w") as f, redirect_stdout(f):
            yield  # 执行代码
    finally:
        os.dup2(original_stdout, original_stdout_fd)
        os.close(null_fd)
        os.close(original_stdout)


_true_set = {"yes", "true", "t", "y", "1"}
_false_set = {"no", "false", "f", "n", "0"}


def str2bool(value, raise_exc=False):
    if isinstance(value, bool):
        return value
    if (
        isinstance(value, str)
        or sys.version_info[0] < 3
        and isinstance(value, basestring)
    ):
        value = value.lower()
        if value in _true_set:
            return True
        if value in _false_set:
            return False

    if raise_exc:
        raise ValueError('Expected "%s"' % '", "'.join(_true_set | _false_set))
    return None


def pnextract(image, resolution=1.0, config_settings=None, verbose=False):
    Path_cwd = Path.cwd()
    """
    write_Statoil:false,
    write_radius:false,
    write_elements:false,
    write_hierarchy:false,
    write_throatHierarchy:false,
    write_vtkNetwork:false,
    write_throats:false,
    write_poreMaxBalls:false,
    write_throatMaxBalls:false,
    
    
    output_path : path to output file, using default value "./pn(with desired suffix)"
    
    minRPore: minimum radius of pore, using default value _minRp=min(1.25, avgR*0.25)+0.5 
    
    medialSurfaceSettings: medial surface settings, using the following default values:
    _clipROutx=0.05;
	_clipROutyz=0.98;
	_midRf=0.7;
	_MSNoise=1.*abs(_minRp)+1.;
	_lenNf=0.6;
	_vmvRadRelNf=1.1;
	_nRSmoothing=3;
	_RCorsnf=0.15;
	_RCorsn=abs(_minRp);

    If you wants to set medialSurfaceSettings, you should use config_settings like this:
    config_settings['medialSurfaceSettings'] = "_clipROutx _clipROutyz _midRf _MSNoise _lenNf _vmvRadRelNf _nRSmoothing _RCorsnf _RCorsn"
    change the arguments to values you want.
    """
    default_config = {
        "write_Statoil": False,
        "write_radius": False,
        "write_elements": False,
        "write_hierarchy": False,
        "write_throatHierarchy": False,
        "write_vtkNetwork": False,
        "write_throats": False,
        "write_poreMaxBalls": False,
        "write_throatMaxBalls": False,
        "write_all": False,
        "output_path": (Path_cwd).resolve(),
        "name": "pn",
        "minRPore": None,
        "medialSurfaceSettings": None,
    }

    if config_settings is not None:
        default_config.update(config_settings)
    default_config = {k: v for k, v in default_config.items() if v is not None}
    default_config = {str(k): str(v) for k, v in default_config.items()}
    if str2bool(default_config["write_all"]):
        for k in default_config:
            if k.startswith("write_"):
                default_config[k] = "true"
    anything2write = any(
        str2bool(default_config[k]) for k in default_config if k.startswith("write_")
    )
    if anything2write:
        os.makedirs(default_config["output_path"], exist_ok=True)
        default_config["output_path"] = os.path.join(
            default_config["output_path"], default_config["name"]
        )
        default_config.pop("name")
    else:
        default_config.pop("output_path")
        default_config.pop("name")
    image = image.astype(np.uint8)
    nz, ny, nx = image.shape
    # 直接根据 verbose 决定是否使用 suppress_stdout
    with suppress_stdout() if not verbose else nullcontext():
        res = pypne_cpp.pnextract(
            nx, ny, nz, resolution, image.reshape(-1), default_config.copy()
        )
    image_VElems = res["VElems"].reshape(nz + 2, ny + 2, nx + 2)
    pn = res["pn"]
    print(default_config)
    if str2bool(default_config["write_elements"]):
        image_VElems.astype(np.int32, copy=False).tofile(
            default_config["output_path"] + "_VElems.raw"
        )
    return image_VElems, pn
