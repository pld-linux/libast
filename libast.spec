#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library of Assorted Spiffy Things
Summary(pl.UTF-8):	Biblioteka AST (Assorted Spiffy Things)
Name:		libast
Version:	0.7
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	a9ec3b2da317f35869316e6d9571d296
URL:		http://www.eterm.org/
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibAST is the Library of Assorted Spiffy Things. It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions. It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%description -l pl.UTF-8
LibAST to biblioteka Assorted Spiffy Things. Zawiera różne podręczne
procedury i zastępniki niektórych dobrych, ale nie przenośnych
funkcji. Aktualnie ma wbudowany system śledzenia pamięci, trochę
pomocy odpluskwiających i parę podobnych narzędzi.

%package devel
Summary:	Library of Assorted Spiffy Things header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AST
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	imlib2-devel
Requires:	pcre-devel

%description devel
Header files and development documentation for libast.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do libast.

%package static
Summary:	Libast static libraries
Summary(pl.UTF-8):	Biblioteki statyczne libast
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Libast static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libast.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libast.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libast.so.2

%files devel
%defattr(644,root,root,755)
%doc DESIGN
%attr(755,root,root) %{_bindir}/libast-config
%attr(755,root,root) %{_libdir}/libast.so
%{_libdir}/libast.la
%{_includedir}/libast*
%{_aclocaldir}/libast.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libast.a
%endif
