Summary:	Old version of AfterStep Window Manager (NeXTalike)
Summary(pl):	Stara wersja zarz�dcy okien AfterStep
Name:		AfterStep10
Version:	1.0
Release:	1
License:	GPL
Source0:	ftp://ftp.afterstep.org/archives/1.0/AfterStep-%{version}.tar.gz
Source1:	%{name}-system.steprc
Patch0:		%{name}-linux_alpha.patch
Patch1:		%{name}-cool3.patch
URL:		http://www.afterstep.org/
Group:		X11/Window Managers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         afterstep       afterstep10

%description
This is old 1.0 version of AfterStep Window Manager. AfterStep is a
continuation of the BowMan WM. It uses modified FVWM code to bring you
a very NeXTStep-ish experience in X Window System. However, it doesn't
stop there, and can be extended beyond just being a simple NeXTStep
clone.

This version includes Rob Malda's cool3.diff

%description -l pl
To jest stara wersja 1.0 zarz�dcy okien AfterStep. AfterStep jest
kontynuacj� BowMan WM. U�ywa zmodyfikowanego kodu FVWM aby dotarczy�
Ci odczucia podobne do NeXTStepa pod X Window System. To nie wszystko.
AfterStep mo�e by� rozszerzony, aby by� czym� wi�cej ni� prostym
klonem NeXTStepa.

Ta wersja zawiera cool3.diff Roba Maldy.

%prep
%setup -q -n AfterStep-%{version}
%ifos Linux
%patch0
%endif
%patch1 -R -p5

%build
./MakeMakefiles
%{__make} CDEBUGFLAGS="%{rpmcflags}" all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11 \
	$RPM_BUILD_ROOT/%{_datadir}/%{afterstep}/{pixmaps,backgrounds}

install afterstep/afterstep $RPM_BUILD_ROOT%{_bindir}/%{afterstep}
install afterstep/afterstep.man $RPM_BUILD_ROOT%{_mandir}/man1/%{afterstep}.1x

AS_MODULES="Wharf Pager asclock"

for m in $AS_MODULES; do
    install modules/$m/$m $RPM_BUILD_ROOT%{_bindir}/as10-$m
    install modules/$m/$m.man $RPM_BUILD_ROOT%{_mandir}/man1/as10-$m.1x
done

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{afterstep}.rc

install icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{afterstep}/pixmaps
install backgrounds/* $RPM_BUILD_ROOT%{_datadir}/%{afterstep}/backgrounds

gzip -9nf CHANGES CREDITS FAQ README README.8bit module-interface.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_sysconfdir}/X11/%{afterstep}.rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{afterstep}
