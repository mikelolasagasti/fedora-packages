%define __requires_exclude libffmpeg.so

Name:    KeeWeb
Version: 1.12.1
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
cp -r ../KeeWeb-%{version} %{buildroot}/opt/KeeWeb
install -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/applications/KeeWeb.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/KeeWeb.desktop

%files
/opt/KeeWeb/*
%{_datadir}/applications/KeeWeb.desktop

%changelog
* Sun Oct 27 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.12.1-1
- Version bump
* Thu Oct 17 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.11.10-1
- Version bump
* Sat Oct 12 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.11.8-1
- Version bump
* Sun Oct 5 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.11.6-1
- Version bump
* Mon Sep 30 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.11.5-1
- Version bump
* Sat Sep 21 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.10.1-1
- Version bump
* Sun Sep 15 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.10.0-1
- Version bump
* Fri Aug 23 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.9.2-1
- Version bump
* Wed Aug 21 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.9.1-2
- Change install path to be version agnostic
* Wed Aug 21 2019 Mikel Olasagasti <mikel@olasagsati.info> - 1.9.1-1
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
