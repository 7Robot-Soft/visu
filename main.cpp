
#include "cmd/CmdView.h"

using namespace visu_cmd;

int main()
{
    CmdView* view = new CmdView();
    view->moveObj("me", 1235.123, 0.223, 123, 3.14);
    return 0;
}
