%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kaname		tokodon
Summary:	A modern Mastodon client
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7a80160f86d18ea835878d672ad76f83
URL:		https://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Keychain-devel
BuildRequires:	Qt6Multimedia-devel
BuildRequires:	Qt6Network-devel >= 5.15.2
BuildRequires:	Qt6Qml-devel >= 5.15.9
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebSockets-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.77.0
BuildRequires:	kf6-kauth-devel >= 5.105.0
BuildRequires:	kf6-kcodecs-devel >= 5.105.0
BuildRequires:	kf6-kcompletion-devel >= 5.105.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.105.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.105.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.77.0
BuildRequires:	kf6-ki18n-devel >= 5.77.0
BuildRequires:	kf6-kio-devel >= 5.77.0
BuildRequires:	kf6-kirigami-devel >= 5.77.0
BuildRequires:	kf6-kitemviews-devel >= 5.105.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.105.0
BuildRequires:	kf6-knotifications-devel >= 5.77.0
BuildRequires:	kf6-kservice-devel >= 5.105.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.105.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.77.0
BuildRequires:	kf6-kxmlgui-devel >= 5.105.0
BuildRequires:	kf6-qqc2-desktop-style-devel
BuildRequires:	kf6-solid-devel >= 5.105.0
BuildRequires:	kirigami-addons-devel >= 0.7.2
BuildRequires:	mpv-client-devel
BuildRequires:	mpvqt-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern Mastodon(https://joinmastodon.org/) client.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%{?with_tests:%ninja_build test}

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tokodon
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/tokodonplugin.so
%{_desktopdir}/org.kde.tokodon.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.tokodon.svg
%{_iconsdir}/hicolor/scalable/actions/*.svg
%{_datadir}/knotifications6/tokodon.notifyrc
%{_datadir}/metainfo/org.kde.tokodon.appdata.xml
%{_datadir}/qlogging-categories6/tokodon.categories
