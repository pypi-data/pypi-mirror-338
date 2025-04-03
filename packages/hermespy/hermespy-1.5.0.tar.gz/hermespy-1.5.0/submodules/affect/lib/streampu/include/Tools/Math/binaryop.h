#ifndef BINARYOP_H
#define BINARYOP_H

#include <string>

namespace spu
{
namespace tools
{
// -------------------------------------------------------------------------- special function prototypes for templates

template<typename TI, typename TO>
using proto_bop = TO (*)(const TI a, const TI b);

// ------------------------------------------------------------------------------------------- special function headers

template<typename TI, typename TO>
inline TO
bop_add(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_sub(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_mul(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_div(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_or(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_xor(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_and(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_min(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_max(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_gt(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_ge(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_lt(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_le(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_ne(const TI a, const TI b);
template<typename TI, typename TO>
inline TO
bop_eq(const TI a, const TI b);

template<typename TI, typename TO, proto_bop<TI, TO> BOP>
std::string
bop_get_name();

}
}

#ifndef DOXYGEN_SHOULD_SKIP_THIS
#include "Tools/Math/binaryop.hxx"
#endif

#endif /* BINARYOP_H */
