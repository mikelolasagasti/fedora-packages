%global srcname pingfs
%global commit f2f2b5ff1893d0531d0a0d1ea2ae96b52dcf780e
%global snapinfo 2020524git%{shortcommit}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    fuse-pingfs
Version: 0.1
Release: 1.%{snapinfo}%{?dist}
Summary:  Stores your data in ICMP ping packets

License: ISC
URL:     https://github.com/yarrick/pingfs
Source0: https://github.com/yarrick/pingfs/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(fuse)

%description
pingfs is a filesystem where the data is stored only in the Internet itself, as
ICMP Echo packets (pings) travelling from you to remote servers and back again.

%prep
%autosetup -n pingfs-%{commit}

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a pingfs %{buildroot}%{_bindir}/pingfs

%files
%{_bindir}/pingfs

%doc README
%license LICENSE

%changelog
* Thu Aug 20 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 20200820
- Initial version of the package
