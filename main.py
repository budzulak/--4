letters = { 
    'a': 
    """ 
 *** 
*   * 
*   * 
* 
*   * 
*   * 
*   * 
""", 
    'b': 
    """ 
**** 
*   * 
*   * 
**** 
*   * 
*   * 
**** 
""", 
    'c': 
    """ 
 *** 
*   * 
* 
* 
* 
*   * 
 *** 
""", 
    'd': 
    """ 
**** 
*   * 
*   * 
*   * 
*   * 
*   * 
**** 
""", 
    'e': 
    """ 
* 
* 
* 
*** 
* 
* 
* 
""", 
    'f': 
    """ 
* 
* 
* 
*** 
* 
* 
* 
""", 
    'g': 
    """ 
 *** 
*   * 
* 
*  ** 
*   * 
*   * 
 *** 
""", 
    'h': 
    """ 
*   * 
*   * 
*   * 
* 
*   * 
*   * 
*   * 
""", 
    'i': 
    """ 
 *** 
  * 
  * 
  * 
  * 
  * 
 *** 
""", 
    'j': 
    """ 
 *** 
  * 
  * 
  * 
  * 
  * 
** 
""", 
    'k': 
    """ 
*   * 
*  * 
* * 
** 
* * 
*  * 
*   * 
""", 
    'l': 
    """ 
* 
* 
* 
* 
* 
* 
* 
""", 
    'm': 
    """ 
*   * 
*   * 
  
* * * 
*   * 
*   * 
*   * 
""", 
    'n': 
    """ 
*   * 
*   * 
**  * 
* * * 
*  ** 
*   * 
*   * 
""", 
    'o': 
    """ 
 *** 
*   * 
*   * 
*   * 
*   * 
*   * 
 *** 
""", 
    'p': 
    """ 
**** 
*   * 
*   * 
**** 
* 
* 
* 
""", 
    'q': 
    """ 
 *** 
*   * 
*   * 
*   * 
*   * 
*  * 
 ** * 
""", 
    'r': 
    """ 
**** 
*   * 
*   * 
**** 
* * 
*  * 
*   * 
""", 
    's': 
    """ 
 **** 
* 
* 
 *** 
    * 
    * 
 *** 
""", 
    't': 
    """ 
* 
  * 
  * 
  * 
  * 
  * 
  * 
""", 
    'v': 
    """ 
*   * 
*   * 
*   * 
*   * 
*   * 
 * * 
  * 
""", 
    'w': 
    """ 
*   * 
*   * 
*   * 
* * * 
  
*   * 
*   * 
""", 
    'x': 
    """ 
*   * 
*   * 
 * * 
  * 
 * * 
*   * 
*   * 
""", 
    'y': 
    """ 
*   * 
*   * 
 * * 
  * 
  * 
  * 
  *  
""", 
    'z': 
    """ 
* 
    * 
   * 
  * 
 * 
* 
* 
""", 
} 
 
 
def pretty_print(string): 
    for letter in string.lower(): 
        print(letters[letter]) 
 
 
pretty_print(input("Введіть слово:"))