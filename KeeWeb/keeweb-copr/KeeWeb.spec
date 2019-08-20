%define __requires_exclude libffmpeg.so

Name:    KeeWeb
Version: 1.9.1
Release: 1%{?dist}
Summary: Free cross-platform password manager compatible with KeePass 
URL:     https://github.com/keeweb/keeweb
License: MIT
BuildRequires: desktop-file-utils

Source0: https://github.com/keeweb/keeweb/releases/download/v%{version}/KeeWeb-%{version}.linux.x64.zip
Source1: %{name}.desktop


%description
Free cross-platform password manager compatible with KeePass 

%prep
%autosetup -c KeeWeb-%{version}

%install
mkdir -p %{buildroot}/opt
cp -r ../KeeWeb-%{version} %{buildroot}/opt/KeeWeb-%{version}
install -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/applications/KeeWeb.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/KeeWeb.desktop

%files
/opt/KeeWeb-%{version}/*
%{_datadir}/applications/KeeWeb.desktop

%changelog
* Tue Aug 21 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.9.1-1
- Version bump
* Fri May 3 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.8.2-1
- Version bump
- Fix desktop file
* Sat Apr 6 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.8.1-1
- Version bump
* Sun Mar 31 2019 Mikel Olasagasti <mikel@olasagasti.info> - 1.8.0-2
- Fix desktop icon path
* Sun Mar 31 2019 Mikel Olasagasti <mikel@olasagasti.info> - 1.8.0-1
- Version bump
* Mon Jun 12 2017 Mikel Olasagasti <mikel@olasagasti.info> - 1.5.4-1
- Version bump
* Sat Mar 11 2017 Philipp Baum <phil@phib.io> - 1.4.0-3
- Changed installdir to /opt
* Sat Mar 11 2017 Philipp Baum <phil@phib.io> - 1.4.0-2
- Added Desktop-file
* Sat Mar 11 2017 Philipp Baum <phil@phib.io> - 1.4.0-1
- Initial package build
