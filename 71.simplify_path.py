class Solution:
    def simplifyPath(self, path: str) -> str:

        dir_list = []

        for d in path.split('/'):
            if d =='..':
                if dir_list: dir_list.pop()
            elif d !='' and d !='.':
                dir_list.append(d)
        
        return '/'+'/'.join(dir_list)



        