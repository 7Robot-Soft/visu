
#ifndef CMDVIEW_H
#define CMDVIEW_H
#include "../View.h"
#include "../ShapedObject.h"

#include <string>

using namespace visu;

namespace visu_cmd {


/**
  * class View
  * 
  */

class CmdView : public View
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  CmdView ( );

  /**
   * Empty Destructor
   */
  virtual ~CmdView ( );
  
  void moveObj (std::string id, float x, float y, float z, float theta );
  void highlightObj (std::string id );
  void addShapedObject (ShapedObject* obj );

  // Static Public attributes
  //  

  // Public attributes
  //  


protected:

  // Static Protected attributes
  //  

  // Protected attributes
  //  

public:

protected:

public:

protected:


private:

  // Static Private attributes
  //  

  // Private attributes
  //  

public:

private:

public:

private:



};
}; // end of package namespace

#endif // CMDVIEW_H
