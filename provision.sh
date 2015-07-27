#!/bin/sh

# Would you like to build from current master? Or instead, from a release?
snapshot=true
# Would you like to build distributive for testing on the VM?
testing=true

# Install required build packages
sudo yum -q -y install git golang rpmdevtools mock tito ansible koji

# Global variables
rpm_build_dir="$HOME/rpmbuild"
distributive_dir="$HOME/distributive"
sudo chown -R vagrant:vagrant "$rpm_build_dir"

#export GOPATH="$HOME/rpmbuild/BUILD/distributive-master/.godeps/"
#export GOPATH="$HOME/rpmbuild/BUILD/distributive-master/"

echo '####  BUILDING DISTRIBUTIVE BINARY RPM SNAPSHOT ####'
if [ ! -e "$rpm_build_dir" ]; then
    echo "ERROR: synced folder is not on vagrant box: $rpm_build_dir"
elif [ ! -w "$rpm_build_dir" ]; then
    echo "ERROR: couldn't write to the rpm build dir: $rpm_build_dir"
fi

# If we already have the sources, get RID of them.
if [ -e "$rpm_build_dir/BUILD/distributive-master" ]; then
    rm -rf "$rpm_build_dir/BUILD/distributive-master"
fi
if [ -e "$rpm_build_dir/SOURCES/master.zip" ]; then
    rm -f "$rpm_build_dir/SOURCES/master.zip"
fi

rpmdev-setuptree
if [ "$snapshot" = true ]; then
    spectool -R -g "$rpm_build_dir/SPECS/distributive-snapshot.spec"
    rpmbuild --quiet -ba "$rpm_build_dir/SPECS/distributive-snapshot.spec"
else
    spectool -R -g "$rpm_build_dir/SPECS/distributive.spec"
    rpmbuild --quiet -ba "$rpm_build_dir/SPECS/distributive.spec"
fi

# Build distributive for testing
if [ "$testing" = true ]; then
    echo "####  BUILDING DISTRIBUTIVE FOR TESTING ####"
    # Clone a new copy of distributive
    [ -e "$distributive_dir" ] && rm -rf "$distributive_dir"
    git clone http://github.com/CiscoCloud/distributive.git "$distributive_dir"
    # Build and get an alias
    cd "$distributive_dir" && ./build.sh
    echo 'alias distributive-new="~/distributive/bin/distributive"' >> ~/.bashrc
fi
