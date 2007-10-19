Summary:	Image from/to X-Face conversion utilities
Name:		compface
Version:	1.5.2
Release:	%mkrel 1
License:	MIT
Group:		Graphics
Source0:	http://freshmeat.net/redir/compface/1439/url_tgz/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Compface provides utilities to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%package devel
Summary:	Image from/to X-Face conversion libraries
Group:		Development/Libraries

%description devel
Compface provides a library to convert from/to X-Face format, a 48x48
bitmap format used to carry thumbnails of email authors in a mail
header.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}{%{_bindir},%{_mandir}/{man1,man3},%{_libdir},%{_includedir}}

install compface %{buildroot}%{_bindir}
install uncompface %{buildroot}%{_bindir}
install compface.1 %{buildroot}%{_mandir}/man1
install compface.3 %{buildroot}%{_mandir}/man3
install libcompface.a %{buildroot}%{_libdir}
install compface.h %{buildroot}%{_includedir}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/compface.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcompface.a
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*
