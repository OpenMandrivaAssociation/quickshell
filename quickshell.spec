%bcond_with         asan

%global commit      eabf79ebb640dbfab6a3ff4639db65e64e05d941
%global snapdate    20250319

Name:               quickshell
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            3
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Group:		Graphical desktop/Other
BuildSystem: cmake
BuildOption: -DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption: -DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES
BuildOption: -DDISTRIBUTOR="Open Mandriva LX"
BuildOption: -DINSTALL_QMLDIR=%{_qtdir}/qml
BuildOption: -DWAYLAND_WLR_LAYERSHELL=OFF
BuildOption: -DWAYLAND_SESSION_LOCK=OFF

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6Quick)
BuildRequires:      cmake(Qt6QuickControls2)
BuildRequires:      cmake(Qt6Widgets)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      gcc-c++
BuildRequires:      ninja
BuildRequires:      pkgconfig(breakpad)
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(gbm)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libdrm)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      pkgconfig(wayland-scanner)
BuildRequires:      spirv-tools

Requires:      pkgconfig(breakpad)
Requires:      pkgconfig(CLI11)
Requires:      pkgconfig(gbm)
Requires:      pkgconfig(jemalloc)
Requires:      pkgconfig(libdrm)
Requires:      pkgconfig(libpipewire-0.3)
Requires:      pkgconfig(pam)
Requires:      pkgconfig(wayland-client)
Requires:      pkgconfig(wayland-protocols)
Requires:      pkgconfig(wayland-scanner)
Requires:      spirv-tools
Requires:      pkgconfig(Qt6Core)
Requires:      pkgconfig(Qt6Qml)
Requires:      pkgconfig(Qt6Quick)
Requires:      pkgconfig(Qt6QuickControls2)
Requires:      pkgconfig(Qt6Widgets)
Requires:      pkgconfig(wayland-client)

%description

%prep
%autosetup -n %{name}-%{commit} -p1

%files
%license LICENSE LICENSE-GPL
%doc BUILD.md CONTRIBUTING.md README.md
%{_bindir}/qs
%{_bindir}/quickshell
%{_qtdir}/*
