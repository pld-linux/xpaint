Summary:	paint program for X
Summary(de):	Malprogramm f�r X
Summary(fr):	Programme de dessin sous X
Summary(pl):	Program do rysowania pod X Window
Summary(tr):	X alt�nda boyama program�
Name:		xpaint
Version:	2.5.6
Release:	2
Copyright:	MIT
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
URL:            http://www.danbbs.dk/~torsten/xpaint/
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/graphics/draw/%{name}-%{version}.tar.gz
Patch:		xpaint-config.patch
Icon:		xpaint.gif
BuildPrereq:	XFree86-devel
BuildPrereq:    xpm-devel
BuildPrereq:    libjpeg-devel
BuildPrereq:    libtiff-devel
BuildPrereq:    libpng-devel
BuildPrereq:    zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
XPaint is a color image editing tool which features most standard paint
program options, as well as advanced features such as image processing
algorithms.  It allows for the editing of multiple images simultaneously and
supp

%description -l de
XPaint ist ein Farbbildbearbeitungs-Tool mit den meisten �blichen, aber auch
erweiterten Funktionen wie Bildverarbeitungsalgorithmen. Sie k�nnen mehrere
Bilder gleichzeitig bearbeiten.

%description -l fr
xpaint est un outil d'�dition d'images en couleur offrant la plupart des
options du programme paint, ainsi que des caract�ristiques avanc�es comme
des algorithmes de traitement d'image. Il permet l'�dition simultan�e de
plusieurs images et plus.

%description -l pl
XPaint jest programem do edycji kolorowych grafik z funkcjami jakie ma
wi�kszo�� typowych program�w tego typu, a tak�e niekt�re bardziej
zaawansowane funkcje, jak r�ne algorytmy obr�bki grafiki. 

%description -l tr
Xpaint, X ortam�nda en temel resimleme yeteneklerini bar�nd�ran basit bir
programd�r.

%prep
%setup -q -n %{name}
%patch -p0

%build
xmkmf
make Makefiles
make \
	CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT \
        MANDIR=%{_mandir}/man1 \
        BINDIR=%{_bindir} \
        install install.man


cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name} <<EOF
%{name} name "%{name}"
%{name} description "Paint Program"
%{name} group Graphics
%{name} exec "%{name} &"
EOF

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	Doc/CHANGES README README.PNG TODO Doc/Operator.doc ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Doc/CHANGES,README,README.PNG,TODO,ChangeLog,Doc/Operator.doc}.gz
%doc Doc/sample.Xdefaults
%attr(755,root,root) %{_bindir}/%{name}

/etc/X11/wmconfig/%{name}
%{_libdir}/X11/app-defaults/XPaint
%{_mandir}/man1/*

%changelog
* Thu May 20 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [2.5.6-2]
- package is FHS 2.0 compliant,
- spec file based on RH version; rewritten for PLD use by me 
  and Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>.
