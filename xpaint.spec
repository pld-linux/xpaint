Summary:	paint program for X
Summary(de):	Malprogramm für X
Summary(fr):	Programme de dessin sous X
Summary(pl):	Program do rysowania pod X Window
Summary(tr):	X altýnda boyama programý
Name:		xpaint
Version:	2.5.7
Release:	1
Copyright:	MIT
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/graphics/draw/%{name}-%{version}.tar.gz
Source1:	xpaint.desktop
Patch:		xpaint-config.patch
Icon:		xpaint.gif
URL:            http://home.worldonline.dk/~torsten/xpaint/index.html
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define 	_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

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

%description -l pl
XPaint jest programem do edycji kolorowych grafik z funkcjami jakie ma
wiêkszo¶æ typowych programów tego typu, a tak¿e niektóre bardziej
zaawansowane funkcje, jak ró¿ne algorytmy obróbki grafiki. 

%description -l tr
Xpaint, X ortamýnda en temel resimleme yeteneklerini barýndýran basit bir
programdýr.

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
install -d $RPM_BUILD_ROOT%{_sysconfdir}/applnk/Graphics

make DESTDIR=$RPM_BUILD_ROOT \
        MANDIR=%{_mandir}/man1 \
        BINDIR=%{_bindir} \
        install install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/applnk/Graphics

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	Doc/CHANGES README README.PNG TODO Doc/Operator.doc ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Doc/CHANGES,README,README.PNG,TODO,ChangeLog,Doc/Operator.doc}.gz
%doc Doc/sample.Xdefaults

%attr(755,root,root) %{_bindir}/xpaint

%{_sysconfdir}/applnk/Graphics/xpaint.desktop
%{_libdir}/X11/app-defaults/XPaint
%{_mandir}/man1/*
