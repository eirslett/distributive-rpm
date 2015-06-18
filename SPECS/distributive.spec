Name:		distributive
Version:	0.1
Release:	1%{?dist}
Summary:	Distributive was designed with Consul in mind to perform distributed health checks in datacenters

License:	ASL 2.0:
URL:		https://github.com/CiscoCloud/distributive
Source0:	https://github.com/CiscoCloud/distributive/archive/v0.1.tar.gz

BuildRequires:	golang

#Requires:	

%description
Distributive is a tool for running distributed health checks in datacenters. It was designed with Consul in mind, but is platform agnostic. It is simple to configure (with JSON checklists) and easy to deploy and run. It has no dependencies, and can be shipped as a speedy 4MB (yes, megabytes!) binary.


%prep
%setup -qn %{name}-%{version}
# Copy JSONs to builddir
#cp -p %%Source1 . 

%build
go build .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -p %{name}-%{version} %{buildroot}%{_bindir}/%{name}
cp -p ./*.json %{buildroot}%{_datadir}/%{name}/
cp -pr samples/ %{buildroot}%{_datadir}/%{name}/


%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/%{name}/samples/
%{_datadir}/%{name}/samples/docker-fail.json
%{_datadir}/%{name}/samples/docker.json
%{_datadir}/%{name}/samples/filesystem-fail.json
%{_datadir}/%{name}/samples/filesystem.json
%{_datadir}/%{name}/samples/misc-fail.json
%{_datadir}/%{name}/samples/misc.json
%{_datadir}/%{name}/samples/network-fail.json
%{_datadir}/%{name}/samples/network.json
%{_datadir}/%{name}/samples/packages-fail.json
%{_datadir}/%{name}/samples/packages.json
%{_datadir}/%{name}/samples/systemctl-fail.json
%{_datadir}/%{name}/samples/systemctl.json
%{_datadir}/%{name}/samples/users-and-groups-fail.json
%{_datadir}/%{name}/samples/users-and-groups.json
%{_sysconfdir}/%{name}/

%changelog

