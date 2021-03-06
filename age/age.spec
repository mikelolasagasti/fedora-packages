%global goipath github.com/FiloSottile/age
%global goforgeurl https://github.com/FiloSottile/age
%global commit 7ef2aa8a4ed365916d75b8d92ca15323b6d7de0d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%gometa

Version: 0

%global _docdir_fmt     %{name}

%global golicenses LICENSE
%global godocs *.md

%global common_description %{expand:
A simple, secure and modern encryption tool with small explicit keys, no config options, and UNIX-style composability.}

Name:    age
Release: 0.0.%{shortcommit}%{?dist}
Summary: A simple, secure and modern encryption tool with small explicit keys, no config options, and UNIX-style composability.
License: New BSD
URL:     %{gourl}
Source0: %{gosource}

BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/crypto/poly1305)
BuildRequires:  golang(golang.org/x/crypto/scrypt)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)

Requires:  golang(golang.org/x/crypto/curve25519)

%description
%{common_description}

%gopkg

%prep
%goprep

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/cmd/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall

%gocheck

%gopkgfiles


%changelog
* Sat Nov 30 2019 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.0-1
- First package for Fedora
