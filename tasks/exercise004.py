# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    txt_list=text.split(" ")
    pig_text=""
    for i in txt_list:
        txt_len=len(i)
        stxt_len=len(i.strip("!@#$%^&*()_+?.,;:`"))
        if stxt_len < txt_len :
            pig_word=(i[1:stxt_len] + i[0] + "ay" + i[stxt_len:txt_len] + " ")
        else:
            pig_word=(i[1:stxt_len] + i[0] + "ay ")
        pig_text=pig_text + pig_word
        rtn_text=pig_text.strip()
    return(rtn_text)