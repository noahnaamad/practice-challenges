def diff_number(arr)
	if arr.length == FIXNUM_MAX + 1
		return nil
	else
		hashed_arr = convert_arr_to_hash(arr)
		missing_num = 0
		loop do #O(n) time to execute
			if !hashed_arr[missing_num]
				return missing_num
			end
			missing_num +=1
		end
	end
end

def convert_arr_to_hash(arr) #O(n) time to execute, O(n) space
	hashed_arr = {}
	arr.each do |element|
		hashed_arr[element] = true
	end
	hashed_arr
end

##the algorithm takes two actions in sequence, each of them
##costing O(n) time.  Total time complexity is O(n)

##the algorithm creates a hash as long as the array, so
##space complexity is O(n)