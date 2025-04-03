#include "Factory/Tools/Codec/RSC/Codec_RSC.hpp"
#include "Factory/Module/Decoder/RSC/Decoder_RSC.hpp"
#include "Factory/Module/Encoder/RSC/Encoder_RSC.hpp"

using namespace aff3ct;
using namespace aff3ct::factory;

const std::string aff3ct::factory::Codec_RSC_name = "Codec RSC";
const std::string aff3ct::factory::Codec_RSC_prefix = "cdc";

Codec_RSC ::Codec_RSC(const std::string& prefix)
  : Codec_SISO(Codec_RSC_name, prefix)
{
    Codec::set_enc(new Encoder_RSC("enc"));
    Codec::set_dec(new Decoder_RSC("dec"));
}

Codec_RSC*
Codec_RSC ::clone() const
{
    return new Codec_RSC(*this);
}

void
Codec_RSC ::get_description(cli::Argument_map_info& args) const
{
    Codec_SISO::get_description(args);

    enc->get_description(args);
    dec->get_description(args);

    auto pdec = dec->get_prefix();

    args.erase({ pdec + "-cw-size", "N" });
    args.erase({ pdec + "-info-bits", "K" });
    args.erase({ pdec + "-no-buff" });
    args.erase({ pdec + "-poly" });
    args.erase({ pdec + "-std" });
}

void
Codec_RSC ::store(const cli::Argument_map_value& vals)
{
    Codec_SISO::store(vals);

    auto enc_rsc = dynamic_cast<Encoder_RSC*>(enc.get());
    auto dec_rsc = dynamic_cast<Decoder_RSC*>(dec.get());

    enc->store(vals);

    dec_rsc->K = enc_rsc->K;
    dec_rsc->N_cw = enc_rsc->N_cw;
    dec_rsc->buffered = enc_rsc->buffered;
    dec_rsc->poly = enc_rsc->poly;
    dec_rsc->standard = enc_rsc->standard;

    dec->store(vals);

    K = enc->K;
    N_cw = enc->N_cw;
    N = enc->N_cw;
    tail_length = enc->tail_length;
}

void
Codec_RSC ::get_headers(std::map<std::string, tools::header_list>& headers, const bool full) const
{
    Codec_SISO::get_headers(headers, full);

    enc->get_headers(headers, full);
    dec->get_headers(headers, full);
}

template<typename B, typename Q>
tools::Codec_RSC<B, Q>*
Codec_RSC ::build(const module::CRC<B>* crc) const
{
    return new tools::Codec_RSC<B, Q>(
      dynamic_cast<const Encoder_RSC&>(*enc), dynamic_cast<const Decoder_RSC&>(*dec), crc);
}

// ==================================================================================== explicit template instantiation
#include "Tools/types.h"
#ifdef AFF3CT_MULTI_PREC
template aff3ct::tools::Codec_RSC<B_8, Q_8>*
aff3ct::factory::Codec_RSC::build<B_8, Q_8>(const aff3ct::module::CRC<B_8>*) const;
template aff3ct::tools::Codec_RSC<B_16, Q_16>*
aff3ct::factory::Codec_RSC::build<B_16, Q_16>(const aff3ct::module::CRC<B_16>*) const;
template aff3ct::tools::Codec_RSC<B_32, Q_32>*
aff3ct::factory::Codec_RSC::build<B_32, Q_32>(const aff3ct::module::CRC<B_32>*) const;
template aff3ct::tools::Codec_RSC<B_64, Q_64>*
aff3ct::factory::Codec_RSC::build<B_64, Q_64>(const aff3ct::module::CRC<B_64>*) const;
#else
template aff3ct::tools::Codec_RSC<B, Q>*
aff3ct::factory::Codec_RSC::build<B, Q>(const aff3ct::module::CRC<B>*) const;
#endif
// ==================================================================================== explicit template instantiation
