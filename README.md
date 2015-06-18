# distributive-rpm
RPM source for Distributive, with example health checks based on the software
included in Microservices Infrastructure.

## Structure

All static checks should be installed to `/usr/share/distributive/`, and
copied by their individual roles into `/etc/distributive.d/`.

Consul health check configurations are copied to `/etc/consul/`.

## Contributing
To create a checklist for Microservices Infrastructure, the process is as
follows:

 1. Read the `roles/<name>/tasks/*.yml` files in Micoservices Infrastructure.
 2. For each task that gets run, create a [distributive check](https://github.com/CiscoCloud/distributive/wiki/Checks-and-Checklists).
 3. Think up and include any relevant checks for runtime.
 4. Check in the new definition file into the SOURCES directory.
 5. Add a line such as `%{_datadir}/%{name}/$YOURFILE.json` to the SPECS/distributive.spec %files section.

Then on the Microservices Infrastructure side, after this RPM is installed.

 1. Create a [Consul health check configuration](https://github.com/CiscoCloud/microservices-infrastructure/blob/master/roles/consul/files/distributive-consul-config.json) in the `roles/<name>/files` directory.
 2. Add a [distributive.yml](https://github.com/CiscoCloud/microservices-infrastructure/blob/master/roles/consul/tasks/distributive.yml) file to the `tasks`.
 3. Include the .yml file in the `main.yml` file.
 
## RPM Build
RPM build target is RHEL6/7, Fedora >17; x86_64, i386 systems. The binary RPMs should install on most RPM systems without issue. Its common to perform the build process as dummy user.
#### Build Procedure
######Build platform is CentOS >6, or Fedora >17
 1. Install rpmdevtools.
 2. Clone repo `git clone https://github.com/CiscoCloud/distributive-rpm.git ~/rpmbuild`.
 3. Run `rpmdev-setuptree`. This will create the rest of ~/rpmbuild structure.
 4. cd ~/rpmbuild, and run `spectool -R -g SPECS/distributive.spec`.
 5. Run `rpmbuild -ba SPECS/distributive.spec`. _There may be a few dup file warnings, safe to disregard_
