## Description

This provides a covenient wrapper for creating RPMs from GEMs using gem2rpm, but packages them with a pe- prefix and installs them into the Puppet Enterprise ruby installation.  Useful if you need a gem installed to support a type/provider that is not shipped with PE.

## Quick start

Make sure your .rpmmacros file contains:

`%_topdir <location of this repo>`

To build packages...

    /opt/puppet/bin/gem install gem2rpm
    cd SPECS
    ./autobuild.sh <gemname>


