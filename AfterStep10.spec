Summary:	Old version of AfterStep Window Manager (NeXTalike)
Name:		AfterStep10
Version:	1.0
Release:	1
License:	GPL
Source0:	ftp://ftp.afterstep.org/archives/1.0/AfterStep-%{version}.tar.gz
Source1:	AfterStep10-system.steprc
Patch0:		AfterStep10-linux_alpha.patch
Patch1:		AfterStep10-cool3.patch
URL:		http://www.afterstep.org/
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         afterstep       afterstep10

%description 
This is old 1.0 version of AfterStep Window Manager.  AfterStep is a
continuation of the BowMan WM. It uses modified FVWM code to bring you
a very NeXTStep-ish experience in X Windows.  However, it doesn't stop
there, and can be extended beyond just being a simple NeXTStep clone.

This version includes Rob Malda's cool3.diff

%prep
%setup -q -n AfterStep-%{version}
%ifos Linux
%patch0
%endif
%patch1 -R -p5

%build
./MakeMakefiles
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS" all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}} \
           $RPM_BUILD_ROOT/etc/X11/ \
   	   $RPM_BUILD_ROOT/%{_datadir}/%{afterstep}/{pixmaps,backgrounds}

install -s afterstep/afterstep $RPM_BUILD_ROOT%{_bindir}/%{afterstep}
gzip -9nfc afterstep/afterstep.man > $RPM_BUILD_ROOT%{_mandir}/man1/%{afterstep}.1x.gz

AS_MODULES="Wharf Pager asclock"

for m in $AS_MODULES; do 
    install -s modules/$m/$m $RPM_BUILD_ROOT%{_bindir}/as10-$m
    gzip -9nfc modules/$m/$m.man > $RPM_BUILD_ROOT%{_mandir}/man1/as10-$m.1x.gz
done

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/%{afterstep}.rc

install -d $RPM_BUILD_ROOT%{_datadir}/%{afterstep}/pixmaps
install icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{afterstep}/pixmaps

install -d $RPM_BUILD_ROOT%{_datadir}/%{afterstep}/backgrounds
install backgrounds/* $RPM_BUILD_ROOT%{_datadir}/%{afterstep}/backgrounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS FAQ README README.8bit module-interface.txt
%config /etc/X11/%{afterstep}.rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.gz
%{_datadir}/%{afterstep}
