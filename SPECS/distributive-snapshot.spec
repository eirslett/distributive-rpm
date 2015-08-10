Name:           distributive
Version:        master
Release:        20150720git.master%{?dist}
Summary:        Distributive was designed with Consul in mind to perform distributed health checks in datacenters

License:        ASL 2.0:
URL:            https://github.com/CiscoCloud/distributive
Source0:        https://github.com/CiscoCloud/distributive/archive/master.zip

BuildRequires:  golang
#Requires:
# Debug info isn't really needed at this time
%global debug_package %{nil}

%description
Distributive is a tool for running distributed health checks in datacenters. It was designed with Consul in mind, but is platform agnostic. It is simple to configure (with JSON checklists) and easy to deploy and run. It has no dependencies, and can be shipped as a speedy 4MB (yes, megabytes!) binary.


%prep
%setup -qn %{name}-%{version}

%build
./build.sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
cp -p bin/%{name} %{buildroot}%{_bindir}/%{name}
cp -p %{_sourcedir}/*.json %{buildroot}%{_datadir}/%{name}/
cp -pr samples/ %{buildroot}%{_datadir}/%{name}/

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/%{name}/chronos.json
%{_datadir}/%{name}/collectd.json
%{_datadir}/%{name}/common.json
%{_datadir}/%{name}/consul.json
%{_datadir}/%{name}/consul-template.json
%{_datadir}/%{name}/dnsmasq.json
%{_datadir}/%{name}/docker.json
%{_datadir}/%{name}/haproxy.json
%{_datadir}/%{name}/iptables.json
%{_datadir}/%{name}/logrotate.json
%{_datadir}/%{name}/logstash.json
%{_datadir}/%{name}/marathon.json
%{_datadir}/%{name}/mesos.json
%{_datadir}/%{name}/nginx.json
%{_datadir}/%{name}/vault.json
%{_datadir}/%{name}/zookeeper.json
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
%{_datadir}/%{name}/samples/usage-fail.json
%{_datadir}/%{name}/samples/usage.json
%{_datadir}/%{name}/samples/users-and-groups-fail.json
%{_datadir}/%{name}/samples/users-and-groups.json
%{_sysconfdir}/%{name}.d/

%changelog
# 19-Jun-15: Updated Version to 0.1.1
# 25-Jun-15: Updated Version to 0.1.2
# 07-Jul-15: Updated Version to 0.2, updated %files to match
# 10-JUL-15: Updated prep and build to use new src file hierarchy and gvp
