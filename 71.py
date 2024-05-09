class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = []
        folder = ""
        for c in path + "/":
            if c=='/':
                if folder=="..":
                    if paths:
                        paths.pop()
                elif folder!="" and folder!=".":
                    paths.append(folder)
                folder = ""
            else:
                folder += c

        return "/"+"/".join(paths)

Solution().
