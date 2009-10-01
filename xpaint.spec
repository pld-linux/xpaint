Summary:	Paint program for X
Summary(de.UTF-8):	Malprogramm für X
Summary(es.UTF-8):	Programa de diseño para X
Summary(fr.UTF-8):	Programme de dessin sous X
Summary(pl.UTF-8):	Program do rysowania pod X Window
Summary(pt_BR.UTF-8):	Programa de desenho para X
Summary(tr.UTF-8):	X altında boyama programı
Name:		xpaint
Version:	2.8.2
Release:	1
License:	MIT
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
# Source0-md5:	e08b4d782f73da897a68794864193265
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://sf-xpaint.sourceforge.net/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel >= 3.4c
BuildRequires:	xorg-util-imake
BuildRequires:	xorg-util-gccmakedep
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/share/X11/app-defaults

%description
XPaint is a color image editing tool which features most standard
paint program options, as well as advanced features such as image
processing algorithms. It allows for the editing of multiple images
simultaneously and supp

%description -l de.UTF-8
XPaint ist ein Farbbildbearbeitungs-Tool mit den meisten üblichen,
aber auch erweiterten Funktionen wie Bildverarbeitungsalgorithmen. Sie
können mehrere Bilder gleichzeitig bearbeiten.

%description -l es.UTF-8
XPaint es una herramienta de edición de imágenes coloridas que
presenta la mayoría de las opciones padrón de programas de pintura,
así como características avanzadas como procesamiento de imágenes a
través de algoritmos. También permite la edición de múltiples imágenes
simultáneamente.

%description -l fr.UTF-8
xpaint est un outil d'édition d'images en couleur offrant la plupart
des options du programme paint, ainsi que des caractéristiques
avancées comme des algorithmes de traitement d'image. Il permet
l'édition simultanée de plusieurs images et plus.

%description -l pl.UTF-8
XPaint jest programem do edycji kolorowych grafik z funkcjami jakie ma
większość typowych programów tego typu, a także niektóre bardziej
zaawansowane funkcje, jak różne algorytmy obróbki grafiki.

%description -l pt_BR.UTF-8
XPaint é uma ferramenta de edição de imagens coloridas que apresenta a
maioria das opções-padrão de programas de pintura, assim como
características avançadas como processamento de imagens através de
algoritmos. Ele também permite a edição de múltiplas imagens
simultaneamente.

%description -l tr.UTF-8
XPaint, X ortamında en temel resimleme yeteneklerini barındıran basit
bir programdır.

%prep
%setup -q

%build
xmkmf
# to get stable results even if Xaw3d/neXtaw is installed
./configure xaw
%{__make} \
	CC="%{__cc}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	XPM_INCLUDE="-I/usr/include/X11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	CONFDIR=%{_datadir}/X11 \
	MANDIR=%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/CHANGES README README.PNG TODO Doc/Operator.doc ChangeLog Doc/sample.Xdefaults
%attr(755,root,root) %{_bindir}/imgmerge
%attr(755,root,root) %{_bindir}/xpaint
%attr(755,root,root) %{_bindir}/pdfconcat
%{_appdefsdir}/XPaint
%lang(es) %{_appdefsdir}/XPaint_es
%lang(fr) %{_appdefsdir}/XPaint_fr
%dir %{_datadir}/xpaint
%{_datadir}/xpaint/XPaintIcon.xpm
%{_datadir}/xpaint/c_scripts
%{_datadir}/xpaint/include
%dir %{_datadir}/xpaint/bin
%{_datadir}/xpaint/bin/xpaint_ocr
%dir %{_datadir}/xpaint/bitmaps
%{_datadir}/xpaint/bitmaps/brushbox.cfg
%dir %{_datadir}/xpaint/bitmaps/brushes
%{_datadir}/xpaint/bitmaps/brushes/*.xpm
%dir %{_datadir}/xpaint/bitmaps/elec
%{_datadir}/xpaint/bitmaps/elec/*.xpm
%dir %{_datadir}/xpaint/help
%{_datadir}/xpaint/help/Help
%lang(es) %{_datadir}/xpaint/help/Help_es
%lang(fr) %{_datadir}/xpaint/help/Help_fr
%dir %{_datadir}/xpaint/messages
%{_datadir}/xpaint/messages/Messages
%lang(es) %{_datadir}/xpaint/messages/Messages_es
%lang(fr) %{_datadir}/xpaint/messages/Messages_fr
%{_mandir}/man1/xpaint.1*
%{_desktopdir}/xpaint.desktop
%{_pixmapsdir}/xpaint.png
%{_libdir}/X11/app-defaults
