Summary:	X Damage extension library
Name:		xorg-libXdamage
Version:	1.1.4
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdamage-%{version}.tar.bz2
# Source0-md5:	0cf292de2a9fa2e9a939aefde68fd34f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Damage extension library.

%package devel
Summary:	Header files for libXdamage library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Damage extension library.

This package contains the header files needed to develop programs that
use libXdamage.

%prep
%setup -qn libXdamage-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXdamage.so.?
%attr(755,root,root) %{_libdir}/libXdamage.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXdamage.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xdamage.pc

