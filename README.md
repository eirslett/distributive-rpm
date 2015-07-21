# distributive-rpm
RPM source for Distributive, with example health checks based on the software
included in Microservices Infrastructure.

## Structure

All static checklists should be installed to `/usr/share/distributive/`, with
samples in `/usr/share/distributive/samples`. The static checklists can be
symlinked by their individual roles into `/etc/distributive.d/`.

## Build Procedure
```shell
$ git clone https://github.com/CiscoCloud/distributive-rpm.git
$ cd distributive-rpm
$ vagrant up
```
should take care of it. This sets up a synced folder with the VM's `~/rpmbuild`
directory, so the RPMs build will be copied automatically to the host. If you're
interested in how this works, take a look at the Vagrantfile and provision.sh.

You can either build a snapshot or a release; changing the variable at the top
of provision.sh changes which Vagrant will build.

## RPM Build
RPM build target is RHEL6/7, Fedora >17; x86_64, i386 systems. The binary RPMs
should install on most RPM systems without issue. Its common to perform the
build process as dummy user.

## Contributing
This RPM is in a stable condition. Head over to [Distributive] [distributive]
or [Microservices-Infrastructure] [MI] to see how you can help!

[distributive]: https://github.com/CiscoCloud/distributive
[MI]: https://github.com/CiscoCloud/microservices-infrastructure/
