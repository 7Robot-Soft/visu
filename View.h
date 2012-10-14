
#ifndef VIEW_H
#define VIEW_H

#include <string>

#include "ShapedObject.h"

namespace visu {


/**
  * class View
  * 
  */

/******************************* Abstract Class ****************************
View does not have any pure virtual methods, but its author
  defined it as an abstract class, so you should not use it directly.
  Inherit from it instead and create only objects from the derived classes
*****************************************************************************/

class View
{
public:



  /**
   * @param  id
   * @param  x
   * @param  y
   * @param  z
   * @param  theta
   */
  virtual void moveObj (std::string id, float x, float y, float z, float theta )
  {
  }


  /**
   * @param  id
   */
  virtual void highlightObj (std::string id )
  {
  }


  /**
   * @param  obj
   */
  virtual void addShapedObject (ShapedObject* obj )
  {
  }

protected:

public:

protected:

public:

protected:


private:

public:

private:

public:

private:



};
}; // end of package namespace

#endif // VIEW_H
