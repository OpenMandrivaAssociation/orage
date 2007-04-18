#%define svn     svn_r20246
#%define svnr    r20246
%define __libtoolize /bin/true

Summary: 	Time-managing application for Xfce
Name: 		orage
Version: 	4.4.1
Release: 	%mkrel 1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	%{name}-%{version}.tar.bz2
Group: 		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:  xfce-mcs-manager-devel >= 4.3.0
BuildRequires:	chrpath
BuildRequires:	dbh-devel 
BuildRequires:  xfce-panel-devel
BuildRequires:  desktop-file-utils
Provides:	xfcalendar
Obsoletes:	xfcalendar

%description
Orage is a time-managing application for the Xfce desktop environment, 
featuring:
- Time-based events
- Data stored in ical format.
- Recurring appointments
- Reminder up to 2 days before the event starts
- Possibility to choose your alarm sound
- Repeating the alarm sound until you close the reminder window
- Possibility to duplicate an appointment
- Archiving system for keeping your history in different files for
  avoiding overloads in the main working file.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 

#disable rpath in _bin
chrpath -d $RPM_BUILD_ROOT/%{_bindir}/*

#rm unneeded file
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/xfce4/mcs-plugins/*.*a
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/orage/doc

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang 
%defattr(-,root,root)
%doc README ChangeLog INSTALL COPYING AUTHORS
%doc doc/C/images/*.png doc/C/orage.html
%{_bindir}/*
%{_libdir}/xfce4
%{_datadir}/applications/*
%{_datadir}/xfce4/panel-plugins/orageclock.desktop
%{_datadir}/icons/*
%dir %{_datadir}/orage
%{_datadir}/orage/sounds/
%{_datadir}/orage/zoneinfo


