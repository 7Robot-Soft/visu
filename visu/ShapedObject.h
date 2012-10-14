
#ifndef SHAPEDOBJECT_H
#define SHAPEDOBJECT_H
#include "visu/Shape.h"

#include <string>

namespace visu {


/**
  * class ShapedObject
  * 
  */

class ShapedObject : virtual public Shape
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
  string id;

protected:

  // Static Protected attributes
  //  

  // Protected attributes
  //  

  visu::Shape shape;
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


  void initAttributes ( ) ;

};
}; // end of package namespace

#endif // SHAPEDOBJECT_H
