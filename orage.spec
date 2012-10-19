%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Time-managing application for Xfce desktop environment
Name:		orage
Version:	4.8.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/orage/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	chrpath
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libical)
BuildRequires:	dbus-glib-devel
BuildRequires:	dbus-devel
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	popt-devel
BuildRequires:	bison
BuildRequires:	flex
Provides:	xfcalendar
Obsoletes:	xfcalendar < 4.5

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
	--enable-libxfce4panel

%make

%install
%makeinstall_std

#disable rpath in _bin
chrpath -d %{buildroot}/%{_bindir}/*

rm -rf %{buildroot}%{_datadir}/orage/doc

%find_lang %{name} %{name}.lang

desktop-file-install \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc README AUTHORS
%doc doc/C/images/*.png doc/C/orage.html
%{_bindir}/*
%{_libdir}/xfce4
%{_datadir}/applications/*
%{_datadir}/xfce4/panel-plugins/xfce4-orageclock-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_iconsdir}/hicolor/*/apps/*.xpm
%dir %{_datadir}/orage
%{_datadir}/orage/sounds/
%{_datadir}/dbus-1/services/org.xfce.*.service
%{_mandir}/man1/*.*
