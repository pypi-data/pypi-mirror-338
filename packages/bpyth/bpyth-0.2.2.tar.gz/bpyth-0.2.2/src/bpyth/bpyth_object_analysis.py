
import sys
import re
from .bpyth_human import human_readable_bytes
from collections.abc import Iterable

# Optionaler Import von Pandas
try:
    import pandas as pd
    pandas_available = True
except ImportError:
    pandas_available = False

# Optionaler Import von Polars
try:
    import polars as pl
    polars_available = True
except ImportError:
    polars_available = False

# Optionaler Import von Numpy
try:
    import numpy as np
    numpy_available = True
except ImportError:
    numpy_available = False

#############################################################################################################
###
### Object analysis
###
#############################################################################################################        

def stype(obj):
    '''
    Returns the type as a short string
    '''
    type_name = type(obj).__name__
    result = re.sub(r'\d+$', '', type_name) # Zahlen am Ende abschneiden
    if result == 'intc':
        return 'int'
    return result


def rtype(inp):
    '''
    Returns the type of the input object as a tuple.
    '''
    if pandas_available:
        if isinstance(inp, pd.DataFrame):
            if inp.empty:
                return ("DataFrame",)
            else:
                return ("DataFrame",) + rtype(inp.iloc[:,0]) # first col

        if isinstance(inp, pd.Series):
            if inp.empty:
                return ("Series",)
            first_element_type = rtype(inp.iloc[0])
            return ("Series",) + first_element_type

    if polars_available:
        if isinstance(inp, pl.DataFrame):
            if inp.is_empty():
                return ("DataFrame",)
            else:
                return ("DataFrame",) + rtype(inp[:, 0]) # first col

        if isinstance(inp, pl.Series):
            if inp.is_empty():
                return ("Series",)
            first_element_type = rtype(inp[0])
            return ("Series",) + first_element_type

    if isinstance(inp, str):
        return ("str",)

    if isinstance(inp, bytes):
        return ("bytes",)

    if isinstance(inp, bool):
        return ("bool",)

    if isinstance(inp, int):
        return ("int",)

    if isinstance(inp, float):
        return ("float",)

    if inp is None:
        return ("NoneType",)

    if isinstance(inp, dict):
        if len(inp) == 0:
            return ("dict",)
        else:
            first_value = next(iter(inp.values()))
            return ("dict",) + rtype(first_value)

    if isinstance(inp, set):
        if len(inp) == 0:
            return ("set",)
        else:
            first_value = next(iter(inp))
            return ("set",) + rtype(first_value)

    if isinstance(inp, Iterable):
        if len(inp) == 0:
            return (stype(inp),)
        else:
            first_value = inp[0]
            return (stype(inp),) + rtype(first_value)

    return (stype(inp),)



def shape(obj):
    '''
    Recursive len. Parses an n-dimensional object and returns a tuple of sizes.
    Caution: only a single scalar is found. A heterogeneous data structure cannot be parsed meaningfully.     
    '''
    
    # Trivialfälle
    if not has_shape(obj):
        return tuple()
    if stype(obj) == 'DataFrame':
        return obj.shape
    
    def ishape(obj):
        try:
            shapes = []
            if isinstance(obj, dict):
                for x in obj.values():
                    if has_shape(x):     
                        shapes.append( ishape(x) )
                    else:
                        shapes.append( [0] )
            else:
                for x in obj:
                    if has_shape(x):    
                        shapes.append( ishape(x) )
                    else:
                        shapes.append( [0] )

        except TypeError:
            shapes = [0]

        try:
            shape = shapes[0]
        except IndexError:
            shape = []
        if shapes.count(shape) != len(shapes): 
            raise ValueError('Ragged list')
        try:
            # Einzusetzender Wert
            shape.append( len(obj) )
        except:
            return []
            #shape.append(0)
        return shape
    
    result = reversed(ishape(obj))
    # Nullen entfernen
    result = [ s for s in result if s > 0]
    return tuple(result)    
    
    

def has_shape(inputobjekt):
    '''
    Does an object have additional dimensions?
    Skalars: No
    Strings: No (per definition)    
    Empty Iterables: No (per definition)    
    Other Iterables: Yes
    '''
    
    if stype(inputobjekt) in ['str']: # iterable, soll aber nicht durchiteriert werden
        return False    
    try:
        iterator = iter(inputobjekt)
    except TypeError:
        return False
    else:
        try:
            test = next(iterator)
            return True
        except StopIteration:
            return False


def has_no_content(obj):
    """
    Recursively checks if an object contains any scalar values.
    An object is considered empty if it contains no scalars (e.g., int, float, str, etc.)
    anywhere in its *values* (not keys).
    """
    if obj is None:
        return True

    try:
        if obj == "":
            return True
        if obj == b"":
            return True
    except:
        pass

    # Scalars are considered not empty
    if isinstance(obj, (int, float, str, bytes, bool)):
        return False

    # Dict: check only the values
    if isinstance(obj, dict):
        if len(obj) == 0:
            return True
        else:
            return all(has_no_content(v) for v in obj.values())

    # Empty container types
    if isinstance(obj, (list, tuple, set)) and len(obj) == 0:
        return True

    # Iterable types (excluding strings/bytes already handled)
    if isinstance(obj, (list, tuple, set)):
        return all(has_no_content(item) for item in obj)

    # numpy arrays
    if numpy_available:
        if isinstance(obj, np.ndarray):
            if obj.size == 0:
                return True
            else:
                return all(has_no_content(item) for item in obj.flatten())

    # pandas Series
    if pandas_available:
        if isinstance(obj, pd.Series):
            if obj.empty:
                return True
            else:
                return all(has_no_content(item) for item in obj)

    # polars Series
    if polars_available:
        if isinstance(obj, pl.Series):
            if obj.is_empty():
                return True
            else:
                return all(has_no_content(item) for item in obj)

    # pandas DataFrame
    if pandas_available:
        if isinstance(obj, pd.DataFrame):
            return obj.empty

    # polars DataFrame
    if polars_available:
        if isinstance(obj, pl.DataFrame):
            return obj.is_empty()

    # Other iterable types
    if isinstance(obj, Iterable):
        try:
            return all(has_no_content(item) for item in obj)
        except TypeError:
            pass

    # Anything else is assumed to be a scalar
    return False
        
  
    
def memory_consumption( iteration_of_objects, limit=10, use_rtype=False):
    '''
    Returns the memory consumption of Python objects.
    * iteration_of_objects: can be e.g. a DataFrame or just locals()
    * limit: Limits the output size
    * use_rtype: Use rtype instead of type?
    
    For the memory consumption of the biggest 10 local variables call:
    bpy.memory_consumption( locals() )
    '''    
    result = []
    list_of_objects = list(iteration_of_objects.items())
    for var, obj in list_of_objects:
        size = sys.getsizeof(obj)
        if use_rtype:
            typ = rtype(obj)
        else:
            typ = stype(obj) 
        result.append( ( var, typ, size, human_readable_bytes(size) ) )
    result = sorted(result, key= lambda x: -x[2])
    result = result[:limit]
    result = [(r[0], r[1], r[3]) for r in result]
    return result
            
        
        
        
        
        
        
        
        
        
        
    