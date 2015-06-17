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

Then on the Microservices Infrastructure side, after this RPM is installed

 1. Create a [Consul health check configuration](https://github.com/CiscoCloud/microservices-infrastructure/blob/master/roles/consul/files/distributive-consul-config.json) in the `roles/<name>/files` directory.
 2. Add a [distributive.yml](https://github.com/CiscoCloud/microservices-infrastructure/blob/master/roles/consul/tasks/distributive.yml) file to the `tasks`.
 3. Include the .yml file in the `main.yml` file.
