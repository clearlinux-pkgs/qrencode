#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qrencode
Version  : 4.0.2
Release  : 1
URL      : https://fukuchi.org/works/qrencode/qrencode-4.0.2.tar.gz
Source0  : https://fukuchi.org/works/qrencode/qrencode-4.0.2.tar.gz
Summary  : A QR Code encoding library
Group    : Development/Tools
License  : LGPL-2.1
Requires: qrencode-bin
Requires: qrencode-lib
Requires: qrencode-license
Requires: qrencode-man
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libpng-dev
BuildRequires : pkgconfig(sdl2)

%description
libqrencode 4.0.2 - QR Code encoding library
GENERAL INFORMATION
===================
Libqrencode is a library for encoding data in a QR Code symbol, a 2D symbology
that can be scanned by handy terminals such as a mobile phone with CCD. The
capacity of QR Code is up to 7000 digits or 4000 characters and has high
robustness.

%package bin
Summary: bin components for the qrencode package.
Group: Binaries
Requires: qrencode-license
Requires: qrencode-man

%description bin
bin components for the qrencode package.


%package dev
Summary: dev components for the qrencode package.
Group: Development
Requires: qrencode-lib
Requires: qrencode-bin
Provides: qrencode-devel

%description dev
dev components for the qrencode package.


%package lib
Summary: lib components for the qrencode package.
Group: Libraries
Requires: qrencode-license

%description lib
lib components for the qrencode package.


%package license
Summary: license components for the qrencode package.
Group: Default

%description license
license components for the qrencode package.


%package man
Summary: man components for the qrencode package.
Group: Default

%description man
man components for the qrencode package.


%prep
%setup -q -n qrencode-4.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535166068
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1535166068
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qrencode
cp COPYING %{buildroot}/usr/share/doc/qrencode/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qrencode

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libqrencode.so
/usr/lib64/pkgconfig/libqrencode.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqrencode.so.4
/usr/lib64/libqrencode.so.4.0.2

%files license
%defattr(-,root,root,-)
/usr/share/doc/qrencode/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/qrencode.1