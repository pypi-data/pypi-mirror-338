#!/bin/bash
set -x

function compile {
	build=$1
	mkdir $build
	cd $build
	cmake .. -G"Unix Makefiles" -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-Wall -funroll-loops $2"
	rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
	make -j $THREADS
	rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
	cd ..
}

cd tests

build_root=build_linux_armv7_clang
compile "${build_root}_nointr"   "-DMIPP_NO_INTRINSICS"
compile "${build_root}_neon"     "-march=armv7-a -mfpu=neon"
compile "${build_root}_neon_fma" "-march=armv7-a -mfpu=neon-vfpv4"
