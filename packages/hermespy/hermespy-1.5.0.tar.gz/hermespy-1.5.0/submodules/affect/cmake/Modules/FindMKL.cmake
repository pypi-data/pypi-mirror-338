# - Find Intel MKL
# Find the MKL libraries
#
# Options:
#
#   MKL_STATIC        :   use static linking
#   MKL_MULTI_THREADED:   use multi-threading
#   MKL_SDL           :   Single Dynamic Library interface
#
# This module defines the following variables:
#
#   MKL_FOUND            : True if MKL_INCLUDE_DIR are found
#   MKL_INCLUDE_DIR      : where to find mkl.h, etc.
#   MKL_INCLUDE_DIRS     : set when MKL_INCLUDE_DIR found
#   MKL_LIBRARIES        : the library to link against.
#   MKL_MINIMAL_LIBRARIES: the library to link against (without lapack).

include(FindPackageHandleStandardArgs)

if(DEFINED ENV{INTELROOT})
    set(INTEL_ROOT $ENV{INTELROOT} CACHE PATH "Folder contains intel libs")
else()
    set(INTEL_ROOT "/opt/intel" CACHE PATH "Folder contains intel libs")
endif()

set(MKL_ROOT $ENV{MKLROOT} CACHE PATH "Folder contains MKL")

# Find include dir
find_path(MKL_INCLUDE_DIR mkl.h
    PATHS ${MKL_ROOT}/include)

# Find include directory
#  There is no include folder under linux
if(WIN32)
    find_path(INTEL_INCLUDE_DIR omp.h
        PATHS ${INTEL_ROOT}/include)
    set(MKL_INCLUDE_DIR ${MKL_INCLUDE_DIR} ${INTEL_INCLUDE_DIR})
endif()

# Find libraries

# Handle suffix
set(_MKL_ORIG_CMAKE_FIND_LIBRARY_SUFFIXES ${CMAKE_FIND_LIBRARY_SUFFIXES})

if(WIN32)
    if(MKL_STATIC)
        set(CMAKE_FIND_LIBRARY_SUFFIXES .lib)
    else()
        set(CMAKE_FIND_LIBRARY_SUFFIXES _dll.lib)
    endif()
else()
    if(APPLE)
        if(MKL_STATIC)
            set(CMAKE_FIND_LIBRARY_SUFFIXES .a)
        else()
            set(CMAKE_FIND_LIBRARY_SUFFIXES .dylib)
        endif()
    else()
        if(MKL_STATIC)
            set(CMAKE_FIND_LIBRARY_SUFFIXES .a)
        else()
            set(CMAKE_FIND_LIBRARY_SUFFIXES .so)
        endif()
    endif()
endif()

# MKL is composed by four layers: Interface, Threading, Computational and RTL
if(APPLE)
    set(MKL_LIBRARIES_PATH
        # ${MKL_ROOT}/lib/ia32/
        ${MKL_ROOT}/lib/)
else()
    set(MKL_LIBRARIES_PATH
        # ${MKL_ROOT}/lib/ia32/
        ${MKL_ROOT}/lib/intel64/)
endif()

set(INTEL_LIBRARIES_PATH
    # ${INTEL_ROOT}/lib/ia32/
    ${INTEL_ROOT}/lib/intel64/)

if(MKL_SDL)
    find_library(MKL_LIBRARY mkl_rt
        PATHS ${MKL_LIBRARIES_PATH})

    set(MKL_MINIMAL_LIBRARY ${MKL_LIBRARY})
else()
    ######################### Interface layer #######################
    if(WIN32)
        set(MKL_INTERFACE_LIBNAME mkl_intel_c)
    else()
        #set(MKL_INTERFACE_LIBNAME mkl_intel)
        set(MKL_INTERFACE_LIBNAME mkl_intel_lp64)
    endif()

    find_library(MKL_INTERFACE_LIBRARY ${MKL_INTERFACE_LIBNAME}
        PATHS ${MKL_LIBRARIES_PATH})

    ######################## Threading layer ########################
    if(MKL_MULTI_THREADED)
        set(MKL_THREADING_LIBNAME mkl_intel_thread)
    else()
        set(MKL_THREADING_LIBNAME mkl_sequential)
    endif()

    find_library(MKL_THREADING_LIBRARY ${MKL_THREADING_LIBNAME}
        PATHS ${MKL_LIBRARIES_PATH})

    ####################### Computational layer #####################
    find_library(MKL_CORE_LIBRARY mkl_core
        PATHS ${MKL_LIBRARIES_PATH})
    find_library(MKL_FFT_LIBRARY mkl_cdft_core
        PATHS ${MKL_LIBRARIES_PATH})
    find_library(MKL_SCALAPACK_LIBRARY mkl_scalapack_core
        PATHS ${MKL_LIBRARIES_PATH})

    ############################ RTL layer ##########################
    if(WIN32)
        set(MKL_RTL_LIBNAME iomp5md)
    else()
        set(MKL_RTL_LIBNAME iomp5)
    endif()
    find_library(MKL_RTL_LIBRARY ${MKL_RTL_LIBNAME}
        PATHS ${INTEL_LIBRARIES_PATH})

    set(MKL_LIBRARY ${MKL_INTERFACE_LIBRARY} ${MKL_THREADING_LIBRARY} ${MKL_CORE_LIBRARY} ${MKL_FFT_LIBRARY} ${MKL_SCALAPACK_LIBRARY} ${MKL_RTL_LIBRARY})
    # set(MKL_MINIMAL_LIBRARY ${MKL_INTERFACE_LIBRARY} ${MKL_THREADING_LIBRARY} ${MKL_CORE_LIBRARY} ${MKL_RTL_LIBRARY})
    set(MKL_MINIMAL_LIBRARY ${MKL_INTERFACE_LIBRARY} ${MKL_THREADING_LIBRARY} ${MKL_CORE_LIBRARY})
endif()

set(CMAKE_FIND_LIBRARY_SUFFIXES ${_MKL_ORIG_CMAKE_FIND_LIBRARY_SUFFIXES})

find_package_handle_standard_args(MKL DEFAULT_MSG
    # MKL_INCLUDE_DIR MKL_LIBRARY MKL_MINIMAL_LIBRARY)
    MKL_INCLUDE_DIR MKL_MINIMAL_LIBRARY)

if(MKL_FOUND)
    set(MKL_INCLUDE_DIRS ${MKL_INCLUDE_DIR})
    set(MKL_LIBRARIES ${MKL_LIBRARY})
    set(MKL_MINIMAL_LIBRARIES ${MKL_MINIMAL_LIBRARY})
endif()