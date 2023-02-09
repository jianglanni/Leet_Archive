class Solution:
    def sortTheStudents(self, score, k):
        score.sort(reverse=True, key=lambda x: x[k])
        return score
