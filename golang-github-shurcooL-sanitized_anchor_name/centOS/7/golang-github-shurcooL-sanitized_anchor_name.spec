# The tests are disabled by default.
# Set --with tests or bcond_without to run tests.
# Original behaviour is preserved.
%bcond_with tests

%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         shurcooL
%global repo            sanitized_anchor_name
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          8e87604bec3c645a4eeaee97dfec9f25811ff20d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gccgo_version  >= 5
%global golang_version >= 1.2.1-3 

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.sgit%{shortcommit}%{?dist}
# Be ahead of Fedora
Epoch:          1
Summary:        Package sanitized_anchor_name provides a func to create sanitized anchor names
License:        MIT
URL:            https://%{import_path}
Source0:        %{name}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel

BuildRequires: golang %{?golang_version}
Requires: golang %{?golang_version} 
Summary:        %{summary}
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{name}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/

%if %{with tests}
%check
%endif

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Thu Feb 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git8e87604
- First package for Fedora
  resolves: #1196551
