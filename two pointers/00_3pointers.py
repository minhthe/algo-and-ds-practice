'''https://www.interviewbit.com/problems/minimize-the-absolute-difference/'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i, j, k = 0, 0 , 0 
        result = int(1e9)
        
        while i < len(A) and j < len(B) and k < len(C):
            result = min( result,  abs(   max( A[i],B[j],C[k] )- min( A[i],B[j],C[k] ) )  )
            # increase the min :
            if min( A[i],B[j],C[k] )  == A[i]: i += 1
            elif min( A[i],B[j],C[k] )  == B[j]: j += 1
            else: k += 1
        
        return result

