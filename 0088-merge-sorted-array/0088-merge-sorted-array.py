class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        k = 0

        temp = [0] * (m + n)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp[k] = nums1[i]
                i += 1
            elif nums1[i] == nums2[j]:
                temp[k] = nums1[i]
                k += 1
                temp[k] = nums2[j]
                i += 1
                j += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            temp[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            temp[k] = nums2[j]
            j += 1
            k += 1

       
        for x in range(m + n):
            nums1[x] = temp[x]

    
             



     

        