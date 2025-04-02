"""
This module handles running OpenSCAD
"""
import sys
import os
import subprocess
from tempfile import gettempdir

def get_openscad_exe():
    """
    This returns the name of the openscad executable. It is needed as OpenSCAD is not
    on the path in MacOS.
    """
    if sys.platform.startswith("darwin"):
        return "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
    return "openscad"

def scad2csg(scadfile, scad_args):
    """
    Run openscad to convert a scad file into a csf file
    """
    tmpdir = gettempdir()
    scadfilename = os.path.basename(scadfile)
    csgfilename = scadfilename[:-4] + 'csg'
    csgfile = os.path.join(tmpdir, csgfilename)
    executable = get_openscad_exe()
    subprocess.run([executable] + [scadfile, '-o', csgfile] + scad_args, check=True)
    return csgfile

def csg2stl(csgfile):
    """
    Run OpenSCAD to convert a csg file into an STL
    """
    tmpdir = gettempdir()
    stlfile = os.path.join(
        tmpdir, os.path.basename(csgfile[:-3]) + 'stl'
    )
    executable = get_openscad_exe()
    try:
        command = [executable] + [csgfile, '-o', stlfile]
        subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(
            "\nError running subprocess: \n"
            f"{command}\n"
            f"STDERR: \n{e.stderr}\n"
            f"STDOUT: \n{e.stdout}\n"
            f"Return code: {e.returncode}\n"
        )
        raise
    os.remove(csgfile)
    return stlfile
