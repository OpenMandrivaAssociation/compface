%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Image from/to X-Face conversion utilities
Name:		compface
Version:	1.5.2
Release:	%mkrel 5
License:	MIT
Group:		Graphics
Source0:	http://freshmeat.net/redir/compface/1439/url_tgz/%{name}-%{version}.tar.bz2
# originally from http://ftp.debian.org/debian/pool/main/libc/libcompface/libcompface_1.5.2-5.diff.gz
Patch0:         libcompface_1.5.2-5.diff
Patch2:         compface-1.5.2-build.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Compface provides utilities to convert from/to X-Face format, a 48x48 bitmap
format used to carry thumbnails of email authors in a mail header.

%package -n	%{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n	%{libname}
Compface provides utilities to convert from/to X-Face format, a 48x48 bitmap
format used to carry thumbnails of email authors in a mail header.

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} >= %{version}
Obsoletes:	%{name}-devel < 1.5.2-3
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Compface provides utilities to convert from/to X-Face format, a 48x48 bitmap
format used to carry thumbnails of email authors in a mail header.

This package provides the development files for %{name}.

%prep

%setup -q
%patch0 -p1
%patch2 -p0

%build
export CFLAGS="%{optflags} -fPIC"

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std STRIP=/bin/true

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README ChangeLog
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/compface.1*
%{_mandir}/man1/uncompface.1*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*
%{_mandir}/man3/uncompface.3*
