#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bsdiff
Version  : 1.0.0
Release  : 1
URL      : https://github.com/clearlinux/bsdiff/releases/download/v1.0.0/bsdiff-1.0.0.tar.xz
Source0  : https://github.com/clearlinux/bsdiff/releases/download/v1.0.0/bsdiff-1.0.0.tar.xz
Summary  : Library for bsdiff
Group    : Development/Tools
License  : BSD-2-Clause
Requires: bsdiff-bin
Requires: bsdiff-lib
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

%description bin
bin components for the bsdiff package.


%package dev
Summary: dev components for the bsdiff package.
Group: Development
Requires: bsdiff-lib
Requires: bsdiff-bin
Provides: bsdiff-devel

%description dev
dev components for the bsdiff package.


%package lib
Summary: lib components for the bsdiff package.
Group: Libraries

%description lib
lib components for the bsdiff package.


%prep
%setup -q -n bsdiff-1.0.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
