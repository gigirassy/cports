pkgname = "dracut-install"
pkgver = "110"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-dracut-cpio"]
configure_gen = []
make_dir = "."
make_build_target = "dracut-install"
hostmakedepends = ["bash", "pkgconf"]
makedepends = ["chimerautils-devel", "kmod-devel"]
checkdepends = ["asciidoc"]
pkgdesc = "Dracut-install command from dracut"
license = "GPL-2.0-or-later"
url = "https://github.com/dracut-ng/dracut-ng"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0d357853f8cf2371d89a8ebcbbb1fd2c1c85a79d8866925fd7385eaeb20a27dc"
hardening = ["vis", "cfi"]
# assumes rw filesystem
options = ["!check"]


def install(self):
    self.install_file("dracut-install", "usr/lib/dracut", mode=0o755)
