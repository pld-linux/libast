Summary:	Library of Assorted Spiffy Things
Summary(pl):	Biblioteka AST (Assorted Spiffy Things)
Name:		libast
Version:	0.7
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	a9ec3b2da317f35869316e6d9571d296
URL:		http://www.eterm.org/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	pcre-devel
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
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libast.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do libast.

%package static
Summary:	Libast static libraries
Summary(pl):	Biblioteki statyczne libast
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Libast static libraries.

%description static -l pl
Biblioteki statyczne libast.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
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

%files devel
%defattr(644,root,root,755)
%doc DESIGN
%attr(755,root,root) %{_bindir}/libast-config
%attr(755,root,root) %{_libdir}/libast.so
%{_libdir}/libast.la
%{_includedir}/libast*
%{_aclocaldir}/libast.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libast.a
