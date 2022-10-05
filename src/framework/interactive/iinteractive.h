#ifndef GS_INTERACTIVE_IINTERACTIVE_H
#define GS_INTERACTIVE_IINTERACTIVE_H

#include <any>
#include <map>
#include <string>
#include <variant>

#include <QVariant>

#include "global/ret.h"

using namespace gs;

namespace gs::interactive
{
class IInteractive
{
public:
    // TODO: Should std::any or std::variant be used?
    // using Values = std::variant<bool, int, float, double, std::string>;
    // using Params = std::map<std::string, Values>;
    // NOTE: Using a QVariant for now
    using Params = std::map<std::string, QVariant>;
    // using Params = std::map<std::string, std::any>;
    virtual void regDialog(const std::string& path, const std::string& resourcePath) {}
    // TODO: Use Ret and Val instead of Qt types
    using Result = QVariantMap;
    virtual Result openDialog(const std::string& path, Params& params) {return Result();}
};
} // gs::interactive

// Q_DECLARE_METATYPE(gs::interactive::IInteractive::Values);

#endif