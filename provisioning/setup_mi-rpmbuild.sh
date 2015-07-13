#!/bin/bash

sudo yum -q -y install git golang rpmdevtools mock tito ansible koji

git clone https://github.com/CiscoCloud/distributive.git 
git clone https://github.com/CiscoCloud/distributive-rpm.git

# Build RPM snapshot

echo "####  BUILDING DISTRIBUTIVE BINARY RPM SNAPSHOT ####"
mkdir ~/rpmbuild
cp -r ~/distributive-rpm/* ~/rpmbuild
rpmdev-setuptree
spectool -R -g ~/rpmbuild/SPECS/distributive-snapshot.spec
rpmbuild --quiet -ba ~/rpmbuild/SPECS/distributive-snapshot.spec

# Build distributive for testing 
echo "####  BUILDING DISTRIBUTIVE FOR TESTING ####"
cd ~/distributive && ./build.sh
echo 'alias distributive-new="~/distributive/bin/distributive"' >> ~/.bashrc
