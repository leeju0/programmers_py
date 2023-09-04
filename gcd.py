import math
def solution(numer1, denom1, numer2, denom2):
    child = numer1 * denom2 + numer2 * denom1
    mother = denom2 * denom1

    gcd = math.gcd(child,mother)
    answer = [child//gcd, mother//gcd]
    return answer


print(solution(1,2,3,4))
