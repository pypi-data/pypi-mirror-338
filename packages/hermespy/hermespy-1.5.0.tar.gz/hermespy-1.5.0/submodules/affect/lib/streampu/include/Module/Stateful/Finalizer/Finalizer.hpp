/*!
 * \file
 * \brief Class module::Finalizer.
 */
#ifndef FINALIZER_HPP_
#define FINALIZER_HPP_

#include <cstdint>
#include <vector>

#include "Module/Stateful/Stateful.hpp"

#include "Tools/Interface/Interface_reset.hpp"

namespace spu
{
namespace module
{
namespace fin
{
enum class tsk : size_t
{
    finalize,
    SIZE
};

namespace sck
{
enum class finalize : size_t
{
    in,
    status
};
}
}

template<typename T = int>
class Finalizer
  : public Stateful
  , public tools::Interface_reset
{
  public:
    inline runtime::Task& operator[](const fin::tsk t);
    inline runtime::Socket& operator[](const fin::sck::finalize s);
    inline runtime::Socket& operator[](const std::string& tsk_sck);

  protected:
    std::vector<std::vector<std::vector<T>>> data;
    size_t next_stream_id;
    size_t ns;

  public:
    Finalizer(const size_t n_elmts, const size_t history_size = 1, const size_t ns = 0);
    virtual ~Finalizer() = default;
    virtual Finalizer* clone() const;

    size_t get_ns() const;
    void set_ns(const size_t ns);

    const std::vector<std::vector<T>>& get_final_data() const;
    const std::vector<std::vector<std::vector<T>>>& get_histo_data() const;
    size_t get_next_stream_id() const;

    void set_n_frames(const size_t n_frames);

    template<class A = std::allocator<T>>
    void finalize(const std::vector<T, A>& in, const int frame_id = -1, const bool managed_memory = true);

    void finalize(const T* in, const int frame_id = -1, const bool managed_memory = true);

    virtual void reset();

  protected:
    virtual void _finalize(const T* in, const size_t frame_id);
};
}
}

#ifndef DOXYGEN_SHOULD_SKIP_THIS
#include "Module/Stateful/Finalizer/Finalizer.hxx"
#endif

#endif /* FINALIZER_HPP_ */
