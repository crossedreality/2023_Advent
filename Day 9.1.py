#region
class OasisReport:
    def __init__(self, seq):
        self.sequence = list(map(int, seq))
        self.nextval = self.getnext(self.sequence)
    
    def getnext(self, seq):
        diffseq = self.getdiff(seq)
        checkset = set(diffseq)
        if len(checkset) == 1 and 0 in checkset: return seq[-1] + 0
        else: return seq[-1] + self.getnext(diffseq)
    
    def getdiff(self, seq):
        diffs = []
        for i in range(1,len(seq)):
            diffs.append(seq[i] - seq[i - 1])
        return diffs
#endregion

reports = []
with open ('Working files/Day 9 Data.txt') as file:
    for line in file:
        reports.append(OasisReport(line.split()))

print(f"Sum of extrapolates: {sum(r.nextval for r in reports)}")