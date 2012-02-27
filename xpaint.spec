Summary:	Paint program for X
Summary(de.UTF-8):	Malprogramm für X
Summary(es.UTF-8):	Programa de diseño para X
Summary(fr.UTF-8):	Programme de dessin sous X
Summary(pl.UTF-8):	Program do rysowania pod X Window
Summary(pt_BR.UTF-8):	Programa de desenho para X
Summary(tr.UTF-8):	X altında boyama programı
Name:		xpaint
Version:	2.9.9
Release:	1
License:	MIT
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
# Source0-md5:	7a30a7855c32fdad84f6ee19297dd540
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://sourceforge.net/projects/sf-xpaint/
BuildRequires:	libxaw3dxft-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libtiff-devel
BuildRequires:	openjpeg-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel >= 3.4c
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/etc/X11/app-defaults

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
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.PNG TODO Doc/Operator.doc ChangeLog Doc/sample.Xdefaults
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
%{_mandir}/man1/imgmerge.1*
%{_mandir}/man1/pdfconcat.1*
%{_desktopdir}/xpaint.desktop
%{_pixmapsdir}/xpaint.png
