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

%define	_prefix		/usr/X11R6

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
* Tue May 11 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [2.5.6-2]
- added gzipping documentation,
- removed man group from man pages,
- removed %config from wmconfig file,
- fixed %description field,
- added xpaint-config.patch,
- added BuildPrereqs,
- cosmetic changes for common l&f,
- recompiled on rpm 3,
- package is FHS 2.0 compliant.

* Sun Nov 29 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5.6-1]
- added pl translation,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added gzipping man pages,
- added URL,
- added full %attr description in %files.

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- build root.

* Tue Jun 09 1998 Mike Wangsmo <wanger@redhat.com>
- changed the docs from being %config files.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- built against libpng 1.0

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new release
- wmconfig

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- "make install.man" places man page in wrong location
