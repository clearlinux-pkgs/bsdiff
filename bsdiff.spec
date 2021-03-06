#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : bsdiff
Version  : 1.0.4
Release  : 21
URL      : https://github.com/clearlinux/bsdiff/releases/download/v1.0.4/bsdiff-1.0.4.tar.xz
Source0  : https://github.com/clearlinux/bsdiff/releases/download/v1.0.4/bsdiff-1.0.4.tar.xz
Summary  : Library for bsdiff
Group    : Development/Tools
License  : BSD-2-Clause
Requires: bsdiff-bin = %{version}-%{release}
Requires: bsdiff-lib = %{version}-%{release}
Requires: bsdiff-license = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)

%description
This project is a forked version of BSDiff, as taken from the Chromium project
Significant changes after the fork include:

%package bin
Summary: bin components for the bsdiff package.
Group: Binaries
Requires: bsdiff-license = %{version}-%{release}

%description bin
bin components for the bsdiff package.


%package dev
Summary: dev components for the bsdiff package.
Group: Development
Requires: bsdiff-lib = %{version}-%{release}
Requires: bsdiff-bin = %{version}-%{release}
Provides: bsdiff-devel = %{version}-%{release}
Requires: bsdiff = %{version}-%{release}

%description dev
dev components for the bsdiff package.


%package lib
Summary: lib components for the bsdiff package.
Group: Libraries
Requires: bsdiff-license = %{version}-%{release}

%description lib
lib components for the bsdiff package.


%package license
Summary: license components for the bsdiff package.
Group: Default

%description license
license components for the bsdiff package.


%package staticdev
Summary: staticdev components for the bsdiff package.
Group: Default
Requires: bsdiff-dev = %{version}-%{release}

%description staticdev
staticdev components for the bsdiff package.


%prep
%setup -q -n bsdiff-1.0.4
cd %{_builddir}/bsdiff-1.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604904310
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure  --disable-tests
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604904310
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bsdiff
cp %{_builddir}/bsdiff-1.0.4/COPYING %{buildroot}/usr/share/package-licenses/bsdiff/d12260c3adb41cb31e2fc1a41ca84ac7c523beef
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bsdiff
/usr/bin/bsdump
/usr/bin/bspatch

%files dev
%defattr(-,root,root,-)
/usr/include/bsdiff.h
/usr/lib64/libbsdiff.so
/usr/lib64/pkgconfig/bsdiff.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbsdiff.so.1
/usr/lib64/libbsdiff.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bsdiff/d12260c3adb41cb31e2fc1a41ca84ac7c523beef

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbsdiff.a
