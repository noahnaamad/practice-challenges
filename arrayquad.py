def find_array_quadruplet(arr, s):
    sums = pairs(arr, s)
    return possible_pairings(sums)

def pairs(arr, s):
  arr_len = len(arr)
  #this dictionary's keys will be sums of each two elements in arr
  #the values will be pairs of indices that add to the key
  sums = {}
  for i in range(0,arr_len):
    for j in range(1, arr_len):
      if i == j:
        pass
      elif (arr[i] + arr[j]) in sums:
        sums[(arr[i] + arr[j])].append(i, j)
      else:
        sums[(arr[i] + arr[j])] = [i,j]
  return sums

def possible_pairings(sums, s):
    #iterate over the keys in sums (which are the possible summations of two elements in the given array) and determine if any two elements add to s.  if so, use find_exclusive_quad to determine if those sums are created using four unique indices from arr.
  list_sums = sums.keys()
  for k in range(0, len(list_sums)):
    for l in range(0, len(list_sums)):
      if list_sums[k] + list_sums[l] == s:
        candidates = [sums[k], sums[l]]
        if find_exclusivity(candidates)[0]:
          return find_exclusivity(candidates)[1]
  return false

def find_exclusive_quad(pairings):
    ##find four indices with no repeats
  a = pairings[0]
  b = pairings[1]
  for m in a:
    for n in b:
      if (m[0] != n[0]) & (m[0] != n[1]) & (m[1] != n[0]) & (m[1] != n[1]):
          quad = m + n
          return [True, quad]
  return [False]


  ##driver code
  #find find_exclusive_quad
# find_exclusive_quad([[[1,2]],[[3,4]]])
# print "2"
# find_exclusive_quad([[[1,2], [2,3]],[[3,4], [5,2], [5,6]]])
# print "3"
# find_exclusive_quad([[[1,2],[2,3]],[[2,4], [2,5], [5,2]]])

#possible_pairings
x = {10:[[1,2][3,4]]}
possible_pairings()
