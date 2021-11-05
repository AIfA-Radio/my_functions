#Insert below all the packages needed by your functions to work 
import numpy as np

#Insert below all the functions you want in your package. 

def example_1(number): 
    
    '''
    Function that multiply by 3. 
    
    Parameters
    ----------
    
    number : float
        Number we want to multiply by 3. 
        
    Returns
    -------
    R : float 
        Number multiplied by 3. 
        
    '''
    
    R = number * 3
    
    return R

def example_2(l): 
    
    '''
    Function that multiply a list by 3. 
    
    Parameters
    ----------
    
    l : list
        List we want to multiply by 3. 
        
    Returns
    -------
    R : list
        List multiplied by 3. 
        
    '''
    
    arr = np.array(l) *3
    R = list(arr)
    
    return R
