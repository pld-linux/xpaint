Summary:	paint program for X
Summary(de):	Malprogramm für X
Summary(es):	Programa de diseño para X
Summary(fr):	Programme de dessin sous X
Summary(pl):	Program do rysowania pod X Window
Summary(pt_BR):	Programa de desenho para X
Summary(tr):	X altýnda boyama programý
Name:		xpaint
Version:	2.6.2
Release:	3
License:	MIT
Group:		X11/Applications/Graphics
Source0:	http://www.image.dk/~torsten/xpaint/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Icon:		xpaint.xpm
URL:		http://www.image.dk/~torsten/xpaint/
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_mandir		%{_prefix}/man

%description
XPaint is a color image editing tool which features most standard
paint program options, as well as advanced features such as image
processing algorithms. It allows for the editing of multiple images
simultaneously and supp

%description -l de
XPaint ist ein Farbbildbearbeitungs-Tool mit den meisten üblichen,
aber auch erweiterten Funktionen wie Bildverarbeitungsalgorithmen. Sie
können mehrere Bilder gleichzeitig bearbeiten.

%description -l es
XPaint es una herramienta de edición de imágenes coloridas que
presenta la mayoría de las opciones padrón de programas de pintura,
así como características avanzadas como procesamiento de imágenes a
través de algoritmos. También permite la edición de múltiples imágenes
simultáneamente.

%description -l fr
xpaint est un outil d'édition d'images en couleur offrant la plupart
des options du programme paint, ainsi que des caractéristiques
avancées comme des algorithmes de traitement d'image. Il permet
l'édition simultanée de plusieurs images et plus.

%description -l pl
XPaint jest programem do edycji kolorowych grafik z funkcjami jakie ma
wiêkszo¶æ typowych programów tego typu, a tak¿e niektóre bardziej
zaawansowane funkcje, jak ró¿ne algorytmy obróbki grafiki.

%description -l pt_BR
XPaint é uma ferramenta de edição de imagens coloridas que apresenta a
maioria das opções-padrão de programas de pintura, assim como
características avançadas como processamento de imagens através de
algoritmos. Ele também permite a edição de múltiplas imagens
simultaneamente.

%description -l tr
Xpaint, X ortamýnda en temel resimleme yeteneklerini barýndýran basit
bir programdýr.

%prep
%setup -q -n %{name}

%build
xmkmf
%{__make} Makefiles
%{__make} \
	CC=%{__cc} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
        MANDIR=%{_mandir}/man1 \
        BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf Doc/CHANGES README README.PNG TODO Doc/Operator.doc ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/*.gz *.gz Doc/sample.Xdefaults
%attr(755,root,root) %{_bindir}/xpaint
%{_libdir}/X11/app-defaults/XPaint
%{_mandir}/man1/*
%{_applnkdir}/Graphics/xpaint.desktop
%{_pixmapsdir}/*
