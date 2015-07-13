# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.box = "centos/7"
  config.vm.hostname = "mi-rpmbuild"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "1536"
     vb.name = "mi-rpmbuild"
  end

  config.vm.provision "file", source: "~/.gitconfig", destination: ".gitconfig"
  config.vm.provision "shell", privileged: false, path: "provisioning/setup_mi-rpmbuild.sh" 

end
