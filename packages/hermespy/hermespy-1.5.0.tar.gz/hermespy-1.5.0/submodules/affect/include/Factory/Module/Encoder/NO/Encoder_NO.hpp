/*!
 * \file
 * \brief Class factory::Encoder_NO.
 */
#ifndef FACTORY_ENCODER_NO_HPP
#define FACTORY_ENCODER_NO_HPP

#include <cli.hpp>
#include <map>
#include <string>

#include "Factory/Module/Encoder/Encoder.hpp"
#include "Module/Encoder/NO/Encoder_NO.hpp"
#include "Tools/Factory/Header.hpp"

namespace aff3ct
{
namespace factory
{
extern const std::string Encoder_NO_name;
extern const std::string Encoder_NO_prefix;
class Encoder_NO : public Encoder
{
  public:
    // ----------------------------------------------------------------------------------------------------- PARAMETERS
    // empty

    // -------------------------------------------------------------------------------------------------------- METHODS
    explicit Encoder_NO(const std::string& p = Encoder_NO_prefix);
    virtual ~Encoder_NO() = default;
    Encoder_NO* clone() const;

    // parameters construction
    void get_description(cli::Argument_map_info& args) const;
    void store(const cli::Argument_map_value& vals);
    void get_headers(std::map<std::string, tools::header_list>& headers, const bool full = true) const;

    // builder
    template<typename B = int>
    module::Encoder_NO<B>* build() const;
};
}
}

#endif /* FACTORY_ENCODER_NO_HPP */
