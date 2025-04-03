/*!
 * \file
 * \brief Class module::Controller.
 */
#ifndef CONTROLLER_HPP_
#define CONTROLLER_HPP_

#include <cstdint>

#include "Module/Stateful/Stateful.hpp"
#include "Tools/Interface/Interface_reset.hpp"

namespace spu
{
namespace module
{
namespace ctr
{
enum class tsk : size_t
{
    control,
    reset,
    SIZE
};

namespace sck
{
enum class control : size_t
{
    out,
    status
};
}
}

class Controller
  : public Stateful
  , public tools::Interface_reset
{
  public:
    inline runtime::Task& operator[](const ctr::tsk t);
    inline runtime::Socket& operator[](const ctr::sck::control s);
    inline runtime::Socket& operator[](const std::string& tsk_sck);

  protected:
    const size_t init_path;
    size_t path;

  public:
    Controller(const size_t init_path = 0);
    virtual ~Controller() = default;

    virtual void set_path(const size_t path);
    size_t get_path() const;

    virtual void reset();

    template<class A = std::allocator<int8_t>>
    void control(std::vector<int8_t, A>& out, const int frame_id = -1, const bool managed_memory = true);

    void control(int8_t* out, const int frame_id = -1, const bool managed_memory = true);

  protected:
    virtual void _control(int8_t* out, const size_t frame_id) = 0;
};
}
}

#ifndef DOXYGEN_SHOULD_SKIP_THIS
#include "Module/Stateful/Controller/Controller.hxx"
#endif

#endif /* CONTROLLER_HPP_ */
