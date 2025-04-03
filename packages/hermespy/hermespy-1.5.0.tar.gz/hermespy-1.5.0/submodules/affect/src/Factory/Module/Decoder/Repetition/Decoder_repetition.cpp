#include <streampu.hpp>
#include <utility>

#include "Factory/Module/Decoder/Repetition/Decoder_repetition.hpp"
#include "Module/Decoder/Repetition/Decoder_repetition_fast.hpp"
#include "Module/Decoder/Repetition/Decoder_repetition_std.hpp"
#include "Module/Decoder/Repetition/Decoder_repetition_vote.hpp"
#include "Tools/Documentation/documentation.h"

using namespace aff3ct;
using namespace aff3ct::factory;

const std::string aff3ct::factory::Decoder_repetition_name = "Decoder Repetition";
const std::string aff3ct::factory::Decoder_repetition_prefix = "dec";

Decoder_repetition ::Decoder_repetition(const std::string& prefix)
  : Decoder(Decoder_repetition_name, prefix)
{
    this->type = "REPETITION";
    this->implem = "STD";
}

Decoder_repetition*
Decoder_repetition ::clone() const
{
    return new Decoder_repetition(*this);
}

void
Decoder_repetition ::get_description(cli::Argument_map_info& args) const
{
    Decoder::get_description(args);

    auto p = this->get_prefix();
    const std::string class_name = "factory::Decoder_repetition::";

    cli::add_options(args.at({ p + "-type", "D" }), 0, "REPETITION", "REPETITION_VOTE");
    cli::add_options(args.at({ p + "-implem" }), 0, "STD", "FAST");

    tools::add_arg(args, p, class_name + "p+no-buff", cli::None());
}

void
Decoder_repetition ::store(const cli::Argument_map_value& vals)
{
    Decoder::store(vals);

    auto p = this->get_prefix();

    if (vals.exist({ p + "-no-buff" })) this->buffered = false;
}

void
Decoder_repetition ::get_headers(std::map<std::string, tools::header_list>& headers, const bool full) const
{
    Decoder::get_headers(headers, full);

    if (this->type != "ML" && this->type != "CHASE")
    {
        auto p = this->get_prefix();

        if (full) headers[p].push_back(std::make_pair("Buffered", (this->buffered ? "on" : "off")));
    }
}

template<typename B, typename Q>
module::Decoder_SIHO<B, Q>*
Decoder_repetition ::build(module::Encoder<B>* encoder) const
{
    try
    {
        return Decoder::build<B, Q>(encoder);
    }
    catch (spu::tools::cannot_allocate const&)
    {
        if (this->type == "REPETITION")
        {
            if (this->implem == "STD")
                return new module::Decoder_repetition_std<B, Q>(this->K, this->N_cw, this->buffered);
            if (this->implem == "FAST")
                return new module::Decoder_repetition_fast<B, Q>(this->K, this->N_cw, this->buffered);
        }
        if (this->type == "REPETITION_VOTE")
        {
            if (this->implem == "STD")
                return new module::Decoder_repetition_vote<B, Q>(this->K, this->N_cw, this->buffered);
        }
    }

    throw spu::tools::cannot_allocate(__FILE__, __LINE__, __func__);
}

// ==================================================================================== explicit template instantiation
#include "Tools/types.h"
#ifdef AFF3CT_MULTI_PREC
template aff3ct::module::Decoder_SIHO<B_8, Q_8>*
aff3ct::factory::Decoder_repetition::build<B_8, Q_8>(module::Encoder<B_8>*) const;
template aff3ct::module::Decoder_SIHO<B_16, Q_16>*
aff3ct::factory::Decoder_repetition::build<B_16, Q_16>(module::Encoder<B_16>*) const;
template aff3ct::module::Decoder_SIHO<B_32, Q_32>*
aff3ct::factory::Decoder_repetition::build<B_32, Q_32>(module::Encoder<B_32>*) const;
template aff3ct::module::Decoder_SIHO<B_64, Q_64>*
aff3ct::factory::Decoder_repetition::build<B_64, Q_64>(module::Encoder<B_64>*) const;
#else
template aff3ct::module::Decoder_SIHO<B, Q>*
aff3ct::factory::Decoder_repetition::build<B, Q>(module::Encoder<B>*) const;
#endif
// ==================================================================================== explicit template instantiation
