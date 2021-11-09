import string

def key_maker(key):
    '''
        This function will create a key dictionary for cipher
    '''

    alpha = string.ascii_lowercase
    d = {}

    for idx in range (len(alpha)):
        
        shift = idx + key
        d[alpha[idx]] = alpha[ shift % 26 ]

    return d


def textstrip(sherlock):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    f=open(sherlock,'r', encoding = 'utf8')
    s = f.read().lower()

    alpha = string.ascii_lowercase
    lower_string = ""

    for letter in s:

        if letter in alpha:
            lower_string = lower_string + letter

    return lower_string
    
def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''

    alpha = string.ascii_lowercase
    d = {}

    for i in alpha:
        d[i] = 0

    for i in s:
        d[i] += 1

    for key in d :
        d[key] = d[key]/len(s)

    return d



def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    
    encrypt_text = ""

    for i in s:

        encrypt_text = encrypt_text + d[i]

    return encrypt_text
    

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''

    cypher_dic = {}

    for key in d:

        cypher_dic[d[key]] = key
    
    return substitution_encrypt(s, cypher_dic)

def max_freq_find(d):
    '''
    This function finds the key with the maximum frequency in the dictionary d
    '''

    maxfreq = -1
    maxletter = ""

    for key in d:
        
        if (d[key] > maxfreq):
            maxfreq = d[key]
            maxletter = key
    
    return maxletter



def cryptanalyse_substitution(s, decrypt_freq_dic):

    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''

    encrypt_freq_dic = letter_distribution(s)

    original_letter = max_freq_find(decrypt_freq_dic)
    encrypt_letter = max_freq_find(encrypt_freq_dic)

    alpha = string.ascii_lowercase

    index_original = alpha.index(original_letter)
    index_encrypt = alpha.index(encrypt_letter)

    key = index_encrypt - index_original

    return key_maker(key)



def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''

    alpha = string.ascii_lowercase

    encrypt_text = ""
    pass_len = len(password)


    for i in range(len(s)):
        
        s_index = alpha.index(s[i])
        p_index = alpha.index(password[i % pass_len])

        encrypt_text = encrypt_text + alpha[(s_index + p_index) % 26]

    return encrypt_text






def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''

    decrypt_text = ""

    alpha = string.ascii_lowercase
    pass_len = len(password)

    for i in range(len(s)):
        
        s_index = alpha.index(s[i])
        p_index = alpha.index(password[i % pass_len])

        decrypt_text = decrypt_text + alpha[(s_index - p_index) % 26]

    return decrypt_text


def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    
    right_string = s[-r:]
    left_string = s[:-r]

    rotated_string  = right_string + left_string
    count=0

    for i in range(len(s)):
        
        if s[i] == rotated_string[i]:
            count+=1

    return count/len(s)


def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''

    password = ""
    alpha = string.ascii_lowercase

    for i in range (k):

        T = ""
        for j in range(i,len(s),k):
            
            T = T + s[j]

        sub_dic = letter_distribution(T)

        max_key = max_freq_find(sub_dic)

        key = alpha.index(max_key) - alpha.index('e')

        if key < 0 :
            key+=26

        password += alpha[key]
    
    return password


def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    for i in range (1,100):
        cf = int(rotate_compare(s, i)*100)
        if(cf == 6):
            return i



def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    length_pass = cryptanalyse_vigenere_findlength(s)
    password = cryptanalyse_vigenere_afterlength(s, length_pass)
    print("password - ", password)
    print(vigenere_decrypt(s,password))




s = textstrip("sherlock.txt")


# Function calls

# freq_dic = letter_distribution(s)
# keydic = key_maker(12)
# encrypt_text = substitution_encrypt(s, keydic)
# encrypt_text = vigenere_encrypt(s,'nitin')
# cryptanalyse_vigenere(encrypt_text)


