%define url_ver %(echo %{version} | cut -d. -f 1,2)

Summary:	Time-managing application for Xfce desktop environment
Name:		orage
Version:	4.20.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://www.xfce.org
Source0:	http://archive.xfce.org/src/apps/orage/%{url_ver}/%{name}-%{version}.tar.bz2
#Patch1:		orage-4.12.1-libical3.patch
BuildRequires:	chrpath
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libical)
BuildRequires:	dbus-glib-devel
BuildRequires:	dbus-devel
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	popt-devel
BuildRequires:	bison
BuildRequires:	flex
Provides:	xfcalendar = %{version}
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
%autopatch -p1

%build
%define Werror_cflags %nil

%configure \
	--disable-static \
	--enable-reentrant \
	--enable-dbus \
	--enable-archive \
	--enable-libnotify \
	--enable-libxfce4panel

%make_build

%install
%make_install

#disable rpath in _bin
chrpath -d %{buildroot}/%{_bindir}/*

rm -rf %{buildroot}%{_datadir}/orage/doc

%find_lang %{name} %{name}.lang

desktop-file-install \
  --add-only-show-in="XFCE" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc README.md AUTHORS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/themes/Default/orage-4.0/gtk.css
%dir %{_datadir}/orage
%{_datadir}/orage/sounds/
%{_datadir}/dbus-1/services/org.xfce.*.service
%{_datadir}/metainfo/org.xfce.orage.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/*
%{_iconsdir}/hicolor/scalable/apps/*
