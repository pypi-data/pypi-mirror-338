"""
Shows different use cases of the library.
"""

from __future__ import print_function
from pyds import MassFunction
from itertools import product


print('=== creating mass functions ===')
m1 = MassFunction({'a':0.3, 'c':0.2, 'ab':0.2, 'ac':0.3}) # using a dictionary

m2 = MassFunction({'b':0.2, 'c':0.1, 'ab':0.5, 'abc':0.2}) # using a dictionary

print(m1.frame())

m12 = m1 & m2
print(m12)

m122 = m12&m2
print(m122)



# print('Dempster\'s combination rule for m_1 and m_2 (Monte-Carlo, importance sampling) =', m1.combine_conjunctive(m2, sample_count=1000, importance_sampling=True))
# print('Dempster\'s combination rule for m_1, m_2, and m_3 =', m1.combine_conjunctive(m2, m3))
# print('unnormalized conjunctive combination of m_1 and m_2 =', m1.combine_conjunctive(m2, normalization=False))
# print('unnormalized conjunctive combination of m_1 and m_2 (Monte-Carlo) =', m1.combine_conjunctive(m2, normalization=False, sample_count=1000))
# print('unnormalized conjunctive combination of m_1, m_2, and m_3 =', m1.combine_conjunctive([m2, m3], normalization=False))

# print('\n=== normalized and unnormalized conditioning ===')
# print('normalized conditioning of m_1 with {a, b} =', m1.condition({'a', 'b'}))
# print('unnormalized conditioning of m_1 with {b, c} =', m1.condition({'b', 'c'}, normalization=False))

# print('\n=== disjunctive combination rule (exact and approximate) ===')
# print('disjunctive combination of m_1 and m_2 =', m1 | m2)
# print('disjunctive combination of m_1 and m_2 (Monte-Carlo) =', m1.combine_disjunctive(m2, sample_count=1000))
# print('disjunctive combination of m_1, m_2, and m_3 =', m1.combine_disjunctive([m2, m3]))

# print('\n=== weight of conflict ===')
# print('weight of conflict between m_1 and m_2 =', m1.conflict(m2))
# print('weight of conflict between m_1 and m_2 (Monte-Carlo) =', m1.conflict(m2, sample_count=1000))
# print('weight of conflict between m_1, m_2, and m_3 =', m1.conflict([m2, m3]))

# print('\n=== pignistic transformation ===')
# print('pignistic transformation of m_1 =', m1.pignistic())
# print('pignistic transformation of m_2 =', m2.pignistic())
# print('pignistic transformation of m_3 =', m3.pignistic())

# print('\n=== local conflict uncertainty measure ===')
# print('local conflict of m_1 =', m1.local_conflict())
# print('entropy of the pignistic transformation of m_3 =', m3.pignistic().local_conflict())

# print('\n=== sampling ===')
# print('random samples drawn from m_1 =', m1.sample(5, quantization=False))
# print('sample frequencies of m_1 =', m1.sample(1000, quantization=False, as_dict=True))
# print('quantization of m_1 =', m1.sample(1000, as_dict=True))

# print('\n=== map: vacuous extension and projection ===')
# extended = m1.map(lambda h: product(h, {1, 2}))
# print('vacuous extension of m_1 to {1, 2} =', extended)
# projected = extended.map(lambda h: (t[0] for t in h))
# print('project m_1 back to its original frame =', projected)

# print('\n=== construct belief from data ===')
# hist = {'a':2, 'b':0, 'c':1}
# print('histogram:', hist)
# print('maximum likelihood:', MassFunction.from_samples(hist, 'bayesian', s=0))
# print('Laplace smoothing:', MassFunction.from_samples(hist, 'bayesian', s=1))
# print('IDM:', MassFunction.from_samples(hist, 'idm'))
# print('MaxBel:', MassFunction.from_samples(hist, 'maxbel'))
# print('MCD:', MassFunction.from_samples(hist, 'mcd'))
