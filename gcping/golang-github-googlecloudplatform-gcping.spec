%global goipath github.com/GoogleCloudPlatform/gcping

Version: 0.0.3

%gometa

%global _docdir_fmt     %{name}

%global golicenses LICENSE
%global godocs *.md
%global godevelheader %{expand:
# The devel package will usually benefit from corresponding project binaries.
}

%global common_description %{expand:
}

# If one of the produced binaries is widely known it should be used to name the
# package instead of “goname”. Separate built binaries in different subpackages
# if needed.
Name:    %{goname}
Release: 1%{?dist}
Summary: Foo
License: APache
URL:	 %{gourl}
Source0: %{gosource}
%description
%{common_description}

%gopkg

%prep
%setup -q -n gcping-%{version}

%build
%gobuild -o %{gobuilddir}/bin/gcping


#%prep
#%goprep github.com/GoogleCloudPlatform/gcping
#%generate_buildrequires
#%go_generate_buildrequires
#%gobuild

#%goprep


%install
#%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

#%gofilelist

%check
#%gocheck github.com/GoogleCloudPlatform/gcping

#%files
#%license %{golicenses}
#%doc

%files
%license LICENSE
%doc README.md
%{_bindir}/gcping

#%gopkgfiles

%changelog
* Thu Aug 22 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.3-1
- First package for Fedora
