Summary:	Time-managing application for Xfce desktop environment
Name:		orage
Version:	4.4.2
Release:	%mkrel 1
License:	GPLv2+
URL:		http://www.xfce.org
Group:		Graphical desktop/Xfce
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	chrpath
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	libdb4.2-devel
BuildRequires:	libical-devel
Provides:	xfcalendar
Obsoletes:	xfcalendar
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
%configure2_5x \
	--disable-static \
	--enable-reentrant \
	--with-bdb4
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

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

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
