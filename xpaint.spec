Summary:     paint program for X
Summary(de): Malprogramm für X
Summary(fr): Programme de dessin sous X
Summary(pl): Program do rysowania pod X Window
Summary(tr): X altýnda boyama programý
Name:        xpaint
Version:     2.5.6
Release:     1
Copyright:   MIT
Group:       X11/Applications/Graphics
Group(pl):   X11/Aplikacje/Grafika
Source:      ftp://sunsite.unc.edu/pub/Linux/apps/graphics/draw/%{name}-%{version}.tar.gz
Icon:        xpaint.gif
URL:         http://www.danbbs.dk/~torsten/xpaint/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
XPaint is a color image editing tool which features most standard paint
program options, as well as advanced features such as image processing
algorithms.  It allows for the editing of multiple images simultaneously and
supp

%description -l de
XPaint ist ein Farbbildbearbeitungs-Tool mit den meisten üblichen, aber auch
erweiterten Funktionen wie Bildverarbeitungsalgorithmen. Sie können mehrere
Bilder gleichzeitig bearbeiten.

%description -l fr
xpaint est un outil d'édition d'images en couleur offrant la plupart des
options du programme paint, ainsi que des caractéristiques avancées comme
des algorithmes de traitement d'image. Il permet l'édition simultanée de
plusieurs images et plus.

%description
XPaint jest programem do edycji kolorowych grafik z funkcjami jakie ma
wiêkszo¶c typowych programów tego typu a tak¿e niektóre bardziej
zaawansowane funkcje jak ró¿ne algorytmy obróbki grafiki. 

program options, as well as advanced features such as image processing
algorithms.  It allows for the editing of multiple images simultaneously and
supp

%description -l tr
Xpaint, X ortamýnda en temel resimleme yeteneklerini barýndýran basit bir
programdýr.

%prep
%setup -q -n xpaint

%build
xmkmf
make Makefiles
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpaint <<EOF
xpaint name "xpaint"
xpaint description "Paint Program"
xpaint group Graphics
xpaint exec "xpaint &"
EOF

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc Doc/CHANGES README README.PNG TODO Doc
%config /etc/X11/wmconfig/xpaint
%attr(755, root, root) /usr/X11R6/bin/xpaint
/usr/X11R6/lib/X11/app-defaults/XPaint
%attr(644, root,  man) /usr/X11R6/man/man1/*

%changelog
* Sun Nov 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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
