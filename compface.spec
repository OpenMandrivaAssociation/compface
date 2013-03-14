%define major	1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Image from/to X-Face conversion utilities
Name:		compface
Version:	1.5.2
Release:	7
License:	MIT
Group:		Graphics
Url:		http://freecode.com/projects/compface
Source0:	http://ftp.xemacs.org/pub/xemacs/aux/%{name}-%{version}.tar.gz
# originally from http://ftp.debian.org/debian/pool/main/libc/libcompface/libcompface_1.5.2-5.diff.gz
Patch0:         libcompface_1.5.2-5.diff
Patch2:         compface-1.5.2-build.patch

%description
Compface provides utilities to convert from/to X-Face format, a 48x48 bitmap
format used to carry thumbnails of email authors in a mail header.

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
Compface provides utilities to convert from/to X-Face format, a 48x48 bitmap
format used to carry thumbnails of email authors in a mail header.

%package -n	%{devname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x

%make

%install
%makeinstall_std STRIP=/bin/true

%files
%doc README ChangeLog
%{_bindir}/*
%{_mandir}/man1/compface.1*
%{_mandir}/man1/uncompface.1*

%files -n %{libname}
%{_libdir}/libcompface.so.%{major}*

%files -n %{devname}
%{_libdir}/lib*.so
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*
%{_mandir}/man3/uncompface.3*

