Summary:	Library of Assorted Spiffy Things
Name:		libast
Version:	0.3
Release:	2
License:	BSD
Group:		Libraries		
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
URL:		http://www.eterm.org/
BuildRequires:	freetype1-devel
BuildRequires:	XFree86-devel
BuildRequires:	imlib2-devel
BuildRequires:	glibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibAST is the Library of Assorted Spiffy Things. It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions. It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

%package devel
Summary:	Library of Assorted Spiffy Things
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libast.

%package static
Summary:	Libast static libraries
Summary(pl):	Biblioteki statyczne libast
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Libast static libraries.

%description devel -l pl
Biblioteki statyczne libast.


%prep
%setup -q

%build
  %configure2_13 --prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir} --includedir=%{_includedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog README

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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
