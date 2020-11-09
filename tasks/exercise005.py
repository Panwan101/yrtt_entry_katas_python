# Introduction
# The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed 
# stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator 
# returns to the usual seated position.

# The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. 
# In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously 
# around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, 
# the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating 
# waves have been produced. (Source Wikipedia)

# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

# Rules
#  1.  The input string will always be lower case but maybe empty.
#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(people):
    char_cntr=0
    rtn_list=[]
    for x in people:
        print(x)
        wave_str=""
        x_len=len(x)
        if x_len > 0:      #EMPTY STRING
            if x != " ":
                k = x.upper()
                print(k)
                wave_str=((people[0:(char_cntr)])+k+(people[(char_cntr+1):]))
                rtn_list.append((wave_str))
                print("rtn=",rtn_list)
        else:                  #else if empty
            wave_str=("")
            rtn_list.append((wave_str))
            break
        print(char_cntr)
        print(wave_str)
        char_cntr += 1
        print(rtn_list)
    return(rtn_list)