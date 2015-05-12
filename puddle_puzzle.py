"""
Copyright 2015 Daniel Rosensweig
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
http://creativecommons.org/licenses/by-nc-sa/4.0/

puddle_puzzle.py uses method puddle_size() to determine the volume of puddles between columns of provided heights.
Uses puzzle example heights as default.
For more info about the puzzle, see http://puzzles.bostonpython.com/puddle.html
"""

def puddle_size(heights=[2, 5, 1, 2, 3, 4, 7, 7, 6]):
	puddle = 0	#total size of all puddles so far (returned at end)
	tops = [(0,0)]	#list of local maximi. Each local top will be deleted once exceeded and puddle filled.
	filled_height = 0	#current height filled in the local puddle
	horiz = 0	#horizontal reference for which column we're working with
	prev = 0	#height of previous column
	inside = False	#tells whether the current puddle is inside a local max (i.e. not on left edge, where puddle falls off map

	for height in heights:
		top_num = len(tops) - 1	#tracks index in local max (last to first)
		while top_num >= 0:
			top = tops[top_num]	#current local max to be evaluated
			if height >= top[0]:	#We're above a local max, so something will be filled
				if inside:	#Make sure our puddle isn't falling off the graph
					puddle += (top[0] - filled_height) * (horiz - top[1] - 1)	#fill the puddle
				tops.pop()	#pop local max now that we've succeeded
				try: 
					tops[0]	#Make sure we still have something in tops
				except:
					tops.append((height, horiz))	#If not, current column is the new top
				filled_height=top[0]	#We've filled up to top[0]. Don't fill same space twice
			elif height > prev:	#We're below a local max, but above where we came from. Fill space in between
				if inside:	#make sure puddle isn't falling off the graph
					puddle += (height - filled_height) * (horiz - top[1] - 1)	#Fill the puddle
					filled_height = height	#We've filled to height. Don't fill same space again later.
			elif height < prev:	#Sloping down.
				if (tops[0] != (prev, horiz - 1)):	#Previous column was local max. Add to tops if not already there
					tops.append((prev, horiz - 1))
				filled_height = height	#Track filled height. In this case, it's the floor, not actual filled space
				inside = True	#If we weren't already, we're now inside the graph. Nothing falls off to the left
				break	#We're smaller than the previous, so we don't need to check other tops
			top_num -= 1	#Move to next top, if we didn't break before
		horiz += 1	#Moving to next column
		prev = height	#Set this column as previous, to be used in next run of the loop
	return puddle	#We're done. Return size of the filled puddle(s)

print(str(puddle_size()))	#10
print(str(puddle_size([2,5,1,2,3,4,1,2,3,4,4,1,7,2,7,6,4])))	#30
