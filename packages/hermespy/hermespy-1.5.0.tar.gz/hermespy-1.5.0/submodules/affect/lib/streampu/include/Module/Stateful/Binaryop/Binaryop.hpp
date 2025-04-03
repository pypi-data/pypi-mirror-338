/*!
 * \file
 * \brief Class module::Binaryop.
 */
#ifndef BINARYOP_HPP_
#define BINARYOP_HPP_

#include <cstdint>
#include <memory>
#include <vector>

#include "Module/Stateful/Stateful.hpp"
#include "Runtime/Socket/Socket.hpp"
#include "Runtime/Task/Task.hpp"
#include "Tools/Math/binaryop.h"

namespace spu
{

namespace module
{
namespace bop
{
enum class tsk : size_t
{
    perform,
    performf,
    SIZE
};

namespace sck
{
enum class perform : size_t
{
    in0,
    in1,
    out,
    status
};
enum class performf : size_t
{
    in0,
    in1,
    status
};
}
}

template<typename TI, typename TO, tools::proto_bop<TI, TO> BOP>
class Binaryop : public Stateful
{
  public:
    inline runtime::Task& operator[](const bop::tsk t);
    inline runtime::Socket& operator[](const bop::sck::perform s);
    inline runtime::Socket& operator[](const bop::sck::performf s);
    inline runtime::Socket& operator[](const std::string& tsk_sck);

  protected:
    const size_t n_elmts;

  public:
    Binaryop(const size_t n_in0, const size_t n_in1);
    Binaryop(const size_t n_elmts);
    virtual ~Binaryop() = default;
    virtual Binaryop<TI, TO, BOP>* clone() const;

    size_t get_n_elmts() const;

    template<class AI = std::allocator<TI>, class AO = std::allocator<TO>>
    void perform(const std::vector<TI, AI>& in0,
                 const std::vector<TI, AI>& in1,
                 std::vector<TO, AO>& out,
                 const int frame_id = -1,
                 const bool managed_memory = true);

    void perform(const TI* in0, const TI* in1, TO* out, const int frame_id = -1, const bool managed_memory = true);

  protected:
    virtual void _perform(const TI* in0, const TI* in1, TO* out, const size_t frame_id);
    virtual void _perform(const TI in0, const TI* in1, TO* out, const size_t frame_id);
    virtual void _perform(const TI* in0, const TI in1, TO* out, const size_t frame_id);
    virtual void _perform(const TI* in, TI* fwd, const size_t frame_id);
    virtual void _perform(const TI in, TI* fwd, const size_t frame_id);
};

#ifdef _MSC_VER // Hack for MSVC compilation /!\ "Unaryop::getname" does not work correctly on MSVC
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_add<TI, TO>>
using Binaryop_add = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_sub<TI, TO>>
using Binaryop_sub = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_mul<TI, TO>>
using Binaryop_mul = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_div<TI, TO>>
using Binaryop_div = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_or<TI, TO>>
using Binaryop_or = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_xor<TI, TO>>
using Binaryop_xor = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_and<TI, TO>>
using Binaryop_and = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_min<TI, TO>>
using Binaryop_min = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_max<TI, TO>>
using Binaryop_max = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_gt<TI, TO>>
using Binaryop_gt = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_ge<TI, TO>>
using Binaryop_ge = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_lt<TI, TO>>
using Binaryop_lt = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_le<TI, TO>>
using Binaryop_le = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_ne<TI, TO>>
using Binaryop_ne = Binaryop<TI, TO, BOP>;
template<typename TI, typename TO = TI, tools::proto_bop<TI, TO> BOP = tools::bop_eq<TI, TO>>
using Binaryop_eq = Binaryop<TI, TO, BOP>;
#else // Standard code
template<typename TI, typename TO = TI>
using Binaryop_add = Binaryop<TI, TO, tools::bop_add<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_sub = Binaryop<TI, TO, tools::bop_sub<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_mul = Binaryop<TI, TO, tools::bop_mul<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_div = Binaryop<TI, TO, tools::bop_div<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_or = Binaryop<TI, TO, tools::bop_or<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_xor = Binaryop<TI, TO, tools::bop_xor<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_and = Binaryop<TI, TO, tools::bop_and<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_min = Binaryop<TI, TO, tools::bop_min<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_max = Binaryop<TI, TO, tools::bop_max<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_gt = Binaryop<TI, TO, tools::bop_gt<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_ge = Binaryop<TI, TO, tools::bop_ge<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_lt = Binaryop<TI, TO, tools::bop_lt<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_le = Binaryop<TI, TO, tools::bop_le<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_ne = Binaryop<TI, TO, tools::bop_ne<TI, TO>>;
template<typename TI, typename TO = TI>
using Binaryop_eq = Binaryop<TI, TO, tools::bop_eq<TI, TO>>;
#endif
}
}

#ifndef DOXYGEN_SHOULD_SKIP_THIS
#include "Module/Stateful/Binaryop/Binaryop.hxx"
#endif

#endif /* BINARYOP_HPP_ */
