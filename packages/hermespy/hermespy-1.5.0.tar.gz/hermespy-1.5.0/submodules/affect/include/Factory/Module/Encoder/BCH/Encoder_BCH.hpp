/*!
 * \file
 * \brief Class factory::Encoder_BCH.
 */
#ifndef FACTORY_ENCODER_BCH_HPP
#define FACTORY_ENCODER_BCH_HPP

#include <cli.hpp>
#include <map>
#include <string>

#include "Factory/Module/Encoder/Encoder.hpp"
#include "Module/Encoder/BCH/Encoder_BCH.hpp"
#include "Tools/Code/BCH/BCH_polynomial_generator.hpp"
#include "Tools/Factory/Header.hpp"

namespace aff3ct
{
namespace factory
{
extern const std::string Encoder_BCH_name;
extern const std::string Encoder_BCH_prefix;
class Encoder_BCH : public Encoder
{
  public:
    // ----------------------------------------------------------------------------------------------------- PARAMETERS
    std::string simd_strategy = "";

    // -------------------------------------------------------------------------------------------------------- METHODS
    explicit Encoder_BCH(const std::string& p = Encoder_BCH_prefix);
    virtual ~Encoder_BCH() = default;
    Encoder_BCH* clone() const;

    // parameters construction
    void get_description(cli::Argument_map_info& args) const;
    void store(const cli::Argument_map_value& vals);
    void get_headers(std::map<std::string, tools::header_list>& headers, const bool full = true) const;

    // builder
    template<typename B = int>
    module::Encoder_BCH<B>* build(const tools::BCH_polynomial_generator<B>& GF) const;
};
}
}

#endif /* FACTORY_ENCODER_BCH_HPP */
