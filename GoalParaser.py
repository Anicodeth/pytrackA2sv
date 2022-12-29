class Solution:
    def interpret(self, command: str) -> str:
        if '()' in command:
            command=command.replace('()','o')       
        if '(' in command:
            command=command.replace('(','')
        if ')' in command:
            command=command.replace(')','')
        return command
