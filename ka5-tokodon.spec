%define		kdeappsver	23.04.1
%define		qtver		5.15.2
%define		kaname		tokodon
Summary:	A modern Mastodon client
Name:		ka5-%{kaname}
Version:	23.04.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	98cb8e268ea079481807ce18a5edecd9
URL:		https://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Keychain-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.15.2
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebSockets-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.77.0
BuildRequires:	kf5-kauth-devel >= 5.105.0
BuildRequires:	kf5-kcodecs-devel >= 5.105.0
BuildRequires:	kf5-kcompletion-devel >= 5.105.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.105.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.105.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.77.0
BuildRequires:	kf5-ki18n-devel >= 5.77.0
BuildRequires:	kf5-kio-devel >= 5.77.0
BuildRequires:	kf5-kirigami2-devel >= 5.77.0
BuildRequires:	kf5-kitemviews-devel >= 5.105.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.105.0
BuildRequires:	kf5-knotifications-devel >= 5.77.0
BuildRequires:	kf5-kservice-devel >= 5.105.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.105.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.77.0
BuildRequires:	kf5-kxmlgui-devel >= 5.105.0
BuildRequires:	kf5-qqc2-desktop-style-devel
BuildRequires:	kf5-solid-devel >= 5.105.0
BuildRequires:	kirigami-addons-devel >= 0.7.2
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modern Mastodon(https://joinmastodon.org/) client.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

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
%{_desktopdir}/org.kde.tokodon.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.tokodon.svg
%{_datadir}/knotifications5/tokodon.notifyrc
%{_datadir}/metainfo/org.kde.tokodon.appdata.xml
%{_datadir}/qlogging-categories5/tokodon.categories
