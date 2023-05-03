
from pprint import pprint

import os
from parse_desc_file import parse_desc_file

path = "/var/lib/pacman/local/"

def local_package_descriptions():
    pkgs = []
    for pkg in os.listdir(path):
        if os.path.isdir("/".join([path, pkg])):
            pkgs.append(parse_desc_file("/".join([path, pkg, "desc"])))
    return pkgs

def desc_name(pkg_desc):
    return pkg_desc['NAME'][0]

def desc_name_version(pkg_desc):
    return (pkg_desc['NAME'][0], pkg_desc['VERSION'][0])

def pacmanQ(with_versions=False):
    return map(
        desc_name_version if with_versions else desc_name,
        local_package_descriptions()
    )

#TODO: use hashmap to avoid O(n^2) time
def have_pkgs(pkg_list):
    local_pkgs = pacmanQ()
    have = []
    need = []

    for pkg in pkg_list:
        if pkg in local_pkgs:
            have.append(pkg)
        else:
            need.append(pkg)

    return (have,need)

