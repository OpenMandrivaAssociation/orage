Summary:	Time-managing application for Xfce desktop environment
Name:		orage
Version:	4.5.93
Release:	%mkrel 1
License:	GPLv2+
URL:		http://www.xfce.org
Group:		Graphical desktop/Xfce
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	chrpath
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	libical-devel
BuildRequires:	libnotify-devel
Provides:	xfcalendar
Obsoletes:	xfcalendar < 4.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%setup -q

%build
%define Werror_cflags %nil

%configure2_5x \
	--disable-static \
	--enable-reentrant \
	--enable-dbus \
	--enable-archive \
	--enable-libnotify \
	--disable-libxfce4mcs
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#disable rpath in _bin
chrpath -d %{buildroot}/%{_bindir}/*

rm -rf %{buildroot}%{_datadir}/orage/doc

%find_lang %{name}

desktop-file-install \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%doc doc/C/images/*.png doc/C/orage.html
%{_bindir}/*
%{_libdir}/xfce4
%{_datadir}/applications/*
%{_datadir}/xfce4/panel-plugins/orageclock.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%dir %{_datadir}/orage
%{_datadir}/orage/sounds/
%{_datadir}/orage/zoneinfo
%{_datadir}/dbus-1/services/org.xfce.*.service
%{_mandir}/man1/*.*
   