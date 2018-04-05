#Convert from 
invalid_msg = "you've not entered a valid format"

def rgb_hex():
  red = int(input("please enter red value: "))
  green = int(input("please enter green value: "))
  blue = int(input("please enter blue value: "))
  
  if (red < 0 or red > 255):
    print (invalid_msg)
    return
  if (blue < 0 or blue > 255):
    print (invalid_msg)
    return
  if (green < 0 or green > 255):
    print (invalid_msg)
    return
  
  val = (red <<16) + (green <<8) + blue
  print ("%s" % (hex(val)[2:].upper()))


def hex_rgb():
    hex_val = input("Enter a hexadecimal value: ")

    if len(hex_val) != 6:
        print (invalid_msg)
        return
    else:
        hex_val = int(hex_val,16)
    
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8        
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8  
    red = hex_val % two_hex_digits
    hex_val = hex_val >> 8  

    print ("Red: %s, Green: %s, Blue: %s" % (red, green, blue))


method = input("input type Hex or RGB? ")
if method == "RGB":
    rgb_hex()
elif method == "Hex":
    hex_rgb()