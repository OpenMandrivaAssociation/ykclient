%define	major 3
%define libname	%mklibname ykclient %{major}
%define develname %mklibname -d ykclient

Summary:	Implements online validation of Yubikey OTPs
Name:		ykclient
Version:	2.8
Release:	1
Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/yubico-c-client/
Source0:	http://yubico-c-client.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://yubico-c-client.googlecode.com/files/%{name}-%{version}.tar.gz.sig
BuildRequires:	autoconf automake libtool
BuildRequires:	chrpath
BuildRequires:	curl-devel

%description
This is a library written in C
to validate a Yubikey OTP against the Yubico
online server.

%package -n	%{libname}
Summary:	Implements online validation of Yubikey OTPs
Group:          System/Libraries
Obsoletes:	%{mklibname libyubikey-client 0}

%description -n	%{libname}
This is a library written in C
to validate a Yubikey OTP against the Yubico
online server.

%package -n	%{develname}
Summary:	Static library and header files for the libykclientt library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}
Obsoletes:	%{mklibname libyubikey-client -d}

%description -n	%{develname}
This is a library written in C to
validate a Yubikey OTP against the Yubico
online server.

This package contains the static
libyubikey-client library and its header files.

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
