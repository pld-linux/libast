Summary:	Library of Assorted Spiffy Things
Summary(pl):	Biblioteka AST (Assorted Spiffy Things)
Name:		libast
Version:	0.4
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
URL:		http://www.eterm.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	glibc-devel
BuildRequires:	imlib2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibAST is the Library of Assorted Spiffy Things. It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions. It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%description -l pl
LibAST to biblioteka Assorted Spiffy Things. Zawiera ró¿ne podrêczne
procedury i zastêpniki niektórych dobrych, ale nie przeno¶nych
funkcji. Aktualnie ma wbudowany system ¶ledzenia pamiêci, trochê
pomocy odpluskwiaj±cych i parê podobnych narzêdzi.

%package devel
Summary:	Library of Assorted Spiffy Things header files
Summary(pl):	Pliki nag³ówkowe biblioteki AST
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libast.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do libast.

%package static
Summary:	Libast static libraries
Summary(pl):	Biblioteki statyczne libast
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Libast static libraries.

%description devel -l pl
Biblioteki statyczne libast.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libast-test
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
