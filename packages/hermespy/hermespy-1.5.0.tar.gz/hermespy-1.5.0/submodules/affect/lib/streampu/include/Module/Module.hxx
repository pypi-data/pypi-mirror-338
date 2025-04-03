#include <algorithm>
#include <cassert>
#include <exception>
#include <sstream>

#include "Module/Module.hpp"

namespace spu
{
namespace module
{
runtime::Task&
Module::operator[](const size_t id)
{
    assert(id < this->tasks_with_nullptr.size());
    assert(this->tasks_with_nullptr[id] != nullptr);

    return *this->tasks_with_nullptr[id];
}

const runtime::Task&
Module::operator[](const size_t id) const
{
    assert(id < this->tasks_with_nullptr.size());
    assert(this->tasks_with_nullptr[id] != nullptr);

    return *this->tasks_with_nullptr[id];
}

runtime::Socket&
Module::operator[](const std::string& tsk_sck)
{
    size_t pos = tsk_sck.find("::", 0);
    if ((int)pos < 0)
    {
        std::stringstream message;
        message << "Invalid socket name, it should be of the form task::socket ('tsk_sck' = " << tsk_sck << ").";
        throw tools::invalid_argument(__FILE__, __LINE__, __func__, message.str());
    }
    std::string tsk_name = tsk_sck.substr(0, pos);
    tsk_name.erase(remove(tsk_name.begin(), tsk_name.end(), ' '), tsk_name.end());
    std::string sck_name = tsk_sck.substr(pos + 2, tsk_sck.size());
    sck_name.erase(remove(sck_name.begin(), sck_name.end(), ' '), sck_name.end());
    auto& cur_tsk = this->operator()(tsk_name);

    auto it = find_if(cur_tsk.sockets.begin(),
                      cur_tsk.sockets.end(),
                      [sck_name](std::shared_ptr<runtime::Socket> s) { return s->get_name() == sck_name; });

    if (it == cur_tsk.sockets.end())
    {
        std::stringstream message;
        message << "runtime::Socket '" << sck_name << "' not found for task '" << tsk_name << "'.";
        throw tools::invalid_argument(__FILE__, __LINE__, __func__, message.str());
    }

    return *it->get();
}

runtime::Task&
Module::operator()(const std::string& tsk_name)
{
    auto it = find_if(this->tasks.begin(),
                      this->tasks.end(),
                      [tsk_name](std::shared_ptr<runtime::Task> t) { return t->get_name() == tsk_name; });

    if (it == this->tasks.end())
    {
        std::stringstream message;
        message << "runtime::Task '" << tsk_name << "' not found.";
        throw tools::invalid_argument(__FILE__, __LINE__, __func__, message.str());
    }

    return *it->get();
}

template<typename T>
inline size_t
Module::create_socket_in(runtime::Task& task, const std::string& name, const size_t n_elmts)
{
    return task.template create_2d_socket_in<T>(name, this->n_frames, n_elmts);
}

template<typename T>
inline size_t
Module::create_sck_in(runtime::Task& task, const std::string& name, const size_t n_elmts)
{
    return this->template create_socket_in<T>(task, name, n_elmts);
}

template<typename T>
inline size_t
Module::create_socket_out(runtime::Task& task, const std::string& name, const size_t n_elmts)
{
    return task.template create_2d_socket_out<T>(name, this->n_frames, n_elmts);
}

template<typename T>
inline size_t
Module::create_sck_out(runtime::Task& task, const std::string& name, const size_t n_elmts)
{
    return this->template create_socket_out<T>(task, name, n_elmts);
}

template<typename T>
inline size_t
Module::create_socket_fwd(runtime::Task& task, const std::string& name, const size_t n_elmts)
{
    return task.template create_2d_socket_fwd<T>(name, this->n_frames, n_elmts);
}

template<typename T>
inline size_t
Module::create_sck_fwd(runtime::Task& task, const std::string& name, const size_t n_elmts)
{
    return this->template create_socket_fwd<T>(task, name, n_elmts);
}

template<typename T>
inline size_t
Module::create_2d_socket_in(runtime::Task& task, const std::string& name, const size_t n_rows, const size_t n_cols)
{
    return task.template create_2d_socket_in<T>(name, this->n_frames * n_rows, n_cols);
}

template<typename T>
inline size_t
Module::create_2d_sck_in(runtime::Task& task, const std::string& name, const size_t n_rows, const size_t n_cols)
{
    return this->template create_2d_socket_in<T>(task, name, n_rows, n_cols);
}

template<typename T>
inline size_t
Module::create_2d_socket_out(runtime::Task& task, const std::string& name, const size_t n_rows, const size_t n_cols)
{
    return task.template create_2d_socket_out<T>(name, this->n_frames * n_rows, n_cols);
}

template<typename T>
inline size_t
Module::create_2d_sck_out(runtime::Task& task, const std::string& name, const size_t n_rows, const size_t n_cols)
{
    return this->template create_2d_socket_out<T>(task, name, n_rows, n_cols);
}

template<typename T>
inline size_t
Module::create_2d_socket_fwd(runtime::Task& task, const std::string& name, const size_t n_rows, const size_t n_cols)
{
    return task.template create_2d_socket_fwd<T>(name, this->n_frames * n_rows, n_cols);
}

template<typename T>
inline size_t
Module::create_2d_sck_fwd(runtime::Task& task, const std::string& name, const size_t n_rows, const size_t n_cols)
{
    return this->template create_2d_socket_fwd<T>(task, name, n_rows, n_cols);
}

size_t
Module::get_n_frames() const
{
    return this->n_frames;
}

size_t
Module::get_n_frames_per_wave() const
{
    return this->n_frames_per_wave;
}

size_t
Module::get_n_waves() const
{
    return this->n_waves;
}

size_t
Module::get_n_frames_per_wave_rest() const
{
    return this->n_frames_per_wave_rest;
}

bool
Module::is_single_wave() const
{
    return this->single_wave;
}

}
}
