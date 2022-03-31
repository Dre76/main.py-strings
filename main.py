# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer_name_one = 'Ruud Gullit'
scorer_name_two = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scorer_name_one + (" ") + str(goal_0)+ "," + (" ") + scorer_name_two + (" ") + str(goal_1)
print(scorers)

report = f'{scorer_name_one} scored in the {goal_0}nd minute\n{scorer_name_two} scored in the {goal_1}th minute'
print(report)

# deel 2

player = 'Ruud Gullit'
a = player.find(" ")
first_name = player[: a]
print(first_name)

spatie = player.find(' ')
last_name = player[spatie:]
print(last_name.strip())
last_name_len = len(last_name.strip())
print(last_name_len)

name_short = (first_name + last_name)
name_short = (first_name[0] + "." + last_name)
print(name_short)

chant = (first_name + "! ") * len(first_name)
chant = chant[:-1]
print(chant)

good_chant = chant != (" "[::])
print(2 != 2)
print(2 != 3)
















 













