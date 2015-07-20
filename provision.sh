#!/bin/sh

# Would you like to build from current master? Or instead, from a release?
snapshot=false

# Install required build packages
sudo yum -q -y install git golang rpmdevtools mock tito ansible koji

# Global variables
rpm_build_dir="$HOME/rpmbuild"
distributive_dir="$HOME/distributive"

# Fix GOPATH for build
export GOPATH="$rpm_build_dir/BUILD/distributive-master/"

# Clone a new copy of distributive
[ -e "$distributive_dir" ] && rm -rf "$distributive_dir"
git clone https://github.com/CiscoCloud/distributive.git "$distributive_dir"

echo '####  BUILDING DISTRIBUTIVE BINARY RPM SNAPSHOT ####'
[ ! -e "$rpm_build_dir" ] && echo "ERROR: synced folder is not on vagrant box: $rpm_build_dir"
rpmdev-setuptree
if [ "$snapshot" = true ]; then
    spectool -R -g "$rpm_build_dir/SPECS/distributive-snapshot.spec"
    rpmbuild --quiet -ba "$rpm_build_dir/SPECS/distributive-snapshot.spec"
else
    spectool -R -g "$rpm_build_dir/SPECS/distributive.spec"
    rpmbuild --quiet -ba "$rpm_build_dir/SPECS/distributive.spec"
fi

# Build distributive for testing
echo "####  BUILDING DISTRIBUTIVE FOR TESTING ####"
cd "$distributive_dir" && ./build.sh
echo 'alias distributive-new="~/distributive/bin/distributive"' >> ~/.bashrc
