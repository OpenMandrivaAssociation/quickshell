%global commit      ed528268e0c0a2f6be2b5aca7089ebc3e214d446
%global quickshell_shortcommit %(c=%{commit}; echo ${c:0:7})
%global bumpver 1

Name:               quickshell
Version:            1~%{bumpver}.git%{quickshell_shortcommit}
Release:            1
Summary:            Flexible QtQuick based desktop shell toolkit
License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Group:              Window Manager/Bar

BuildSystem:    cmake
BuildOption:    -GNinja
BuildOption:    -DBUILD_SHARED_LIBS=OFF 
BuildOption:    -DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption:    -DDISTRIBUTOR="OpenMandriva LX"
BuildOption:    -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES
BuildOption:    -DINSTALL_QMLDIR="lib64/qt6/qml"
BuildOption:    -DINSTALL_QML_PREFIX="lib64/qt6/qml"

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Gui)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6Quick)
BuildRequires:      cmake(Qt6QuickControls2)
BuildRequires:      cmake(Qt6Widgets)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(breakpad)
BuildRequires:      pkgconfig(gbm)
BuildRequires:      pkgconfig(libdrm)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      cmake(Qt6QmlNetwork)
BuildRequires:      qt6-qtbase-theme-gtk3
BuildRequires:      cmake(Qt6QmlCore)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      pkgconfig(wlr-protocols)
BuildRequires:      spirv-tools

Requires:      pkgconfig(pam)

%description

%prep
%autosetup -n %{name}-%{commit} -p1

%files
%license LICENSE LICENSE-GPL
%{_bindir}/qs
%{_bindir}/quickshell
%{_qtdir}/qml/*
