# Frida Kahlo Exhibition
# 
# You've been hired to work on a retrospective of Frida Kahlo's work at a major museum. Your job is to put together the audio tour, but in order to do that you need to create a list of each painting featured in the exhibit, the date it was painted, and its spot in the tour. 
# 
# Use your knowledge of Python lists to create a master list of each painting, its date, and its audio tour ID.  

# Task 1

paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']


# Task 2

dates = [1939, 1933, 1946, 1940]

# Task 3 

paintings = list(zip(paintings, dates))
print(paintings)

# Task 4

paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

# ## Task 5

print(len(paintings))

# Task 6

audio_tour_number = [i for i in range(1, len(paintings)+1)]
print(audio_tour_number)

# Task 7 

master_list = list(zip(audio_tour_number, paintings))

# Task 8 

print(master_list)

