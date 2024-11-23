def dec_to_bin(num):
    num = int(num)
    _list = []
    while num != 1:
        bin = str(num%2)
        _list.append(bin)
        num = num//2
    _list.append("1")
    _list.reverse()
    return "".join(_list)
    
def bin_to_dec(num):
    digit = 0
    for i,n in enumerate(num):
        if int(n) > 1:
            raise ValueError()
        if int(n) == 0:
            continue
        else:
            digit += int(n)*2**(len(num)-1-i)
    return str(digit)

def hex_to_dec(num):
    hex = {"A":"10","B":"11","C":"12","D":"13","E":"14","F":"15"}
    result = 0
    for i,n in enumerate(num):
        if n in hex:
            result += int(hex[n])*16**(len(num)-1-i)
        else:
            result += n*16**(len(num)-1-i)
            
    return str(result)
            
def dec_to_hex(num):
    hex = {"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    result = []
    num = int(num)
    while num >= 16:
        rem = num%16
        if rem < 10:
            result.append(str(rem))
        else:
            result.append(hex[str(rem)])
        num = (num-rem)//16
    if num < 10:
        result.append(str(num))
    else:
        result.append(str(num))
    result.reverse()
    return "".join(result)   
 
def bin_to_hex(num):
    return dec_to_hex(bin_to_dec(num))
    
        
def hex_to_bin(num):
    hex = {"A":"10","B":"11","C":"12","D":"13","E":"14","F":"15"}
    result = []
    for n in (num):
        if n == "0":
            result.append("0000")
        if n in hex:
            digit = dec_to_bin(hex[n])
            result.append(digit.zfill(4))
        else:
            dig = dec_to_bin(n)
            result.append(dig.zfill(4))  
    return "".join(result)
        
def oct_to_dec(num):
    result = 0
    for i,n in enumerate(num):
        if int(n) > 8:
            raise ValueError()
        if int(n) == 0:
            continue
        else:
            result += int(n)*8**(len(num)-1-i)
            return str(result)
            
def dec_to_oct(num):
    result = []
    num = int(num)
    while num > 8:
        rem = int(num)%8
        num = (num-rem)//8
        result.append(str(rem))
    result.reverse()
    return "".join(result)
def main():      
    try:
        number = input("Enter a number: ")
        operation = input("Select the operation you want to perform:\ndec-bin\nbin-dec\nhex-bin\nbin-hex\noct-dec\n\n")
        
        if operation == "dec-bin":
            print(dec_to_bin(number))
        elif operation == "bin-dec":
            print( bin_to_dec(number))
        elif operation == "hex-bin":
            print(hex_to_bin(number))
        elif operation == "oct-dec":
            print(oct_to_dec(number))
        elif operation == "bin-hex":
            print(bin_to_hex(number))
        elif operation == "dec-oct":
            print(dec_to_oct(number))
        elif operation == "hex-dec":
            print(hex_to_dec(number))
        elif operation == "dec-hex":
            print(dec_to_hex(number))
            
    except ValueError:
        print("Invalid input")
if __name__=="__main__":
    main()

