
#ifndef SHAPEDOBJECT_H
#define SHAPEDOBJECT_H
#include "Shape.h"

#include <string>

namespace visu {


/**
  * class ShapedObject
  * 
  */

class ShapedObject : public Shape
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  ShapedObject ( );

  /**
   * Empty Destructor
   */
  virtual ~ShapedObject ( );

  // Static Public attributes
  //  

  // Public attributes
  //  

  float x;
  float y;
  float z;
  float height;
  std::string id;

protected:

  // Static Protected attributes
  //  

  // Protected attributes
  //  

  Shape shape;
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

#endif // SHAPEDOBJECT_H
