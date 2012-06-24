Summary:	Paint program for X
Summary(de):	Malprogramm f�r X
Summary(es):	Programa de dise�o para X
Summary(fr):	Programme de dessin sous X
Summary(pl):	Program do rysowania pod X Window
Summary(pt_BR):	Programa de desenho para X
Summary(tr):	X alt�nda boyama program�
Name:		xpaint
Version:	2.6.2
Release:	4
License:	MIT
Group:		X11/Applications/Graphics
Source0:	http://www.image.dk/~torsten/xpaint/%{name}-%{version}.tar.gz
# Source0-md5:	9f22460f15a189721573d88454ce3d41
Source1:	%{name}.desktop
Source2:	%{name}.png
#Icon:		xpaint.xpm
URL:		http://www.image.dk/~torsten/xpaint/
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPaint is a color image editing tool which features most standard
paint program options, as well as advanced features such as image
processing algorithms. It allows for the editing of multiple images
simultaneously and supp

%description -l de
XPaint ist ein Farbbildbearbeitungs-Tool mit den meisten �blichen,
aber auch erweiterten Funktionen wie Bildverarbeitungsalgorithmen. Sie
k�nnen mehrere Bilder gleichzeitig bearbeiten.

%description -l es
XPaint es una herramienta de edici�n de im�genes coloridas que
presenta la mayor�a de las opciones padr�n de programas de pintura,
as� como caracter�sticas avanzadas como procesamiento de im�genes a
trav�s de algoritmos. Tambi�n permite la edici�n de m�ltiples im�genes
simult�neamente.

%description -l fr
xpaint est un outil d'�dition d'images en couleur offrant la plupart
des options du programme paint, ainsi que des caract�ristiques
avanc�es comme des algorithmes de traitement d'image. Il permet
l'�dition simultan�e de plusieurs images et plus.

%description -l pl
XPaint jest programem do edycji kolorowych grafik z funkcjami jakie ma
wi�kszo�� typowych program�w tego typu, a tak�e niekt�re bardziej
zaawansowane funkcje, jak r�ne algorytmy obr�bki grafiki.

%description -l pt_BR
XPaint � uma ferramenta de edi��o de imagens coloridas que apresenta a
maioria das op��es-padr�o de programas de pintura, assim como
caracter�sticas avan�adas como processamento de imagens atrav�s de
algoritmos. Ele tamb�m permite a edi��o de m�ltiplas imagens
simultaneamente.

%description -l tr
XPaint, X ortam�nda en temel resimleme yeteneklerini bar�nd�ran basit
bir programd�r.

%prep
%setup -q -n %{name}

%build
xmkmf
%{__make} Makefiles
%{__make} \
	CC=%{__cc} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags} `pkg-config --cflags libpng12 2>/dev/null`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/CHANGES README README.PNG TODO Doc/Operator.doc ChangeLog Doc/sample.Xdefaults
%attr(755,root,root) %{_bindir}/xpaint
%{_libdir}/X11/app-defaults/XPaint
%{_mandir}/man1/*
%{_applnkdir}/Graphics/xpaint.desktop
%{_pixmapsdir}/*
