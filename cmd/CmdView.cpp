#include "CmdView.h"

#include <stdio.h>

namespace visu_cmd {

// Constructors/Destructors
//  

CmdView::CmdView ( ) {
}

CmdView::~CmdView ( ) { }

//  
// Methods
//  

void CmdView::moveObj (std::string id, float x, float y, float z, float theta )
{
    printf("[MOVE] %s x:%0.2f y:%0.2f z:%0.2f theta:%0.2f\n", id.c_str(), x, y, z, theta);
}

void CmdView::highlightObj (std::string id )
{
    printf("[HL] %s\n", id.c_str());
}
  
void CmdView::addShapedObject (visu::ShapedObject* obj )
{
}

// Accessor methods
//  


// Other methods
//  


};
