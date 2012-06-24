Summary:	Library of Assorted Spiffy Things
Summary(pl):	Biblioteka AST (Assorted Spiffy Things)
Name:		libast
Version:	0.4
Release:	2
License:	BSD
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	A�ger�as�fn
Group(it):	Librerie
Group(ja):	�饤�֥��
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(sl):	Knji�nice
Group(sv):	Bibliotek
Group(uk):	��̦�����
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
LibAST to biblioteka Assorted Spiffy Things. Zawiera r�ne podr�czne
procedury i zast�pniki niekt�rych dobrych, ale nie przeno�nych
funkcji. Aktualnie ma wbudowany system �ledzenia pami�ci, troch�
pomocy odpluskwiaj�cych i par� podobnych narz�dzi.

%package devel
Summary:	Library of Assorted Spiffy Things header files
Summary(pl):	Pliki nag��wkowe biblioteki AST
Group:		X11/Development/Libraries
Group(cs):	X11/V�vojov� prost�edky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(is):	X11/�r�unart�l/A�ger�as�fn
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/��ȯ/�饤�֥��
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(sl):	X11/Razvoj/Knji�nice
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libast.

%description devel -l pl
Pliki nag��wkowe i dokumentacja programisty do libast.

%package static
Summary:	Libast static libraries
Summary(pl):	Biblioteki statyczne libast
Group:		X11/Development/Libraries
Group(cs):	X11/V�vojov� prost�edky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(is):	X11/�r�unart�l/A�ger�as�fn
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/��ȯ/�饤�֥��
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(sl):	X11/Razvoj/Knji�nice
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/��������/��̦�����
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
autoconf
automake -a -c
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
