#/bin/bash

# Usage: ./auobuild.sh <packagename>
# eg: ./autobuild.sh hiera-gpg

PACKAGE=$1

cd ../SOURCES
/opt/puppet/bin/gem2rpm --fetch $PACKAGE

SOURCE=`ls ${PACKAGE}-* | tail -1`

cd ../SPECS
/opt/puppet/bin/gem2rpm -t pe-template.spec ../SOURCES/${SOURCE} > ${PACKAGE}.spec
rpmbuild -bb ${PACKAGE}.spec

