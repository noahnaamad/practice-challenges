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

def possible_pairings(sums)
  list_sums = sums.keys()
  for k in range(0, len(list_sums)):
    for l in range(0, len(list_sums)):
      if list_sums[k] + list_sums[l] == s:
        candidates = [sums[k], sums[l]]
        if find_exclusivity(candidates)[0]:
          return find_exclusivity(candidates)[1]
  return false

def find_exclusivity(idx)
  a = idx[0]
  b = idx[1]
  for m in a:
    for n in b:
      if (m[0] != n[0]) && (m[0] != n[1]) && (m[1] != n[0]) && (m[1] != n[1]):
          quad = m + n
          return [True, quad]
  return [False]
