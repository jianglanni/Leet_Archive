class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for star in asteroids:
            if star > mass:
                return False
            mass += star
        return True


def main():
    s = Solution()
    print(s.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))
    print(s.asteroidsDestroyed(5, [4, 9, 23, 4]))


if __name__ == "__main__":
    main()
