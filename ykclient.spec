%define	major 3
%define libname	%mklibname ykclient %{major}
%define develname %mklibname -d ykclient

Summary:	Implements online validation of Yubikey OTPs
Name:		ykclient
Version:	2.7
Release:	3
Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/yubico-c-client/
Source0:	http://yubico-c-client.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://yubico-c-client.googlecode.com/files/%{name}-%{version}.tar.gz.sig
BuildRequires:	autoconf automake libtool
BuildRequires:	chrpath
BuildRequires:	curl-devel

%description
This is a library written in C to validate a Yubikey OTP against the Yubico
online server.

%package -n	%{libname}
Summary:	Implements online validation of Yubikey OTPs
Group:          System/Libraries
Obsoletes:	%{mklibname libyubikey-client 0}

%description -n	%{libname}
This is a library written in C to validate a Yubikey OTP against the Yubico
online server.

%package -n	%{develname}
Summary:	Static library and header files for the libykclientt library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}
Obsoletes:	%{mklibname libyubikey-client -d}

%description -n	%{develname}
This is a library written in C to validate a Yubikey OTP against the Yubico
online server.

This package contains the static libyubikey-client library and its header files.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x \
    --with-libcurl=%{_prefix}

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

# nuke rpath
chrpath -d %{buildroot}%{_bindir}/ykclient

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files
%{_bindir}/ykclient

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon Dec 19 2011 Oden Eriksson <oeriksson@mandriva.com> 2.7-1
+ Revision: 743664
- 2.7
- various cleanups

* Wed Jun 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.6-1
+ Revision: 688181
- 2.6

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4-3
+ Revision: 671944
- mass rebuild

* Sun Mar 13 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4-2
+ Revision: 644242
- bump
- disable make check for now
- 2.4
- fix make check

* Sat Oct 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-4mdv2011.0
+ Revision: 586028
- rebuild

* Tue Oct 12 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-3mdv2011.0
+ Revision: 585119
- rebuild

* Thu Jun 11 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3-2mdv2010.0
+ Revision: 385135
- fix one stupid thing...
- obsolete the correct libs :-)
- import ykclient


* Thu Jun 11 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3-1mdv2009.0
- the project was renamed from libyubikey-client to ykclient

* Wed Mar 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdv2009.1
+ Revision: 357408
- 1.5

* Wed Sep 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2009.0
+ Revision: 285330
- 1.4
- drop upstream patches

* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2009.0
+ Revision: 284995
- revert to 1.2 due to version freeze
- add fixes from upstream svn
- 1.3

* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdv2009.0
+ Revision: 284923
- import libyubikey-client

* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdv2009.0
- initial Mandriva package
