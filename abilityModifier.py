class abilityModifier:
    table = {3:[-3, 'No spellcasting possible', 'No spellcasting possible'],
             4:[-2, -2, 1],
             5:[-2, -2, 1],
             6:[-1, -1, 1],
             7:[-1, -1, 1],
             8:[-1, 0, 2],
             9:[0, 0, 2],
             10:[0, 0, 3],
             11:[0, 0, 3],
             12:[0, 0, 4],
             13:[1, 0, 4],
             14:[1, 1, 5],
             15:[1, 1, 5],
             16:[2, 1, 6],
             17:[2, 2, 6],
             18:[3, 2, 7]}


    def getModifiers(self, n):
        return self.table.get(n)