pkgname = "hashcat"
pkgver = "7.1.2"
pkgrel = 0
build_style = "makefile"
make_env = {
    "PREFIX": "/usr",
    "SED": "/usr/bin/gsed",
    "USE_SYSTEM_ZLIB": "1",
    "USE_SYSTEM_OPENCL": "1",
    "USE_SYSTEM_XXHASH": "1",
}
make_use_env = True
hostmakedepends = ["gsed"]
makedepends = [
    "linux-headers",
    "minizip-devel",
    "opencl-headers",
    "xxhash-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Password recovery tool"
license = "MIT"
url = "https://hashcat.net/hashcat"
source = f"https://hashcat.net/files/hashcat-{pkgver}.tar.gz"
sha256 = "9546a6326d747530b44fcc079babad40304a87f32d3c9080016d58b39cfc8b96"
# check: no obvious test suite
options = ["!check"]


if self.profile().endian == "big":
    broken = "bug endian"


def post_install(self):
    self.install_license("docs/license.txt")
