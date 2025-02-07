Name:           valent
Version:        1.0.0alpha
Release:        0
Summary:        Connect, control and sync devices
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
Url:            https://github.com/andyholmes/valent/tree/main

Source0:        %{name}-%{version}.tar.gz


BuildRequires:  meson >= 0.59.0
BuildRequires:  fdupes
BuildRequires:  vala
BuildRequires:  gcc-c++ 
BuildRequires:  cmake
BuildRequires:  sed
BuildRequires:  desktop-file-utils
BuildRequires:  pkg-config
BuildRequires:  sassc
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gnutls) >= 3.1.3
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6.0
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.24.0
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libebook-1.2) >= 3.34
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.0
BuildRequires:  pkgconfig(sysprof-capture-4) >= 3.38
BuildRequires:  pkgconfig(libwalbottle-0) >= 0.3.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  typelib(Peas)
BuildRequires:  cmake(libphonenumber)


Recommends: valent-lang
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define soname 1-1_0_0

%package -n libvalent-devel
Summary: Development library for valent
Requires: libvalent-%{soname} = %{version}
%description -n libvalent-devel
Development library for valent.

%package -n libvalent-%{soname}
Summary: Library for valent
%description -n libvalent-%{soname}
Library for valent.

%package -n typelib-1_0-libvalent-%{soname}
Summary: Typelib for valent
%description -n typelib-1_0-libvalent-%{soname}
Typelib for valent.

%package -n valent-lang
BuildArch: noarch
Summary: Languages for valent
%description -n valent-lang
Languages for valent.

%description
Securely connect your devices to open files and links where you need them, get notifications when you need them, stay in control of your media and more.

Features:

Sync contacts, notifications and clipboard content
Control media players and volume
Share files, links and text
Virtual touchpad and keyboard
Call and text notification
Execute custom commands

Valent is an implementation of the KDE Connect protocol, built on GNOME platform libraries.


%prep
%setup -q
sed "s~libportal_version = .*~libportal_version = '>= 0.5'~" -i meson.build

%build
%meson
sed 's/--pkg=libpeas-2/--pkg=Peas-2/' -i %{_vpath_builddir}/build.ninja
%meson_build

%post -n libvalent-%{soname} -p /sbin/ldconfig
%postun -n libvalent-%{soname} -p /sbin/ldconfig

%install
%meson_install
rm -R '%{buildroot}%{_datadir}/locale/ru*' || :
%fdupes %{buildroot}

%files
%doc README.md
%license LICENSE*
%{_sysconfdir}/xdg/**/*
%{_bindir}/valent
%{_datadir}/dbus-1/**/*
%{_datadir}/glib-2.0/**/*
%{_datadir}/icons/**/*
%{_datadir}/metainfo/*
%{_datadir}/applications/*
%dir %{_datadir}/applications
%dir %{_datadir}/metainfo
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/dbus-1

%files -n valent-lang
%{_datadir}/locale/**/*
%dir %{_datadir}/locale

%files -n typelib-1_0-libvalent-%{soname}
%{_libdir}/girepository-1.0/*

%files -n libvalent-%{soname}
%{_libdir}/*.so.*

%files -n libvalent-devel
%{_includedir}/**/*
%dir %{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/vala/**/*
%dir %{_libdir}/pkgconfig
%dir %{_datadir}/vala
%{_datadir}/gir-1.0/*
%dir %{_datadir}/gir-1.0

%changelog

