%global goipath github.com/GoogleCloudPlatform/gcping

Version: 0.0.3

%gometa

%global _docdir_fmt     %{name}

%global golicenses LICENSE
%global godocs *.md

%global common_description %{expand:
gcping is a command line tools that reports median latency to Google Cloud regions.
}

Name:    gcping
Release: 2%{?dist}
Summary: Foo
License: Apache Software License 2.0
URL:	 %{gourl}
Source0: %{gosource}
%description
%{common_description}

%gopkg

%prep
%setup -q -n %{name}-%{version}

%build
%gobuild -o %{gobuilddir}/bin/%{name}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/gcping

%changelog
* Sun Aug 25 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.3-2
- Change package name to gcping
- Clean spec
* Thu Aug 22 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.3-1
- First package for Fedora
