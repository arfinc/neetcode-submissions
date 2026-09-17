class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []

        for op in operations:
            if op == "+":
                add = int(record[-1] + record[-2])
                record.append(add)
            elif op == "C":
                record.pop()
            elif op == "D":
                record.append(2 * record[-1])
            else:
                record.append(int(op))

        
        return sum(record)