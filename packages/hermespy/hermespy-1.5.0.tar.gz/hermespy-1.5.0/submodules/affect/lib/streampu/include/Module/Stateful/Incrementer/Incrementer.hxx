#include "Module/Stateful/Incrementer/Incrementer.hpp"

namespace spu
{
namespace module
{

template<typename T>
runtime::Task&
Incrementer<T>::operator[](const inc::tsk t)
{
    return Module::operator[]((size_t)t);
}

template<typename T>
runtime::Socket&
Incrementer<T>::operator[](const inc::sck::increment s)
{
    return Module::operator[]((size_t)inc::tsk::increment)[(size_t)s];
}

template<typename T>
runtime::Socket&
Incrementer<T>::operator[](const inc::sck::incrementf s)
{
    return Module::operator[]((size_t)inc::tsk::incrementf)[(size_t)s];
}

template<typename T>
runtime::Socket&
Incrementer<T>::operator[](const std::string& tsk_sck)
{
    return Module::operator[](tsk_sck);
}

template<typename T>
template<class A>
void
Incrementer<T>::increment(const std::vector<T, A>& in,
                          std::vector<T, A>& out,
                          const int frame_id,
                          const bool managed_memory)
{
    (*this)[inc::sck::increment::in].bind(in);
    (*this)[inc::sck::increment::out].bind(out);
    (*this)[inc::tsk::increment].exec(frame_id, managed_memory);
}

}
}
