#include "Factory/Tools/Codec/Polar/Codec_polar.hpp"
#include "Factory/Module/Decoder/Polar/Decoder_polar.hpp"
#include "Factory/Module/Encoder/Polar/Encoder_polar.hpp"
#include "Factory/Module/Puncturer/Polar/Puncturer_polar.hpp"

using namespace aff3ct;
using namespace aff3ct::factory;

const std::string aff3ct::factory::Codec_polar_name = "Codec Polar";
const std::string aff3ct::factory::Codec_polar_prefix = "cdc";

Codec_polar ::Codec_polar(const std::string& prefix)
  : Codec_SISO(Codec_polar_name, prefix)
{
    Codec::set_enc(new Encoder_polar("enc"));
    Codec::set_dec(new Decoder_polar("dec"));

    fbg = new Frozenbits_generator(enc->get_prefix() + "-fb");
}

Codec_polar*
Codec_polar ::clone() const
{
    return new Codec_polar(*this);
}

void
Codec_polar ::enable_puncturer()
{
    set_pct(new Puncturer_polar("pct"));
}

std::vector<std::string>
Codec_polar ::get_names() const
{
    auto n = Codec::get_names();
    std::vector<std::string> n2;

    for (size_t i = 0; i < n.size(); i++)
    {
        n2.push_back(n[i]);
        if (enc != nullptr && n[i] == enc->get_name() && fbg != nullptr)
        {
            auto nn = fbg->get_names();
            for (auto& x : nn)
                n2.push_back(x);
        }
    }

    //	if (fbg != nullptr) { auto nn = fbg->get_names(); for (auto &x : nn) n.push_back(x); }
    return n2;
}

std::vector<std::string>
Codec_polar ::get_short_names() const
{
    auto sn = Codec::get_short_names();
    std::vector<std::string> sn2;

    for (size_t i = 0; i < sn.size(); i++)
    {
        sn2.push_back(sn[i]);
        if (enc != nullptr && sn[i] == enc->get_short_name() && fbg != nullptr)
        {
            auto nn = fbg->get_short_names();
            for (auto& x : nn)
                sn2.push_back(x);
        }
    }

    //	if (fbg != nullptr) { auto nn = fbg->get_short_names(); for (auto &x : nn) sn.push_back(x); }
    return sn2;
}

std::vector<std::string>
Codec_polar ::get_prefixes() const
{
    auto p = Codec::get_prefixes();
    std::vector<std::string> p2;

    for (size_t i = 0; i < p.size(); i++)
    {
        p2.push_back(p[i]);
        if (enc != nullptr && p[i] == enc->get_prefix() && fbg != nullptr)
        {
            auto nn = fbg->get_prefixes();
            for (auto& x : nn)
                p2.push_back(x);
        }
    }

    //	if (fbg != nullptr) { auto nn = fbg->get_prefixes(); for (auto &x : nn) p.push_back(x); }
    return p2;
}

void
Codec_polar ::get_description(cli::Argument_map_info& args) const
{
    Codec_SISO::get_description(args);

    enc->get_description(args);
    fbg->get_description(args);
    dec->get_description(args);

    auto pdec = dec->get_prefix();
    auto pfbg = fbg->get_prefix();

    args.erase({ pdec + "-info-bits", "K" });
    args.erase({ pdec + "-no-sys" });
    args.erase({ pdec + "-cw-size", "N" });
    args.erase({ pfbg + "-cw-size", "N" });
    args.erase({ pfbg + "-info-bits", "K" });

    if (pct != nullptr)
    {
        pct->get_description(args);

        auto penc = enc->get_prefix();

        args.erase({ penc + "-cw-size", "N" });
        args.erase({ penc + "-info-bits", "K" });
    }
}

void
Codec_polar ::store(const cli::Argument_map_value& vals)
{
    Codec_SISO::store(vals);

    if (pct != nullptr)
    {
        pct->store(vals);

        enc->K = fbg->K = dec->K = pct->K;
        enc->N_cw = fbg->N_cw = dec->N_cw = pct->N_cw;
    }

    enc->store(vals);

    if (pct == nullptr)
    {
        fbg->K = dec->K = enc->K;
        fbg->N_cw = dec->N_cw = enc->N_cw;
    }

    fbg->store(vals);

    dec->systematic = enc->systematic;

    dec->store(vals);

    K = pct != nullptr ? pct->K : enc->K;
    N_cw = pct != nullptr ? pct->N_cw : enc->N_cw;
    N = pct != nullptr ? pct->N : enc->N_cw;
}

void
Codec_polar ::get_headers(std::map<std::string, tools::header_list>& headers, const bool full) const
{
    Codec_SISO::get_headers(headers, full);

    enc->get_headers(headers, full);
    fbg->get_headers(headers, full);
    dec->get_headers(headers, full);
    if (pct != nullptr) pct->get_headers(headers, full);
}

template<typename B, typename Q>
tools::Codec_polar<B, Q>*
Codec_polar ::build(const module::CRC<B>* crc) const
{
    return new tools::Codec_polar<B, Q>(*fbg,
                                        dynamic_cast<const Encoder_polar&>(*enc),
                                        dynamic_cast<const Decoder_polar&>(*dec),
                                        dynamic_cast<const Puncturer_polar*>(pct.get()),
                                        crc);
}

// ==================================================================================== explicit template instantiation
#include "Tools/types.h"
#ifdef AFF3CT_MULTI_PREC
template aff3ct::tools::Codec_polar<B_8, Q_8>*
aff3ct::factory::Codec_polar::build<B_8, Q_8>(const aff3ct::module::CRC<B_8>*) const;
template aff3ct::tools::Codec_polar<B_16, Q_16>*
aff3ct::factory::Codec_polar::build<B_16, Q_16>(const aff3ct::module::CRC<B_16>*) const;
template aff3ct::tools::Codec_polar<B_32, Q_32>*
aff3ct::factory::Codec_polar::build<B_32, Q_32>(const aff3ct::module::CRC<B_32>*) const;
template aff3ct::tools::Codec_polar<B_64, Q_64>*
aff3ct::factory::Codec_polar::build<B_64, Q_64>(const aff3ct::module::CRC<B_64>*) const;
#else
template aff3ct::tools::Codec_polar<B, Q>*
aff3ct::factory::Codec_polar::build<B, Q>(const aff3ct::module::CRC<B>*) const;
#endif
// ==================================================================================== explicit template instantiation
