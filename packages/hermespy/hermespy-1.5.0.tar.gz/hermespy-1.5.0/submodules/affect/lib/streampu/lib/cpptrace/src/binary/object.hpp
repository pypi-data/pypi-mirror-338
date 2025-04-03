#ifndef OBJECT_HPP
#define OBJECT_HPP

#include "../utils/common.hpp"
#include "../utils/utils.hpp"
#include "module_base.hpp"

#include <string>
#include <vector>
#include <mutex>
#include <unordered_map>

#if IS_LINUX || IS_APPLE
 #include <unistd.h>
 #include <dlfcn.h>
 #ifdef CPPTRACE_HAS_DL_FIND_OBJECT
  #include <link.h>
 #endif
#elif IS_WINDOWS
 #include <windows.h>
#endif

namespace cpptrace {
namespace detail {
    #if IS_LINUX || IS_APPLE
    #ifdef CPPTRACE_HAS_DL_FIND_OBJECT
    inline object_frame get_frame_object_info(frame_ptr address) {
        // Use _dl_find_object when we can, it's orders of magnitude faster
        object_frame frame;
        frame.raw_address = address;
        frame.object_address = 0;
        dl_find_object result;
        if(_dl_find_object(reinterpret_cast<void*>(address), &result) == 0) { // thread safe
            if(result.dlfo_link_map->l_name != nullptr && result.dlfo_link_map->l_name[0] != 0) {
                frame.object_path = result.dlfo_link_map->l_name;
            } else {
                // empty l_name, this means it's the currently running executable
                // TODO: Caching and proper handling
                char buffer[CPPTRACE_PATH_MAX + 1]{};
                auto res = readlink("/proc/self/exe", buffer, CPPTRACE_PATH_MAX);
                if(res == -1) {
                    // error handling?
                } else {
                    frame.object_path = buffer;
                }
            }
            frame.object_address = address
                                    - to_frame_ptr(result.dlfo_link_map->l_addr)
                                    + get_module_image_base(frame.object_path);
        }
        return frame;
    }
    #else
    // dladdr queries are needed to get pre-ASLR addresses and targets to run addr2line on
    inline object_frame get_frame_object_info(frame_ptr address) {
        // reference: https://github.com/bminor/glibc/blob/master/debug/backtracesyms.c
        Dl_info info;
        object_frame frame;
        frame.raw_address = address;
        frame.object_address = 0;
        if(dladdr(reinterpret_cast<void*>(address), &info)) { // thread safe
            frame.object_path = info.dli_fname;
            frame.object_address = address
                                    - reinterpret_cast<std::uintptr_t>(info.dli_fbase)
                                    + get_module_image_base(info.dli_fname);
        }
        return frame;
    }
    #endif
    #else
    inline object_frame get_frame_object_info(frame_ptr address) {
        object_frame frame;
        frame.raw_address = address;
        frame.object_address = 0;
        HMODULE handle;
        // Multithread safe as long as another thread doesn't come along and free the module
        if(GetModuleHandleExA(
            GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT | GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS,
            reinterpret_cast<const char*>(address),
            &handle
        )) {
            frame.object_path = get_module_name(handle);
            frame.object_address = address
                                    - reinterpret_cast<std::uintptr_t>(handle)
                                    + get_module_image_base(frame.object_path);
        } else {
            std::fprintf(stderr, "%s\n", std::system_error(GetLastError(), std::system_category()).what());
        }
        return frame;
    }
    #endif

    inline std::vector<object_frame> get_frames_object_info(const std::vector<frame_ptr>& addresses) {
        std::vector<object_frame> frames;
        frames.reserve(addresses.size());
        for(const frame_ptr address : addresses) {
            frames.push_back(get_frame_object_info(address));
        }
        return frames;
    }

    inline object_frame resolve_safe_object_frame(const safe_object_frame& frame) {
        return {
            frame.raw_address,
            frame.address_relative_to_object_start + get_module_image_base(frame.object_path),
            frame.object_path
        };
    }
}
}

#endif
