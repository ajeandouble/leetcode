from typing import List


class Solution:
    # def parse(self):
    #     if self.expr[self.tok_idx] == "t":
    #         print("TRUE")
    #         self.tok_idx += 1
    #         return True
    #     elif self.expr[self.tok_idx] == "f":
    #         print("FALSE")
    #         self.tok_idx += 1
    #         return False
    #     elif self.expr[self.tok_idx] == "!":
    #         print("NOT")
    #         self.tok_idx += 2
    #         return not self.parse()
    #     elif self.expr[self.tok_idx] == "&":
    #         print("&(")
    #         self.tok_idx += 2
    #         return self.parse_and()
    #     elif self.expr[self.tok_idx] == "|":
    #         print("|(")
    #         self.tok_idx += 2
    #         return self.parse_or()

    # def parse_and(self):
    #     print(self.parse_and.__name__)
    #     result = self.parse()
    #     print(f"result={result}", result)
    #     # print(f"token == {self.expr[self.tok_idx]}")
    #     self.tok_idx += 1
    #     while self.tok_idx < len(self.expr) and self.expr[self.tok_idx] != ")":
    #         if self.expr[self.tok_idx] == ",":
    #             self.tok_idx += 1
    #         result &= self.parse()
    #         print(self.expr[self.tok_idx])
    #         self.tok_idx += 1
    #     return result

    # def parse_or(self):
    #     print(self.parse_or.__name__)
    #     result = self.parse()
    #     print(f"result={result}")
    #     print(f"token == {self.expr[self.tok_idx]}")
    #     self.tok_idx += 1
    #     while self.tok_idx < len(self.expr) and self.expr[self.tok_idx] != ")":
    #         print(f"{self.parse_or.__name__}, result={result}")
    #         if self.expr[self.tok_idx] == ",":
    #             self.tok_idx += 1
    #         result |= self.parse()
    #         print(f"result={result}")
    #         print(self.expr[self.tok_idx])
    #         self.tok_idx += 1
    #     return result

    #     pass

    def tokenize(self, expr):
        tokens = []
        i = 0
        while i < len(expr):
            print(i)
            if expr[i] == "t":
                tokens += ["TRUE"]
                i += 1
            elif expr[i] == "f":
                tokens += ["FALSE"]
                i += 1
            elif expr[i] == "&":
                tokens += ["AND"]
                i += 2
            elif expr[i] == "|":
                tokens += ["OR"]
                i += 2
            elif expr[i] == "!":
                tokens += ["NOT"]
                i += 2
            elif expr[i] == ")":
                tokens += ["RPAR"]
                i += 1
            elif expr[i] == ",":
                tokens += ["COMMA"]
                i += 1
        return tokens

    def parse(self):
        curr_token = self.tokens[self.tok_idx]
        if curr_token == "TRUE":
            self.tok_idx += 1
            return True
        elif curr_token == "FALSE":
            self.tok_idx += 1
            return False
        elif curr_token == "AND":
            self.tok_idx += 1
            return self.parse_and()
        elif curr_token == "OR":
            self.tok_idx += 1
            return self.parse_or()
        elif curr_token == "NOT":
            self.tok_idx += 1
            return not self.parse()

    def parse_and(self):
        result = self.parse()
        curr_token = self.tokens[self.tok_idx]
        while curr_token and curr_token != "RPAR":
            print("only commas ffs!", curr_token)
            print("whaaat", self.tokens[self.tok_idx])
            self.tok_idx += 1
            result &= self.parse()
            curr_token = (
                self.tokens[self.tok_idx] if self.tok_idx < len(self.tokens) else None
            )
        self.tok_idx += 1
        return result

    def parse_or(self):
        result = self.parse()
        curr_token = self.tokens[self.tok_idx]
        while curr_token and curr_token != "RPAR":
            print("only commas ffs!", self.tokens[self.tok_idx])
            self.tok_idx += 1
            result |= self.parse()
            curr_token = (
                self.tokens[self.tok_idx] if self.tok_idx < len(self.tokens) else None
            )
        self.tok_idx += 1
        return result

    def parseBoolExpr(self, expression: str) -> bool:
        self.tok_idx = 0
        self.tokens = self.tokenize(expression)
        print(self.tokens)
        return self.parse()


s = Solution()
# expr = "!(|(f,f,f,f,f,&(t,f)))"  # false
# ans = s.parseBoolExpr(expr)
# print(ans)

expr = "&(|(f),|(t,f))"  # false
ans = s.parseBoolExpr(expr)
print(ans)
