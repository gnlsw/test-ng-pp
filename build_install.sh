#!/bin/bash
# build and install

# You can change this testngpp install dir by yourself, it must be an absolute path.
install_dir=/home/jelly/Programming/cpp-ut-project/cpp-ut-project/premake_version/tools/testngpp


function build() {
	mkdir $1 2>/dev/null
	cd $1
	cmake -DCMAKE_INSTALL_PREFIX=$install_dir $2
	make install
}

build ../build_testngpp_to_install ../test-ng-pp

cd ../test-ng-pp

mv -f $install_dir/3rdparty $install_dir/..
