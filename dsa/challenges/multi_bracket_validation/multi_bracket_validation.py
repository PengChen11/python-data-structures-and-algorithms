import re

def multi_bracket_validation(str_input):
    if str_input.count("{")==str_input.count("}") and str_input.count("(")==str_input.count(")") and str_input.count("[")==str_input.count("]"):#Check uneven number of brackets. if happens, return False

        if str_input.count("[") != 0:
            if str_input.rfind("]")<str_input.rfind("["):#reverse check whether openning brackets appears after closing brackets.
                return False
            square_check = re.split("\(|\{|\}|\)",str_input)
            if len(square_check)==1:
                if str_input.find("]")<str_input.find("["):#check whether openning brackets appears after closing brackets.
                    return False
            else:
                for i in range(1,len(square_check)):
                    if square_check[i].find("]")<square_check[i].find("["):#check space inside of an open and closing other type of brackets, to see whether a square bracket inside of it is not closed.
                        return False

        if str_input.count("{") != 0:
            if str_input.rfind("}")<str_input.rfind("{"):
                return False
            curly_check = re.split("\[|\]|\(|\)",str_input)
            if len(curly_check)==1:
                if str_input.find("}")<str_input.find("{"):
                    return False
            else:
                for i in range(1,len(curly_check)):
                    if curly_check[i].find("}")<curly_check[i].find("{"):
                        return False

        if str_input.count("(") != 0:
            if str_input.rfind(")")<str_input.rfind("("):
                return False
            small_check = re.split("\{|\}|\[|\]",str_input)
            if len(small_check)==1:
                if str_input.find(")")<str_input.find("("):
                    return False
            else:
                for i in range(1,len(small_check)):
                    if small_check[i].find(")")<small_check[i].find("("):
                        return False

        return True
    return False

if __name__ == "__main__":
    print(multi_bracket_validation("][[[][]]"))
