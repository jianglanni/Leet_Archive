class Solution:
    def distinctNames(self, ideas) -> int:
        groupy = dict()
        for idea in ideas:
            if idea[0] not in groupy:
                groupy[idea[0]] = {idea[1:]}
            else:
                groupy[idea[0]].add(idea[1:])
        initials = list(groupy.keys())
        ret = 0
        for i in range(len(initials)-1):
            for j in range(i+1, len(initials)):
                overlap = len(groupy[initials[i]].intersection(groupy[initials[j]]))
                ret += (len(groupy[initials[i]])-overlap) * (len(groupy[initials[j]])-overlap)
        return ret*2
